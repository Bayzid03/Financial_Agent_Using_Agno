import streamlit as st
from Financial_Agent import agents

st.set_page_config(page_title="Financial Agent", layout="wide")
st.title("💹 Financial Agent")

st.markdown(
    "Ask any financial question (e.g., *What is the current stock price of Apple Inc. (AAPL)?*)"
)

user_query = st.text_area("Your question:", height=100)

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            response = agents.print_response(user_query, stream=False)
            st.markdown(response)
    else:
        st.warning("Please enter a question.")