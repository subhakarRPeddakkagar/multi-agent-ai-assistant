from langchain_groq import ChatGroq
from app.config import get_secret

def debug_agent(state):
    api_key = get_secret("GROQ_API_KEY")
    if not api_key:
        return {"error": "Missing GROQ_API_KEY"}

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=api_key
    )

    code = state.get("code", "")[:1500]

    response = llm.invoke(f"Fix bugs in this code:\n{code}")

    return {
        "task": state.get("task"),
        "research": state.get("research"),
        "code": code,
        "final_code": response.content
    }