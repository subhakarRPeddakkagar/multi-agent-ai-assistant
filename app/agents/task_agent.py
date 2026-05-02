from langchain_groq import ChatGroq
from app.config import get_secret

def task_agent(state):
    api_key = get_secret("GROQ_API_KEY")
    if not api_key:
        return {"error": "Missing GROQ_API_KEY"}

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=api_key
    )

    user_input = state["input"]
    response = llm.invoke(f"""
You are a senior software engineer.
Break this task into coding steps only.

Task:
{user_input}
""")

    return {
        "input": user_input,
        "task": response.content
    }