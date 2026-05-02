from langchain_groq import ChatGroq

def task_agent(state):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key="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"
    )

    user_input = state["input"]

    response = llm.invoke(f"""
You are a senior software engineer.

Break this task into clear coding steps ONLY.
Do NOT give project management advice.

Focus on:
- API structure
- endpoints
- database
- authentication

Task:
{user_input}
""")

    return {
        "input": user_input,
        "task": response.content
    }