# RAG Evaluation Framework — Findings Report

**System Under Test:** WhiteOWL Research Workbench (AI Research Assistant, RAG pipeline)
**Test Corpus:** *Atomic Habits* by James Clear — Chapter 19, "The Goldilocks Rule"
**Evaluation Framework:** RAGAS v0.4.3
**Generation Model (SUT):** `gpt-4o-mini`
**Judge Model (RAGAS):** `gpt-4o-mini`
**Mode Tested:** Uploaded-files only (web search disabled)
**Records Evaluated:** 11 scoreable + 2 blocked-by-defect
**Author:** Raghav — Software Quality Analyst / AI QA

---

## 1. Methodology

### 1.1 Grey-Box Evaluation via Network-Layer Inspection

The initial plan assumed a **black-box** evaluation: no access to retrieved chunks, forcing document-level summaries to be used as proxy contexts. **This assumption was disproven during testing.**

Inspection of WebSocket traffic in Chrome DevTools revealed an `internal_context` field in the response payload containing the **complete retrieval set** for every query:

| Field | Contents |
|---|---|
| `internal_context` | All retrieved chunks — `id`, `text`, `page_number`, cosine `score` |
| `internal_sources` | Only the chunks cited in the final answer |
| `llm_model` | The generation model in use (`gpt-4o-mini`) |
| `conversation_flow` | Clarification state and generated follow-up questions |

**Reclassification:** This is a **Grey-Box evaluation** — retrieval internals are accessible via the network layer without developer access, backend permissions, or code instrumentation.

**Why it matters:** All four RAGAS metrics become *accurate* rather than *directional*. Faithfulness, Context Precision, and Context Recall all require real retrieved contexts; proxy summaries would have made three of the four metrics unreliable.

### 1.2 Dataset Construction

| RAGAS field (v0.4 API) | Source |
|---|---|
| `user_input` | Question designed by QA |
| `response` | Answer returned by the Workbench |
| `retrieved_contexts` | Top 7 chunks by cosine score, extracted from `internal_context` |
| `reference` | Ground truth written by QA from the source text |

**Ground truth policy (deliberate methodology choice):**
- **Pure factual questions** → verbatim source text is acceptable (a single correct answer exists).
- **Inference and multi-part questions** → ground truth written in QA's own words, to test whether the system *synthesized* correctly rather than merely copied.

**Retrieval window decision:** The system returns **K=50 chunks** per query. The **top 7 by cosine score** were used as `retrieved_contexts` — the realistic grounding set. Scoring against all 50 would depress Context Precision by construction, since most of the 50 are unrelated content. Documented as a deliberate scoping decision.

### 1.3 Test Design — Question Type Coverage

| Type | What it stresses | Target | Captured |
|---|---|---|---|
| Happy Path | Basic retrieval + clean generation | 4 | 3 |
| Multi-part | Context Recall — were *all* pieces retrieved? | 2 | 2 |
| Inference | Generation-layer synthesis, not lookup | 3 | 3 |
| Specific Fact | Precise number/name retrieval | 3 | 2 |
| Out-of-Scope | Hallucination resistance | 2 | 1 |
| **Total** | | **14** | **11 scoreable + 2 blocked** |

The shortfall between target and captured is **itself a finding** — see Finding 1.

---

## 2. Quantitative Results

### 2.1 Aggregate Scores (n = 11)

| Metric | Mean | Reading |
|---|---|---|
| **Faithfulness** | **0.9437** | Strong — the system does not fabricate |
| **Answer Relevancy** | **0.7438** | Weakest metric — answers over-elaborate and drift |
| **Context Precision** | **0.8997** | Good overall — but two clear outliers (see Finding 3) |
| **Context Recall** | **0.8238** | Acceptable — two significant outliers |

### 2.2 Per-Question Breakdown

