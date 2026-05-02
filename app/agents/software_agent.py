from langchain_groq import ChatGroq
from app.config import get_secret

def software_agent(state):
    api_key = get_secret("GROQ_API_KEY")
    if not api_key:
        return {"error": "Missing GROQ_API_KEY"}

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=api_key
    )

    task = state.get("task", "")

    response = llm.invoke(f"""
Write minimal working code only.
No explanations.

Task:
{task}
""")

    return {
        "input": state.get("input"),
        "task": task,
        "research": state.get("research"),
        "code": response.content
    }