import streamlit as st
import pandas as pd
from langchain_community.llms import Ollama
import datetime

# Performance: Using Llama3 via Ollama
llm = Ollama(model="llama3")

st.set_page_config(page_title="Strategic Intervention Engine", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- Feature Engineering & Heuristic Intelligence ---
def get_strategic_trigger(row):
    """
    Simulates a Propensity Model (BTC - Best Time to Contact).
    Weights: 
    1. Historical Success (Last_Success_Time)
    2. Sector/Industry Habits (Basket Analysis Logic)
    3. Urgency Penalty (Pay_Drift)
    """
    history = str(row.get('Last_Success_Time', 'None'))
    sector = row['Sector']
    drift = row['Pay_Drift']
    
    # Feature 1: Historical Override (The strongest signal)
    if history != 'None':
        return history, 98, "Verified Historical Engagement Pattern"

    # Feature 2: Sector-Based Propensity (Target-style 'Customer Persona' logic)
    sector_intelligence = {
        'Tech': ("7:45 PM", 85, "Post-deep-work/Evening browsing window"),
        'Healthcare': ("8:30 AM", 78, "Shift-change transition period"),
        'Civil Servant': ("5:15 PM", 90, "End-of-day commute receptivity"),
        'Self-Employed': ("9:00 AM", 65, "Pre-client-meeting administrative window")
    }
    
    time, score, reason = sector_intelligence.get(sector, ("12:30 PM", 50, "General Lunch Baseline"))
    
    # Feature 3: Urgency Weighting (A/B Test Logic)
    if drift > 15:
        score -= 10 # High stress reduces receptivity
        reason += " | Urgency Escalation: Strategy shifted to early-cycle intervention."
        
    return time, score, reason

# --- Sidebar & Demo Data Generation ---
st.sidebar.title("🛠️ Project Controls")
if st.sidebar.checkbox("🚀 Enable Demo Mode", value=True):
    # Creating Dummy Feature Data for the 'Wow' factor
    data = {
        'Acct_ID': [1001, 1002, 1003, 1004, 1005],
        'Sector': ['Tech', 'Healthcare', 'Self-Employed', 'Civil Servant', 'Tech'],
        'Pay_Drift': [8, 0, 15, 3, 25],
        'ACH_Active': ['No', 'Yes', 'No', 'Yes', 'No'],
        'Last_Success_Time': ['19:45', 'None', '09:15', 'None', '20:30'],
        'Last_Item_Purchased': ['Cloud Storage', 'Stethoscope', 'Business Software', 'Stationery', 'Monitor'], # Target-style feature
        'Balance': [12500, 8500, 45000, 1200, 32000]
    }
    df = pd.DataFrame(data)
else:
    uploaded = st.sidebar.file_uploader("Upload CSV", type="csv")
    if uploaded: df = pd.read_csv(uploaded)
    else: st.stop()

# --- Strategic Risk Scoring ---
df['Risk_Score'] = df.apply(lambda r: (40 if r['Sector'] in ['Tech', 'Self-Employed'] else 10) + 
                                     (30 if r['Pay_Drift'] > 7 else 0) + 
                                     (30 if r['ACH_Active'] == 'No' else 0), axis=1)

# --- Dashboard UI ---
st.title("🛡️ Strategic Intervention Engine")
st.markdown("### *Propensity-Driven Asset Recovery*")

c1, c2, c3 = st.columns(3)
c1.metric("Portfolio Risk", f"${df[df['Risk_Score'] >= 70]['Balance'].sum():,.0f}")
c2.metric("Critical Triggers", len(df[df['Risk_Score'] >= 70]))
c3.metric("System Health", "Llama3 Active")

# --- The Queue ---
st.subheader("⚠️ Priority Intervention Queue")
high_risk = df[df['Risk_Score'] >= 70].sort_values(by='Risk_Score', ascending=False)
st.dataframe(high_risk, use_container_width=True, hide_index=True)

# --- The "Let Her Rip" Button ---
if st.button("🤖 Run Machine Intelligence Analysis"):
    st.divider()
    for _, row in high_risk.iterrows():
        best_time, prob, logic = get_strategic_trigger(row)
        
        with st.expander(f"Strategy: Account {row['Acct_ID']} ({row['Sector']})", expanded=True):
            left, right = st.columns([1, 2])
            
            with left:
                st.write("### 🕒 BTC Trigger")
                st.success(f"**Target: {best_time}**")
                st.progress(prob/100, text=f"Success Probability: {prob}%")
                st.caption(f"**Feature Signal:** {logic}")
            
            with right:
                st.write("### 📱 A/B Tested Payload")
                prompt = (f"Draft a 140-char SMS for a {row['Sector']} worker "
                         f"who is {row['Pay_Drift']} days late. Focus on 'Credit Protection' "
                         f"and offer a 'Help' button. Tone: Professional Partner.")
                
                with st.spinner("Analyzing..."):
                    msg = llm.invoke(prompt)
                    st.info(msg)
                    st.button("🚀 Push to Channel", key=f"p_{row['Acct_ID']}")