| # | Question (abbrev.) | Type | Faith. | Ans. Rel. | Ctx Prec. | Ctx Recall |
|---|---|---|---|---|---|---|
| Q1 | What is the Goldilocks Rule? | Happy Path | 0.917 | 0.618 | **0.585** | **0.500** |
| Q2 | Top performers vs everyone else | Inference | 0.929 | **0.297** * | 0.915 | 1.000 |
| Q3 | Professionals vs amateurs | Happy Path | 1.000 | 0.931 | **0.643** | 0.667 |
| Q4 | What is a flow state? | Happy Path | 0.846 | 0.978 | 1.000 | 0.667 |
| Q5 | Motivation factors + boredom + flow | Multi-part | 1.000 | 0.668 | 1.000 | 1.000 |
| Q6 | Goldilocks + boredom + professionals | Multi-part | 0.955 | 0.578 | 1.000 | 1.000 |
| Q7 | Why boredom, not failure? | Inference | 1.000 | 0.901 | 0.948 | **0.429** |
| Q8 | Flow ↔ just-manageable difficulty | Inference | 1.000 | 0.854 | 1.000 | 0.800 |
| Q9 | How far beyond ability for flow? (4%) | Specific Fact | 1.000 | 0.690 | 1.000 | 1.000 |
| Q10 | What is the Yerkes-Dodson law? | Specific Fact | 0.917 | 0.702 | 1.000 | 1.000 |
| Q13 | Does the book discuss cryptocurrency? | Out-of-Scope | 0.818 | 0.965 | 0.806 | 1.000 |

**\* Q2 — known data-integrity caveat.** The `user_input` recorded for Q2 is the *original* phrasing ("What is the difference between best athletes and everyone?"), which the system **rejected with a clarification request** and which therefore never produced the recorded answer. The answer came from a rephrased query. Answer Relevancy works by generating questions from the answer and comparing them to `user_input` — so **0.297 reflects a question/answer mismatch in the dataset, not a system failure.** This record must be re-captured with matched inputs before the score is cited. Flagged openly rather than silently corrected.

### 2.3 Score Stability Caveat

RAGAS requests **3 generations** per LLM-judged metric and averages them for stability. Throughout execution the judge model returned only 1:

```
LLM returned 1 generations instead of requested 3. Proceeding with 1 generations.
```

All scores are therefore **single-sample** and carry more variance than RAGAS defaults intend. Directionally sound; not precise to the third decimal.

---

## 3. Defects and Findings

### FINDING 1 — Clarification classifier over-triggers, masking retrieval failure
**Severity: HIGH** · **Reproduced 6× across 4 distinct questions**

The system returns `clarification_type: insufficient_context` — with `answer: ""` and `internal_context: null` — for questions whose answers **exist verbatim in indexed, retrievable chunks**.

| # | Query | Anchoring used | Result |
|---|---|---|---|
| 1 | "What is the difference between best athletes and everyone?" | none | Clarification |
| 2 | "How many percent beyond your current ability… flow state?" | none | Clarification |
| 3 | "According to *Atomic Habits*, in what year did the ten-year-old boy walk into Disneyland?" | document named | Clarification |
| 4 | "According to *Atomic Habits*, what year did **Steve Martin** first visit Disneyland?" | document + entity | Clarification |
| 5 | "According to *Atomic Habits*, tell me the story of the comedian who visited Disneyland as a boy." | document + narrative framing | Clarification |
| 6 | "According to *Atomic Habits*, what did **Machiavelli** say about novelty?" | document + entity | Clarification |

**Proof the content was retrievable:**
- The **Disneyland / Steve Martin** chunk (p.177) was retrieved for Q1 at cosine **0.8254**.
- The **Machiavelli / novelty** chunk (p.181) was retrieved for Q5 (**0.8280**) and Q7 (**0.8629**).

Both chunks are indexed, embedded, and score well — yet direct queries targeting them are rejected as "insufficient context."

**Root-cause hypothesis:** The clarification classifier runs **before, or independently of, retrieval**. It judges insufficiency from the *question text alone* and never checks whether relevant chunks exist. Supporting evidence: the generated clarification questions frequently **restate the user's own intent** back to them — asked about the Steve Martin anecdote, the system replied *"Are you looking for a specific anecdote related to Steve Martin?"* This circularity indicates no retrieval grounding.

**Impact:**
- Indexed content becomes **unreachable** via direct query.
- The user is **misinformed** — told their question was unclear, when the real event was a retrieval/routing failure.
- A user cannot distinguish *"your question was unclear"* from *"this content doesn't exist"* — both return an identical response. (Confirmed: the same clarification shape was returned for a valid in-corpus fact **and** for a genuinely out-of-scope question about protein intake.)

**Recommendation:** Run retrieval first. Trigger clarification only when retrieval returns nothing above threshold. Distinguish "not found in document" from "question ambiguous" in the user-facing response.

---

### FINDING 2 — *(REFUTED by data — retained for methodological transparency)*

