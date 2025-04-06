import ollama

import streamlit as st
from db import get_all_customers
import requests

st.set_page_config(page_title="Customer360 AI", layout="wide")

st.title("🧠 Customer360: Multi-Agent Assistant")

prompt = st.text_input("Ask me anything about your customers:")

if prompt:
    response = ollama.chat(model='phi', messages=[{"role": "user", "content": prompt}])
    st.write("🤖 Agent says:")
    st.success(response["message"]["content"])

st.markdown("### 📊 All Customers in DB")
customers = get_all_customers()
st.table(customers)
