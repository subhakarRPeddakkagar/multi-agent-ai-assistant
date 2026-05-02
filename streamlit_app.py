import streamlit as st
from app.main import run_system

st.title("🤖 Multi-Agent AI Assistant")

user_input = st.text_input("Enter your task:")

if st.button("Run AI Team"):
    if not user_input:
        st.warning("Please enter a task")
    else:
        result = run_system(user_input)

        # ✅ handle errors
        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader("🧠 Task Breakdown")
            st.write(result.get("task", "No output"))

            st.subheader("🔍 Research")
            st.write(result.get("research", "No output"))

            st.subheader("💻 Generated Code")
            st.code(result.get("code", "No output"))

            st.subheader("🐞 Fixed Code")
            st.code(result.get("final_code", "No output"))