**Original hypothesis:** *"Retrieval precision collapses on short, single-concept queries."*

**Status: REFUTED.**

The hypothesis was formed by counting off-topic chunks in the top 7. Q9 showed 4 of 7 off-topic; Q10 showed 6 of 7. This looked damning.

**The measured scores contradict it directly:**

| Question | Off-topic chunks in top 7 | Measured Context Precision |
|---|---|---|
| Q9 (short factual) | 4 of 7 | **1.000** |
| Q10 (short factual) | 6 of 7 | **1.000** |

**Why the hypothesis failed:** `LLMContextPrecisionWithReference` is **rank-aware**. It evaluates whether *relevant* chunks appear at the *top* of the ranking, weighted by position. In both Q9 and Q10 the single correct chunk sat at **rank #1**, and no other chunk was needed to answer the question — so precision is perfect regardless of what sits below it.

**Lesson:** raw chunk-relevance counts are not a proxy for Context Precision. The metric measures *ranking quality*, not *noise volume*. The hypothesis conflated the two.

**What remains true:** the noise is real and carries a genuine cost — token spend and distraction risk at generation time (see Finding 9). It simply does not manifest as low Context Precision.

*This finding is deliberately preserved rather than deleted. A hypothesis was formed, tested against data, and refuted. Recording that is more honest — and more useful — than a report in which every prediction conveniently holds.*

---

### FINDING 3 — Junk chunks at rank #1 are the true driver of low precision
**Severity: MEDIUM–HIGH** · **Quantitatively confirmed**

With Finding 2 refuted, the data points to the real cause. The two lowest Context Precision scores in the suite share one trait: **a junk chunk occupying the top of the ranking.**

| Question | Ctx Precision | Chunk at/near rank #1 |
|---|---|---|
| **Q1** | **0.585** | `"Just right. THE GOLDILOCKS RULE"` — a **page heading fragment**, cosine **0.8797**, ranked **#1 of 50** |
| **Q3** | **0.643** | A **back-of-book index entry** (`"professionals vs. amateurs, 236…"`), cosine 0.831 — and it was **cited to the user** |

Every other question in the suite scored **0.92–1.00** on Context Precision.

