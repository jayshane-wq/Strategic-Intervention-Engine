import streamlit as st
import pandas as pd
from langchain_community.llms import Ollama
import datetime

# --- Performance: LLM Initialization with Connection Shield ---
def get_llm():
    try:
        # Attempts to connect to local Ollama instance
        return Ollama(model="llama3", timeout=2)
    except:
        return None

llm = get_llm()

# --- Page Config & Styling ---
st.set_page_config(page_title="S.I.E. | Strategic Ops", layout="wide")

# --- Decision Intelligence: The BTC Propensity Model ---
def get_strategic_trigger(row):
    """
    Identifies the 'Golden Window' based on:
    1. Historical Engagement | 2. Sector Persona | 3. Risk Intensity
    """
    history = str(row.get('Last_Success_Time', 'None'))
    sector = row['Sector']
    drift = row['Pay_Drift']
    
    # Logic 1: Historical Evidence (Primary Signal)
    if history != 'None' and history != 'nan':
        return history, 98, "Verified Historical Engagement Window"

    # Logic 2: Sector Persona Heuristics
    sector_intelligence = {
        'Tech': ("7:45 PM", 85, "Post-Focus/Evening Receptivity"),
        'Healthcare': ("8:15 AM", 78, "Shift-change transition window"),
        'Civil Servant': ("5:15 PM", 92, "Standard end-of-day commute"),
        'Self-Employed': ("9:00 AM", 65, "Pre-client-meeting prep time")
    }
    
    time, score, reason = sector_intelligence.get(sector, ("12:30 PM", 50, "General Population Baseline"))
    
    # Logic 3: Drift Penalty (Urgency Adjustment)
    if drift > 15:
        score -= 10
        reason += " | Urgency Escalated: Strategic morning intervention recommended."
        
    return time, score, reason

# --- Sidebar: Feature Controls ---
st.sidebar.title("⚙️ Operations Control")
st.sidebar.info("Strategic Intervention Engine (S.I.E.) v1.0")
demo_mode = st.sidebar.checkbox("🚀 Enable Feature Demo Mode", value=True)

if demo_mode:
    # Portfolio Data Structure for Demoing Capabilities
    data = {
        'Acct_ID': [1001, 1002, 1003, 1004, 1005],
        'Sector': ['Tech', 'Healthcare', 'Self-Employed', 'Civil Servant', 'Tech'],
        'Pay_Drift': [8, 0, 15, 3, 25],
        'ACH_Active': ['No', 'Yes', 'No', 'Yes', 'No'],
        'Last_Success_Time': ['19:45', 'None', '09:15', 'None', '20:30'],
        'Balance': [12500, 8500, 45000, 1200, 32000]
    }
    df = pd.DataFrame(data)
    st.sidebar.success("Demo Logic Loaded Successfully")
else:
    uploaded = st.sidebar.file_uploader("Upload Portfolio CSV", type="csv")
    if uploaded: 
        df = pd.read_csv(uploaded)
    else: 
        st.info("Please upload a CSV or toggle Demo Mode to continue.")
        st.stop()

# --- Risk Scoring Analysis ---
# Calculating 'Hiccup Propensity' based on operational flags
df['Risk_Score'] = df.apply(lambda r: (40 if r['Sector'] in ['Tech', 'Self-Employed'] else 10) + 
                                     (30 if r['Pay_Drift'] > 5 else 0) + 
                                     (30 if r['ACH_Active'] == 'No' else 0), axis=1)

# --- Dashboard Header ---
st.title("🛡️ Strategic Intervention Engine")
st.markdown("### *Predictive Propensity & Recovery Automation*")

c1, c2, c3 = st.columns(3)
with c1: st.metric("Portfolio Exposure", f"${df['Balance'].sum():,.0f}")
with c2: st.metric("Critical Queue", len(df[df['Risk_Score'] >= 70]))
with c3: st.metric("System Logic", "Llama3 Propensity-v1")

# --- Intervention Queue ---
st.subheader("⚠️ Priority Intervention Queue")
high_risk = df[df['Risk_Score'] >= 70].sort_values(by='Risk_Score', ascending=False)
st.dataframe(high_risk, use_container_width=True, hide_index=True)

# --- The Strategic Trigger Engine ---
if st.button("🤖 Analyze & Generate Triggers"):
    st.divider()
    for _, row in high_risk.iterrows():
        best_time, prob, logic = get_strategic_trigger(row)
        
        with st.expander(f"Acct {row['Acct_ID']} | {row['Sector']} Strategy", expanded=True):
            left, right = st.columns([1, 2])
            
            with left:
                st.write("### 🕒 BTC Intel")
                st.success(f"**Best Window: {best_time}**")
                st.progress(prob/100, text=f"Success Propensity: {prob}%")
                st.caption(f"**Rationale:** {logic}")
            
            with right:
                st.write("### 📱 Outreach Payload")
                
                # Check for active LLM connection (Local Only)
                if llm and not demo_mode:
                    try:
                        prompt = (f"Draft a 140-char SMS for a {row['Sector']} worker "
                                 f"who is {row['Pay_Drift']} days late. Focus on 'Credit Protection'.")
                        with st.spinner("Generating AI Payload..."):
                            msg = llm.invoke(prompt)
                            st.info(msg)
                    except:
                        st.warning("AI Engine Offline (Connection Timeout)")
                        st.info(f"FALLBACK TEMPLATE: Hi! We noticed a timing shift in your payment. We’d like to help you avoid a credit 'hiccup.' Reply HELP to chat with a partner.")
                else:
                    # Professional Placeholder for the Public Demo link
                    st.caption("✨ *Strategic Template (AI Generation requires local Ollama)*")
                    st.info(f"STRATEGIC TEMPLATE: Hi! We noticed a shift in your {row['Sector']} payment timing. We're here to help protect your account status. Reply HELP to discuss options.")
                
                st.button("✅ Queue for Dispatch", key=f"q_{row['Acct_ID']}")

# --- Footer ---
st.divider()
st.caption("Developed by Jason Shane, PMP | Senior Operations & PMO Leadership")
