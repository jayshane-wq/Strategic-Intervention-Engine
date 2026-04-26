import streamlit as st
import pandas as pd
from langchain_community.llms import Ollama

# --- Direct Ollama Integration ---
def get_llm():
    try:
        # Direct connection for local Llama3
        return Ollama(model="llama3")
    except:
        return None

llm = get_llm()

st.set_page_config(page_title="S.I.E. | Local Intelligence Engine", layout="wide")

# --- BTC Logic ---
def get_strategic_trigger(row):
    history = str(row.get('Last_Success_Time', 'None'))
    sector = row['Sector']
    drift = row['Pay_Drift']
    
    if history != 'None' and history != 'nan':
        return history, 98, "Verified Historical Engagement"

    sector_intelligence = {
        'Tech': ("7:45 PM", 85, "Evening Receptivity"),
        'Healthcare': ("8:15 AM", 78, "Shift-change transition"),
        'Civil Servant': ("5:15 PM", 92, "Standard end-of-day"),
        'Self-Employed': ("9:00 AM", 65, "Pre-client-meeting")
    }
    
    time, score, reason = sector_intelligence.get(sector, ("12:30 PM", 50, "Baseline"))
    if drift > 15:
        score -= 10
        reason += " | Urgency Escalated."
        
    return time, score, reason

# --- UI & Upload ---
st.title("🛡️ Strategic Intervention Engine")
st.subheader("Local Execution Mode (Ollama Enabled)")

uploaded_file = st.sidebar.file_uploader("Upload Portfolio CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Risk Calculation
    df['Risk_Score'] = df.apply(lambda r: (40 if r['Sector'] in ['Tech', 'Self-Employed'] else 10) + 
                                         (30 if r['Pay_Drift'] > 5 else 0) + 
                                         (30 if r['ACH_Active'] == 'No' else 0), axis=1)

    st.metric("Total Accounts", len(df))
    
    high_risk = df[df['Risk_Score'] >= 70].sort_values(by='Risk_Score', ascending=False)
    st.dataframe(high_risk, use_container_width=True)

    if st.button("🤖 Run AI Analysis"):
        for _, row in high_risk.iterrows():
            best_time, prob, logic = get_strategic_trigger(row)
            with st.expander(f"Strategy: Acct {row['Acct_ID']}"):
                c1, c2 = st.columns([1, 2])
                with c1:
                    st.success(f"BTC Window: {best_time}")
                    st.caption(logic)
                with c2:
                    if llm:
                        prompt = f"Draft an empathetic 140-char SMS for a {row['Sector']} worker late on payment. Focus on credit health."
                        msg = llm.invoke(prompt)
                        st.info(msg)
                    else:
                        st.error("Ollama connection not found. Ensure 'ollama serve' is active.")
else:
    st.info("👈 Upload a CSV file in the sidebar to begin local analysis.")