**Root cause A — heading fragments as standalone chunks.** The chunker treats a page heading as its own chunk. Because the heading text nearly duplicates the query text, it achieves artificially high embedding similarity — a **lexical-overlap false positive**. In Q1 it out-ranked the chunk that actually defines the rule (the tennis / Federer / Serena passage, 0.8279, rank #3).

**Root cause B — non-prose content ingested as first-class chunks.** The book's index, notes, and bibliography sections are embedded and retrieved like ordinary content. An index entry is a page-number lookup table with no answerable content, yet it was surfaced *as a citation*.

**Impact:** directly measurable — roughly a 35–40% precision penalty on affected queries. Wastes top-K slots and surfaces non-answers as sources.

**Recommendation:**
1. Merge heading fragments into their following content block; enforce a minimum token threshold per chunk.
2. Filter index, table-of-contents, and bibliography sections at ingestion.

---

### FINDING 4 — Answer Relevancy is the system's weakest dimension
**Severity: MEDIUM** · **Mean 0.744 — lowest of the four metrics**

Excluding the Q2 data artifact, five of ten records score **below 0.71**:

| Question | Ans. Relevancy | Pattern |
|---|---|---|
| Q6 | 0.578 | Long multi-paragraph answer with a summary appended |
| Q1 | 0.618 | Definition question answered with a tennis analogy, a flow tangent, and a closing summary |
| Q5 | 0.668 | Verbose synthesis |
| Q9 | 0.690 | Simple 4% fact padded with unrequested elaboration |
| Q10 | 0.702 | Yerkes-Dodson definition padded with a comedian example |

**Pattern:** the system **over-answers**. It reliably includes the correct content (Faithfulness 0.944) but surrounds it with unrequested elaboration, examples, and summaries. RAGAS measures relevancy by generating questions *from the answer* and comparing them to the original query — padding pulls those generated questions away from what was actually asked.

Contrast: Q4 (0.978) and Q3 (0.931) scored high because they answered tightly.

**Impact:** users receive correct but bloated answers. Higher token cost, lower signal density, worse UX.

**Recommendation:** tighten the generation prompt toward answer scope — instruct the model to answer the question asked and stop.

---

### FINDING 5 — Two different root causes behind low Context Recall
**Severity: MEDIUM** · **Q1 (0.500), Q7 (0.429)**

**Q1 — a generation-layer failure.** Retrieval **succeeded**. The chapter-summary chunk (rank #2, cosine 0.8677) contained the chapter's central thesis: *"Anyone can work hard when they feel motivated. It's the ability to keep going when work isn't exciting that makes the difference."* The generated answer mentioned boredom only as a "threat" and **never delivered this insight** — the actual point of the chapter. The context was present, ranked high, and available to the LLM. The LLM did not use it.

**Q7 — a retrieval-layer failure (lowest recall in the suite).** An inference question whose ground truth spanned the novelty-craving mechanism, the boredom-as-obstacle argument, *and* the professional/amateur distinction. The retrieved contexts supported only part of it. A synthesis-heavy question needs chunks assembled from across the chapter, and the retriever did not gather the full set.

**Combined signal:** the two lowest-recall records fail for **different reasons** — one in generation, one in retrieval. A single aggregate recall score would have hidden this. Both warrant separate attention.

---

### FINDING 6 — Most relevant chunk ranked ~21st of 50
**Severity: MEDIUM** · **Ranking failure, Q2**

For the "top performers vs everyone else" query, the chunk containing the **literal answer** — the coach's line:

> *"At some point it comes down to who can handle the boredom of training every day… Really successful people feel the same lack of motivation as everyone else. The difference is that they still find a way to show up despite the feelings of boredom."*

— scored **0.7990**, ranking approximately **21st of 50**, and was **not cited**. Chunks about genetics, explore/exploit trade-offs, and competence-in-context all ranked above it.

**Impact:** under a standard top-K cutoff (K=5 or 7), the single most relevant passage would be **excluded entirely** from the grounding set.

*Methodology note: this chunk was manually included in the Q2 record's top-7 — a documented QA override. Strict "top-N by raw score" would have omitted the correct answer, rendering the record meaningless.*

---

### FINDING 7 — Citation list empty despite a grounded, cited answer
**Severity: MEDIUM** · **Q10**

The response payload for Q10 showed:

```
"internal_sources": [],
"external_sources": [],
```

Both empty — yet the answer text carried a citation marker referencing chunk `67c5e1e2`, and that chunk was present in `internal_context` at **rank #1** (cosine 0.8669). The answer was correctly grounded (Faithfulness 0.917); the **UI would display no sources at all**.

Compare with Q9, where `internal_sources` was correctly populated. The behaviour is inconsistent.

**Impact:** users lose the ability to verify a correct answer. Undermines trust in an otherwise sound response.

---

### FINDING 8 — Persistent false-positive cluster: "systems vs goals" summaries
**Severity: LOW–MEDIUM** · **Observed in Q3, Q4, Q9, Q10, Q13**

Two chunks — the Chapter 1 summary (p.27) and "A System of Atomic Habits" (p.26) — appear in the top 7 for questions on **entirely unrelated topics**, consistently scoring 0.83–0.85. They surfaced for questions about professionals vs amateurs, flow state, the Yerkes-Dodson law, and even cryptocurrency.

**Root-cause hypothesis:** high-level summary chunks contain broad, topic-neutral vocabulary ("habits," "system," "results," "improvement") that yields a **high baseline similarity to any query about the book**. They act as semantic attractors.

**Impact:** consumes top-K slots on nearly every query. Per Finding 2, this does *not* directly depress Context Precision — but it does inflate token cost and adds distraction risk at generation time.

---

### FINDING 9 — Retrieval is wide, grounding is narrow
**Severity: INFORMATIONAL** · **Architectural observation**

The system retrieves **K=50 chunks** per query but cites only **1–2** in the final answer.

Chunks ranked 25–50 routinely score 0.77–0.79 and cover entirely unrelated material (junk food and supernormal stimuli, the Law of Least Effort, Goodhart's Law, delayed gratification).

**Open question for the development team:** are all 50 chunks passed into the generation prompt, or only the top few? If all 50, this represents significant token cost and a real distraction risk — which would connect directly to the over-elaboration pattern in Finding 4.

---

### FINDING 10 — Out-of-scope handling is correct
**Severity: PASS** · **Q13 — positive result**

Asked *"Does Atomic Habits discuss cryptocurrency investing?"*, the system responded correctly:

> *"'Atomic Habits' does not specifically discuss cryptocurrency investing…"*

**No hallucination.** It declined cleanly and explained what the book *does* cover. Scores: Faithfulness 0.818, Answer Relevancy 0.965, Context Recall 1.000.

**Supporting signal:** retrieval scores for this query clustered at **0.79–0.81** — measurably below the 0.83–0.90 range seen on in-scope queries. The system's own similarity scores correctly reflected the absence of relevant content.

**Assessment:** hallucination resistance on clearly out-of-domain questions is a genuine strength.

---

## 4. Environment Notes

### RAGAS v0.4.3 — upstream import bug

Installing `ragas 0.4.3` alongside `langchain-community 0.4.2` produces an immediate crash on import:

```
ModuleNotFoundError: No module named 'langchain_community.chat_models.vertexai'
```

**Cause:** `ragas/llms/base.py` eagerly imports `ChatVertexAI` from a module path that newer `langchain-community` releases removed. The import fires even for OpenAI-only users who never touch VertexAI.

**Tracking:** [ragas issue #2741](https://github.com/vibrantlabsai/ragas/issues/2741) (open); fix proposed in PR #2739 (unmerged at time of testing).

**Workaround applied:** wrapped the VertexAI import in `try/except ImportError` and made `MULTIPLE_COMPLETION_SUPPORTED` extend conditionally only when VertexAI is available.

**Caveat:** this patch lives in `site-packages` and will be lost on reinstall. Long-term: pin compatible versions or await the upstream merge.

### RAGAS v0.4 — dataset schema renaming

RAGAS v0.4 renamed the schema. Most tutorials online still use the v0.1 names, which fail on the current release.

| v0.1 (legacy — most tutorials) | v0.4 (current) |
|---|---|
| `question` | `user_input` |
| `answer` | `response` |
| `contexts` | `retrieved_contexts` |
| `ground_truth` | `reference` |

Construction also moved from `Dataset.from_dict()` to `SingleTurnSample` objects wrapped in an `EvaluationDataset`.

---

## 5. Summary for Stakeholders

### What works

- **Faithfulness 0.944** — the system does not fabricate. Answers stay grounded in retrieved content.
- **Out-of-scope questions are correctly declined** without hallucination, and retrieval scores correctly drop when relevant content is absent.
- **Multi-concept queries retrieve cleanly** — Q5, Q6, Q8 all achieved perfect Context Precision.

### What needs attention — priority order

| # | Issue | Severity | Evidence |
|---|---|---|---|
| 1 | Clarification classifier blocks answerable questions and masks retrieval failure | **HIGH** | 6 reproductions; content proven retrievable at 0.82–0.86 |
| 2 | Junk chunks (heading fragments, book index) rank #1 and get cited | **MED-HIGH** | Q1 precision 0.585, Q3 precision 0.643 vs 0.92–1.00 elsewhere |
| 3 | Answers over-elaborate beyond the question asked | **MED** | Answer Relevancy 0.744 — lowest metric; 5 of 10 below 0.71 |
| 4 | Generation drops key insights that retrieval successfully surfaced | **MED** | Q1 Context Recall 0.500 despite the answer chunk ranking #2 |
| 5 | Retrieval fails to assemble full context for synthesis questions | **MED** | Q7 Context Recall 0.429 — lowest in suite |
| 6 | Most relevant chunk ranked ~21st of 50; not cited | **MED** | Q2 coach quote, cosine 0.799 |
| 7 | Citation list returned empty despite a grounded, cited answer | **MED** | Q10 — `internal_sources: []` |

### Known limitations of this evaluation

- **n = 11.** Small sample. Findings are directional; a larger suite would firm up the pattern claims.
- **Single-generation scoring.** RAGAS defaults to 3 generations per LLM-judged metric; the judge returned 1. Scores carry more variance than intended.
- **Judge model = system model.** Both are `gpt-4o-mini`. A stronger, independent judge would reduce the risk of the evaluator sharing the system's blind spots. Known weakness; clear next step.
- **Q2 has a question/answer mismatch** (see §2.2). Its Answer Relevancy of 0.297 should not be cited until the record is re-captured.
- **Specific Fact category is incomplete** (2 of 3) — not through oversight, but because the system refused to answer narrow factual queries (Finding 1). The inability to construct the test set is itself the result.

---

*Self-directed AI QA evaluation. All findings are reproducible from the captured network payloads and the RAGAS dataset in this repository. Where a hypothesis was refuted by measurement (Finding 2), the refutation is documented rather than removed.*
