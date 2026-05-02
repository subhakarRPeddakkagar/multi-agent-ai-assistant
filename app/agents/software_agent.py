from langchain_groq import ChatGroq

def software_agent(state):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key="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"
    )

    task = state.get("task", "")
    research = state.get("research", "")

    response = llm.invoke(f"""
Write MINIMAL working code only.

Do not add explanations.
Do not add extra features.

Task:
{task}
""")

    return {
        "input": state.get("input"),
        "task": task,
        "research": research,
        "code": response.content
    }