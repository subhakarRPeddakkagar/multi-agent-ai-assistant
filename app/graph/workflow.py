from langgraph.graph import StateGraph

from app.agents.task_agent import task_agent
from app.agents.research_agent import research_agent
from app.agents.software_agent import software_agent
from app.agents.debug_agent import debug_agent

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("task", task_agent)
    graph.add_node("research", research_agent)
    graph.add_node("code", software_agent)
    graph.add_node("debug", debug_agent)

    graph.set_entry_point("task")

    graph.add_edge("task", "research")
    graph.add_edge("research", "code")
    graph.add_edge("code", "debug")

    return graph.compile()