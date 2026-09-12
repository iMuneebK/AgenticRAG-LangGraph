import os
from typing import Dict, TypedDict, List

class AgentState(TypedDict):
    question: str
    generation: str
    web_search: bool
    documents: List[str]

class AgenticRAG:
    def __init__(self):
        self.state = {}

    def retrieve_documents(self, state: AgentState) -> AgentState:
        print("---RETRIEVING DOCUMENTS FROM VECTOR DB---")
        state['documents'] = ["Document 1: Contextual details on AI agentic RAG.", "Document 2: ReAct framework guidelines."]
        return state

    def grade_documents(self, state: AgentState) -> AgentState:
        print("---CHECKING DOCUMENT RELEVANCE---")
        state['web_search'] = False
        return state

    def generate_answer(self, state: AgentState) -> AgentState:
        print("---GENERATING ANSWER WITH REFLECTION---")
        state['generation'] = "Agentic RAG answer synthesized with self-reflection and grade evaluation."
        return state
