import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Methodology 3.0 Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS
# ============================================================================

st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 20px;
        color: white;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE
# ============================================================================

if 'projects' not in st.session_state:
    st.session_state.projects = []
if 'view' not in st.session_state:
    st.session_state.view = 'dashboard'

# ============================================================================
# SAMPLE DATA
# ============================================================================

def create_sample_data():
    return [
        {
            "id": "PROJ-001",
            "name": "Digital Transformation",
            "type": "Type 2",
            "phase": "C",
            "health": 85,
            "ai_adoption": 65,
            "sustainability": 78,
            "created": "2024-01-10"
        },
        {
            "id": "PROJ-002",
            "name": "AI Implementation",
            "type": "Type 1",
            "phase": "B",
            "health": 72,
            "ai_adoption": 80,
            "sustainability": 85,
            "created": "2024-01-05"
        },
        {
            "id": "PROJ-003", 
            "name": "Sustainability Initiative",
            "type": "Type 3",
            "phase": "A",
            "health": 90,
            "ai_adoption": 45,
            "sustainability": 95,
            "created": "2024-01-15"
        }
    ]

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.title("🚀 Methodology 3.0")
    st.caption("AI-Enhanced Project Management")
    
    st.markdown("---")
    
    # Navigation
    view = st.radio(
        "📊 Navigation",
        ["Dashboard", "Projects", "AI Analytics", "Methodology", "Reports", "Settings"],
        key="nav"
    )
    st.session_state.view = view.lower().replace(" ", "_")
    
    st.markdown("---")
    
    # Quick Stats
    st.subheader("📈 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Projects", "3", "+1")
    with col2:
        st.metric("Avg Health", "82", "+5")
    
    st.markdown("---")
    st.caption(f"v3.0 • {datetime.now().strftime('%Y-%m-%d')}")

# ============================================================================
# MAIN CONTENT
# ============================================================================

if st.session_state.view == "dashboard":
    st.title("📊 Methodology 3.0 Dashboard")
    st.markdown("### AI-Enhanced Project Management System")
    
    st.markdown("---")
    
    # Key Metrics
    st.subheader("🎯 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Projects", "3", "+1")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Active Projects", "3", "100%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("AI Adoption", "63%", "+8%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Sustainability", "86/100", "+12")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Projects Table
    st.subheader("📋 Recent Projects")
    projects = create_sample_data()
    df = pd.DataFrame(projects)
    st.dataframe(
        df[['name', 'type', 'phase', 'health', 'ai_adoption']],
        column_config={
            "name": "Project",
            "type": "Type", 
            "phase": "Phase",
            "health": st.column_config.ProgressColumn(
                "Health",
                format="%d",
                min_value=0,
                max_value=100,
            ),
            "ai_adoption": st.column_config.ProgressColumn(
                "AI %", 
                format="%d%%",
                min_value=0,
                max_value=100,
            )
        },
        hide_index=True,
        use_container_width=True
    )

