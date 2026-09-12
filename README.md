# 🧠 Autonomous Agentic RAG System (LangGraph + ReAct)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red)

An advanced Agentic Retrieval-Augmented Generation (RAG) system built with LangGraph, ReAct framework, self-reflection, document relevance grading, and web search fallback.

## 🏗️ Architecture
```mermaid
graph TD
    User[Query Input] --> Router[Router Node]
    Router --> Retrieve[Vector Store Retrieval]
    Retrieve --> Grade[Document Relevance Grader]
    Grade -- Relevant --> Generate[LLM Synthesis & Reflection]
    Grade -- Not Relevant --> Search[Tavily Web Search Fallback]
    Search --> Generate
    Generate --> Output[Final Output]
```
