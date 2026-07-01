import streamlit as st

st.set_page_config(page_title="AI Career Hub", layout="wide")

st.title("🚀 Welcome to AI Career Intelligence Suite")
st.markdown("An advanced AI-powered pipeline designed to optimize your job application strategy.")
st.markdown("---")

st.subheader("🛠️ Platform Core Modules (Select from the sidebar)")
col1, col2 = st.columns(2)

with col1:
    st.info("""
    ### 🎯 1. ATS Resume Matcher
    * **Status:** 🔥 Fully Functional
    * **Action:** Click **"1 📊 ATS Matcher"** in the left sidebar to start.
    """)

with col2:
    st.success("""
    ### 💬 2. AI STAR Interview Coach
    * **Status:** ⏳ Coming Soon
    """)