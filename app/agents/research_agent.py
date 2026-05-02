from tavily import TavilyClient

def research_agent(state):
    client = TavilyClient(api_key="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")

    task = state.get("task", "")

    short_query = task.split("\n")[0][:200]

    results = client.search(
        query=short_query,
        max_results=2   # ✅ REDUCED
    )

    formatted = "\n".join([r["content"][:300] for r in results["results"]])

    return {
        "input": state.get("input"),
        "task": task,
        "research": formatted
    }