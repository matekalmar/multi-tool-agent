from pathlib import Path
from langchain.messages import HumanMessage
from .agent import build_agent
from .config import AppConfig

def main():
    config = AppConfig(
        csv_path=Path("data/sales.csv"),
        pdf_path=Path("data/kisvallalati_ado_szabalyzat.pdf"),
    )

    multi_tool_agent, context, tools = build_agent(config)

    while True:
        question = input("Kérdés: ").strip()
        if question.lower() in {"q", "quit", "exit"}:
            break

        response = multi_tool_agent.invoke(
            {"messages": [HumanMessage(content=question)]}
        )
        print(response)
        print()

if __name__ == "__main__":
    main()