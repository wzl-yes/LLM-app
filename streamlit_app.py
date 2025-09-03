import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

# 初始化对话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

llm_base_url = st.sidebar.text_input("LLM Base URL", value="https://dashscope.aliyuncs.com/compatible-mode/v1", type="default")
llm_model = st.sidebar.text_input("LLM Model", value="deepseek-v3.1", type="default")
llm_api_key = st.sidebar.text_input("LLM API Key", type="password")


def generate_response(input_text):
    model = ChatOpenAI(
        temperature=0.7,
        api_key=llm_api_key,
        base_url=llm_base_url,
        model_name=llm_model
    )
    message = model.invoke(input_text)
    return message.content


# 显示对话历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# 用户输入
if prompt := st.chat_input("说点什么..."):
    if not llm_api_key.startswith("sk-"):
        st.warning("Please enter your LLM API key!", icon="⚠")
    else:
        # 添加用户消息
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 生成助手回复
        with st.chat_message("assistant"):
            response = generate_response(prompt)
            st.markdown(response)

        # 添加助手消息到历史
        st.session_state.messages.append({"role": "assistant", "content": response})