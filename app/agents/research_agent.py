from tavily import TavilyClient
from app.config import get_secret

def research_agent(state):
    api_key = get_secret("TAVILY_API_KEY")
    if not api_key:
        return {
            "task": state.get("task"),
            "research": "No Tavily key provided"
        }

    client = TavilyClient(api_key=api_key)

    task = state.get("task", "")
    query = task.split("\n")[0][:200] or "software development"

    results = client.search(query=query, max_results=2)

    formatted = "\n".join([r["content"][:300] for r in results["results"]])

    return {
        "input": state.get("input"),
        "task": task,
        "research": formatted
    }