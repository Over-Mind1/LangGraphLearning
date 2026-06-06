from typing import Literal

from langchain_core.messages import AIMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from agent_state import AgentState

from llm import LLM
from search_tool import ddg_search, get_user_data


# =========================
# setup model
# =========================

llm = LLM().get_model()

tools = [
    ddg_search,
    get_user_data,
]

llm_with_tools = llm.bind_tools(tools)

tool_node = ToolNode(tools)


# =========================
# agent node
# =========================

def agent_node(state: AgentState):

    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# =========================
# router
# =========================

def should_continue(
    state: AgentState
) -> Literal["tools", "__end__"]:

    last_message = state["messages"][-1]

    if isinstance(last_message, AIMessage):

        if last_message.tool_calls:
            return "tools"

    return "__end__"


# =========================
# graph
# =========================

graph_builder = StateGraph(AgentState)

graph_builder.add_node(
    "agent",
    agent_node
)

graph_builder.add_node(
    "tools",
    tool_node
)

graph_builder.set_entry_point(
    "agent"
)

graph_builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "__end__": END
    }
)

graph_builder.add_edge(
    "tools",
    "agent"
)

react_graph = graph_builder.compile()