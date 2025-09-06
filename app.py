from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("My LLM App")
st.write("#### 専門家への質問フォーム")
st.write("質問したい専門家を選択し、質問内容を入力してください。")

selected_expert = st.radio(
    "専門家を選択してください。",
    ("法律", "政治")
)

user_input = st.text_area("質問を入力してください")

if selected_expert == "法律":
    messages = [
        SystemMessage(content="あなたは法律の専門家です。"),
        HumanMessage(content=user_input)
    ]
else:
    messages = [
        SystemMessage(content="あなたは政治の専門家です。"),
        HumanMessage(content=user_input)
    ]

if st.button("送信"):
    st.divider()
    response = llm(messages)

    if user_input:
        st.write(f"選択した専門家: {selected_expert}")
        st.write("回答:")
        if hasattr(response, "content"):
            st.write(response.content)
        else:
            st.error("エラー: 応答に 'content' 属性がありません。")
    else:
        st.warning("質問内容を入力してください。")