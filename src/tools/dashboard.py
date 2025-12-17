import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Methodology 3.0 Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🚀 Project Office Methodology 3.0")
st.markdown("### AI-enhanced, PMBOK® 8 Compliant Project Management")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to", ["Overview", "Projects", "AI Analysis", "Documentation"])
    
    st.markdown("---")
    st.header("Quick Actions")
    if st.button("🔄 Refresh"):
        st.rerun()

# Main content
if page == "Overview":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Projects", "0", "Ready")
    with col2:
        st.metric("AI Adoption", "0%", "Pending")
    with col3:
        st.metric("Compliance", "0%", "Not started")
    st.info("🎯 Next: Add your methodology files to the created directories.")

elif page == "Projects":
    st.header("📋 Project Management")
    with st.form("create_project"):
        name = st.text_input("Project Name")
        ptype = st.selectbox("Project Office Type", ["Type 1", "Type 2", "Type 3"])
        submitted = st.form_submit_button("Create Project")
        if submitted:
            st.success(f"✅ Project '{name}' created!")

elif page == "AI Analysis":
    st.header("🤖 AI Analysis")
    st.write("AI modules for benefits prediction, risk intelligence, and sustainability assessment.")

elif page == "Documentation":
    st.header("📚 Documentation")
    st.write("Add your methodology content to the docs/ directory.")

st.markdown("---")
st.caption(f"Methodology 3.0 | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
