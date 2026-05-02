import time
from app.graph.workflow import build_graph

graph = build_graph()

def run_system(user_input):
    time.sleep(2)  # ✅ avoid rate burst
    return graph.invoke({"input": user_input})