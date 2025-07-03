
import streamlit as st
from orchestrator.task_manager import TaskManager

st.title("🧠 GenAI Research Agent")
query = st.text_input("Enter your research question:")

if query:
    task_manager = TaskManager()
    with st.spinner("Thinking..."):
        result = task_manager.handle_task(query)
    st.success("Done!")
    st.write(result)
