# RAG Evaluation Framework

Grey-box evaluation of a production RAG system using [RAGAS](https://github.com/vibrantlabsai/ragas). Automated retrieval and generation quality testing, built from real retrieval data captured at the network layer.

**System under test:** WhiteOWL Research Workbench (AI research assistant, RAG pipeline)
**Test corpus:** *Atomic Habits* by James Clear, Chapter 19, "The Goldilocks Rule"
**Framework:** RAGAS v0.4.3
**Generation model (SUT):** `gpt-4o-mini` | **Judge model (RAGAS):** `gpt-4o-mini`

---

## Why this exists

Most RAG evaluation tutorials assume you own the pipeline. This project asks a different question: **how much can a QA engineer evaluate when all they have is the UI and a browser?**

The initial plan was a black-box evaluation, using document summaries as proxy contexts. That assumption was disproven during testing. Chrome DevTools showed the WebSocket response payload contained the full retrieval set for every query, including each chunk's text, page number, and cosine score. That makes this a **grey-box** evaluation: real retrieved contexts, no developer access, no backend permissions, and no code instrumentation.

Real contexts matter because three of the four RAGAS metrics (Faithfulness, Context Precision, Context Recall) need them. With proxy summaries those scores would only be directional. With captured chunks they are accurate.

## What gets measured

| Metric | RAGAS class | What it checks |
| --- | --- | --- |
| Faithfulness | `Faithfulness` | Is the answer grounded in the retrieved context, or hallucinated? |
| Answer Relevancy | `ResponseRelevancy` | Does the answer actually address the question asked? |
| Context Precision | `LLMContextPrecisionWithReference` | Are the relevant chunks ranked at the top? |
| Context Recall | `LLMContextRecall` | Did retrieval surface everything needed to answer? |

## Repository layout

```
.
├── dataset.py      # Test dataset: 11 captured records as RAGAS SingleTurnSample objects
├── evaluate.py     # Runner: scores the dataset with the four metrics, writes a CSV
├── FINDINGS.md     # Full findings report: methodology, scores, defects, recommendations
└── .gitignore
```

## Dataset

Each record in `dataset.py` maps to the RAGAS v0.4 schema.

| RAGAS field | Source |
| --- | --- |
| `user_input` | Question designed by QA. |
| `response` | Answer returned by the system, verbatim from the capture. |
| `retrieved_contexts` | Top 7 chunks by cosine score, taken from the captured `internal_context`. |
| `reference` | Ground truth written by QA from the source text. |

**Design decisions:**

- **Top 7 of 50.** The system retrieves K=50 chunks per query. Scoring against all 50 would depress Context Precision by construction, so the top 7 is used as the realistic grounding set.
- **Ground truth policy.** Pure factual questions use verbatim source text. Inference and multi-part questions use QA's own wording, to test whether the system synthesized rather than copied.
- **Question types covered:** happy path, multi-part, inference, specific fact, and out-of-scope (hallucination resistance).

Records are numbered Q1 to Q13. Q11, Q12 and Q14 are absent because the system's clarification classifier refused to answer those questions (see Finding 1 in `FINDINGS.md`).

## Getting started

### Prerequisites

- Python 3.10+.
- An OpenAI API key. RAGAS calls the OpenAI API for both the judge LLM and embeddings.

### Install

```bash
git clone https://github.com/RraghavVohra/rag-evaluation-framework786.git
cd rag-evaluation-framework786

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install ragas==0.4.3 langchain-openai python-dotenv pandas
```

### Configure

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-key-here
```

### Run

```bash
python evaluate.py
```

This runs all four metrics over the dataset, prints the aggregate scores, and saves per-record results to `results/full_evaluation.csv`.

## Headline results (n = 11)

| Metric | Mean | Reading |
| --- | --- | --- |
| Faithfulness | 0.944 | Strong. The system does not fabricate. |
| Answer Relevancy | 0.744 | Weakest. Answers over-elaborate and drift. |
| Context Precision | 0.900 | Good overall, with two outliers caused by junk chunks at rank #1. |
| Context Recall | 0.824 | Acceptable, with two outliers that fail for different reasons. |

**Top findings:**

- **Clarification classifier over-triggers (HIGH).** Answerable questions are rejected as "insufficient context", even though the answer chunks were retrievable. Reproduced 6 times across 4 distinct questions.
- **Junk chunks at rank #1 (MED-HIGH).** Heading fragments and back-of-book index entries rank first and get cited, cutting precision by roughly 35-40% on affected queries.
- **Over-answering (MED).** Correct content wrapped in unrequested examples and summaries, which drags Answer Relevancy down.
- **Out-of-scope handling is correct (PASS).** The system declines cleanly without hallucinating.

One hypothesis (low precision on short queries) was **refuted by the data** and is kept in the report deliberately. The full write-up, with evidence and recommendations for every finding, is in [`FINDINGS.md`](./FINDINGS.md).

## Known limitations

- **Small sample.** n = 11, so findings are directional.
- **Single-sample scoring.** RAGAS requests 3 generations per LLM-judged metric, but the judge returned only 1. Scores carry more variance than RAGAS defaults intend.
- **Judge equals system model.** Both are `gpt-4o-mini`. A stronger, independent judge would reduce shared blind spots.
- **Q2 data mismatch.** Its recorded `user_input` is the original phrasing that the system rejected, while the answer came from a rephrased query. Its Answer Relevancy of 0.297 reflects that mismatch and should not be cited until the record is re-captured.
- **Manual override on Q2.** The coach-quote chunk (ranked about 21st of 50) was manually included in the top 7. Strict top-N by score would have excluded the correct answer.

## Environment notes

**RAGAS 0.4.3 import crash.** Installing `ragas 0.4.3` with `langchain-community 0.4.2` fails on import with `ModuleNotFoundError: No module named 'langchain_community.chat_models.vertexai'`, because RAGAS eagerly imports a module path that newer `langchain-community` releases removed. This happens even for OpenAI-only users. It is tracked upstream in [ragas issue #2741](https://github.com/vibrantlabsai/ragas/issues/2741). If you hit it, either pin compatible versions or wrap the VertexAI import in `ragas/llms/base.py` in a `try/except ImportError`. Note that a patch inside `site-packages` is lost on reinstall.

**RAGAS v0.4 schema renames.** Most online tutorials use the v0.1 names, which fail on the current release.

| v0.1 (legacy) | v0.4 (current) |
| --- | --- |
| `question` | `user_input` |
| `answer` | `response` |
| `contexts` | `retrieved_contexts` |
| `ground_truth` | `reference` |

Construction also moved from `Dataset.from_dict()` to `SingleTurnSample` objects wrapped in an `EvaluationDataset`.

## Adapting this to another RAG system

1. Open the app in Chrome and watch the Network tab (WebSocket or XHR) while asking a question.
2. Look for a payload field exposing the retrieved chunks. If one exists, you can run a grey-box evaluation without any backend access.
3. For each test question, record the question, the returned answer, the top-N retrieved chunks, and a ground truth written from the source material.
4. Add each record to `dataset.py` as a `SingleTurnSample` and include it in `load_dataset()`.
5. Run `python evaluate.py`.

## Author

**Raghav Vohra**, Software Quality Analyst. Self-directed AI QA evaluation.