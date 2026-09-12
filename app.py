import streamlit as st
from agent_graph import AgenticRAG

st.set_page_config(page_title="Agentic RAG Workflow", layout="wide")
st.title("🧠 Autonomous Agentic RAG System (LangGraph + ReAct)")
st.caption("Self-reflecting, multi-vector router RAG agent with fallback search.")

user_query = st.text_input("Ask a complex technical question:")
if user_query:
    rag = AgenticRAG()
    initial_state = {'question': user_query, 'generation': '', 'web_search': False, 'documents': []}
    s1 = rag.retrieve_documents(initial_state)
    s2 = rag.grade_documents(s1)
    s3 = rag.generate_answer(s2)
    st.success(s3['generation'])
