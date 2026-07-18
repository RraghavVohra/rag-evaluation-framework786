"""
RAGAS Evaluation Framework - Runner
Runs the four core metrics against the WhiteOWL capture and saves results.
"""
import os
from dotenv import load_dotenv

from ragas import evaluate
from ragas.metrics import (
    Faithfulness,
    ResponseRelevancy,
    LLMContextPrecisionWithReference,
    LLMContextRecall,
)
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from dataset import load_dataset

load_dotenv()  # reads OPENAI_API_KEY from your .env file


def main():
    # RAGAS uses an LLM as the internal judge + embeddings for similarity
    judge_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))
    judge_emb = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model="text-embedding-3-small"))

    metrics = [
        Faithfulness(llm=judge_llm),                          # hallucination check
        ResponseRelevancy(llm=judge_llm, embeddings=judge_emb),  # answer relevancy
        LLMContextPrecisionWithReference(llm=judge_llm),      # retrieval precision
        LLMContextRecall(llm=judge_llm),                      # retrieval recall
    ]

    dataset = load_dataset()

    print("Running RAGAS evaluation... (this calls the OpenAI API)\n")
    results = evaluate(dataset=dataset, metrics=metrics)
    print(results)

    os.makedirs("results", exist_ok=True)
    df = results.to_pandas()
    df.to_csv("results/full_evaluation.csv", index=False)
    print("\nSaved -> results/full_evaluation.csv")


if __name__ == "__main__":
    main()