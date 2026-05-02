from langchain_groq import ChatGroq

def debug_agent(state):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key="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"
    )

    code = state.get("code", "")

    # ✅ FIX: reduce token usage
    short_code = code[:1500]

    response = llm.invoke(f"""
Fix bugs in this code (keep answer short):

{short_code}
""")

    return {
        "task": state.get("task"),
        "research": state.get("research"),
        "code": code,
        "final_code": response.content
    }