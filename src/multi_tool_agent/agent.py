from langchain.agents import create_agent
from .context import build_context
from .config import AppConfig
from .prompts import SYSTEM_PROMPT
from .tools import (
    make_calculate_tool,
    make_analyze_csv_tool,
    make_search_document_tool,
)

def make_tools(context):
    calculate = make_calculate_tool()
    analyze_csv = make_analyze_csv_tool(context)
    search_document = make_search_document_tool(context)
    return [calculate, analyze_csv, search_document]

def build_agent(config: AppConfig):
    context = build_context(config)
    tools = make_tools(context)

    agent = create_agent(
        model=config.agent_model,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

    return agent, context, tools