elif st.session_state.view == "projects":
    st.title("📋 Project Portfolio")
    st.markdown("### Manage All Projects")
    
    # Create project cards
    projects = create_sample_data()
    cols = st.columns(3)
    
    for i, project in enumerate(projects):
        with cols[i % 3]:
            # Health indicator
            if project['health'] >= 80:
                color = "#10B981"
                icon = "🟢"
            elif project['health'] >= 60:
                color = "#F59E0B"
                icon = "🟡"
            else:
                color = "#EF4444"
                icon = "🔴"
            
            st.markdown(f"""
            <div style="border: 1px solid #e5e7eb; border-radius: 10px; padding: 15px; margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0;">{project['name']}</h4>
                    <span style="background: {color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8em;">
                        {icon} {project['health']}
                    </span>
                </div>
                <p style="color: #6b7280; font-size: 0.9em; margin: 10px 0;">
                    {project['type']} • Phase {project['phase']}
                </p>
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <small>AI</small><br>
                        <strong>{project['ai_adoption']}%</strong>
                    </div>
                    <div>
                        <small>Sustainability</small><br>
                        <strong>{project['sustainability']}/100</strong>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.view == "ai_analytics":
    st.title("🤖 AI Analytics Studio")
    st.markdown("### Advanced AI-Powered Analysis")
    
    tab1, tab2, tab3 = st.tabs(["🧠 Benefits", "⚠️ Risk", "🌱 Sustainability"])
    
    with tab1:
        st.subheader("Benefits Prediction")
        # Simple chart
        data = pd.DataFrame({
            'Benefit': ['Cost Reduction', 'Efficiency', 'Quality', 'Revenue'],
            'Planned': [50000, 75000, 30000, 100000],
            'Predicted': [45000, 70000, 28000, 85000]
        })
        
        st.bar_chart(data.set_index('Benefit'))
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Planned", ",000")
        with col2:
            st.metric("Predicted", ",000")
        with col3:
            st.metric("Value at Risk", ",000")
    
    with tab2:
        st.subheader("Risk Intelligence")
        risk_data = pd.DataFrame({
            'Risk': ['Schedule Delay', 'Budget Overrun', 'Technical Issues', 'Stakeholder'],
            'Probability': [0.7, 0.4, 0.6, 0.3],
            'Impact': [0.8, 0.9, 0.7, 0.6]
        })
        st.dataframe(risk_data, use_container_width=True)
    
    with tab3:
        st.subheader("Sustainability Analytics")
        esg_data = pd.DataFrame({
            'Category': ['Environmental', 'Social', 'Governance'],
            'Score': [75, 82, 88],
            'Target': [85, 85, 90]
        })
        st.dataframe(esg_data, use_container_width=True)

elif st.session_state.view == "methodology":
    st.title("📚 Methodology 3.0")
    st.markdown("### Complete AI-Enhanced Framework")
    
    stages = {
        "I": "AI-Powered Start-up",
        "II": "Intelligent Execution", 
        "III": "Predictive Benefits Realization",
        "IV": "AI-Guided Close & Learning"
    }
    
    for stage_id, stage_name in stages.items():
        with st.expander(f"Stage {stage_id}: {stage_name}", expanded=True):
            st.write(f"**Description:** {stage_name}")
            if stage_id == "I":
                st.write("- Phase A: AI-Enhanced Start-up")
                st.write("- Phase B: Predictive Maturity Assessment")
                st.write("- Phase W: Sustainability Integration")
            elif stage_id == "II":
                st.write("- Phase C: Predictive Planning")
                st.write("- Phase D: Smart Resource Management")
                st.write("- Phase H: Benefits Intelligence")

elif st.session_state.view == "reports":
    st.title("📈 Reports & Analytics")
    st.markdown("### Generate Professional Reports")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Quick Reports")
        if st.button("📋 Project Health Report", use_container_width=True):
            st.success("Generating report...")
        if st.button("💰 Benefits Analysis", use_container_width=True):
            st.success("Generating report...")
        if st.button("⚠️ Risk Assessment", use_container_width=True):
            st.success("Generating report...")
    
    with col2:
        st.subheader("Custom Report")
        with st.form("custom_report"):
            report_type = st.selectbox("Type", ["Executive", "Detailed", "Dashboard"])
            format_type = st.selectbox("Format", ["PDF", "HTML", "Excel"])
            if st.form_submit_button("Generate"):
                st.success(f"Generating {report_type} report in {format_type} format!")

elif st.session_state.view == "settings":
    st.title("⚙️ Settings")
    st.markdown("### Configure Your Dashboard")
    
    tab1, tab2 = st.tabs(["Dashboard", "AI"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Theme", ["Light", "Dark", "System"])
            st.selectbox("Refresh Rate", ["30s", "1m", "5m", "15m"])
        with col2:
            st.checkbox("Show Notifications", True)
            st.checkbox("Compact Mode", False)
        
        if st.button("Save Settings", type="primary"):
            st.success("Settings saved!")
    
    with tab2:
        st.checkbox("Benefits Prediction", True)
        st.checkbox("Risk Intelligence", True)
        st.checkbox("Sustainability Analytics", True)
        st.slider("AI Confidence Threshold", 0.0, 1.0, 0.7)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.caption(f"Project Office Methodology 3.0 • {datetime.now().strftime('%Y-%m-%d %H:%M')} • Deployed on Streamlit Cloud")
