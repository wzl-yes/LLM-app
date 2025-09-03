import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")


llm_base_url = st.sidebar.text_input("LLM Base URL", value="https://dashscope.aliyuncs.com/compatible-mode/v1", type="default")
llm_model = st.sidebar.text_input("LLM Model", value="deepseek-v3.1", type="default")
llm_api_key = st.sidebar.text_input("LLM API Key", type="password")


def generate_response(input_text):
    model = ChatOpenAI(
        temperature=0.7,
        api_key=llm_api_key,
        base_url=llm_base_url,  # 可自定义
        model_name=llm_model             # 可自定义
    )
    message = model.invoke(input_text)
    st.info(message.content)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:"
    )
    submitted = st.form_submit_button("Submit")
    if not llm_api_key.startswith("sk-"):
        st.warning("Please enter your LLM API key!", icon="⚠")
    if submitted and llm_api_key.startswith("sk-"):
        generate_response(text)