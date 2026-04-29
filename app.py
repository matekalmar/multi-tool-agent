from pathlib import Path

from langchain.messages import HumanMessage
import streamlit as st

from src.multi_tool_agent.agent import build_agent
from src.multi_tool_agent.config import AppConfig

st.set_page_config(
    page_title="Multi Tool Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("Multi Tool Agent")
st.write("Kérdezz a CSV vagy PDF adatok alapján.")

@st.cache_resource
def load_agent():
    config = AppConfig(
        csv_path=Path("data/sales.csv"),
        pdf_path=Path("data/kisvallalati_ado_szabalyzat.pdf"),
    )

    multi_tool_agent, context, tools = build_agent(config)

    return multi_tool_agent, context, tools


multi_tool_agent, context, tools = load_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Tegyél fel egy kérdést...")

if prompt:
    st.session_state.messages.append({
        "role" : "user",
        "content" : prompt
    })
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Gondolkodom..."):
            response = multi_tool_agent.invoke({
                "messages" : [HumanMessage(content=prompt)]
            })["messages"][-1].content
            st.write(response)
    st.session_state.messages.append({
        "role" : "assistant",
        "content" : response
    })