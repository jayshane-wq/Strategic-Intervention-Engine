# 🛡️ Strategic Intervention Engine (S.I.E.)
### *AI-Powered Propensity Modeling for Frictionless Asset Recovery*

## 📌 Executive Summary
The **Strategic Intervention Engine** is an operations-focused prototype designed to transform traditional, reactive collections into a proactive, data-driven "Member Support" model. By leveraging **Propensity-to-Pay (PTP)** logic and **Best-Time-to-Contact (BTC)** heuristics, the engine identifies a borrower's "Golden Window" for engagement—reducing operational friction, protecting institutional yield, and maintaining brand loyalty.

## 🚀 Key Features
* **Propensity-Driven BTC Intelligence:** Intuitively detects optimal outreach triggers based on historical engagement, industry behavior patterns (Sector Persona), and risk intensity.
* **AI-Augmented Outreach:** Integrates with **Llama3 (via Ollama)** to generate empathetic, partner-focused communication that prioritizes "Credit Protection" over traditional "Debt Collection."
* **Hiccup Prediction Logic:** Scores portfolio risk using a multi-feature decision tree, identifying high-risk "drifts" before they become charge-offs.
* **Dual-Environment Architecture:** Built to run on public cloud infrastructure (Simulation Mode) or secured local hardware (Private AI Mode) to satisfy CISO/Security requirements.

## 🛠️ Technical Stack
* **Framework:** Streamlit (Python)
* **LLM Integration:** LangChain & Ollama (Local Llama3)
* **Data Processing:** Pandas
* **Intelligence:** Heuristic-based Propensity Modeling

---

## 📂 Choose Your Adventure: Deployment Modes

### 1. ☁️ Live Cloud Demo (Quick View)
Experience the UI and core propensity logic immediately via the web.
* **Link:** [https://strategic-intervention-engine.streamlit.app/](https://strategic-intervention-engine.streamlit.app/)
* **Note:** This version runs in **Simulation Mode**. Because cloud servers do not have access to local hardware LLMs, the outreach payload uses high-conversion strategic templates instead of live AI generation.

### 2. 🏠 Local Intelligence (Full AI Mode)
To run the engine with full Llama3 generation and total data privacy:
1.  **Install Requirements:** ```bash
    pip install -r requirements.txt
    ```
2.  **Start AI Brain:** Ensure **Ollama** is running with `llama3`.
3.  **Launch Engine:**
    ```bash
    streamlit run strategic_intervention_local.py
    ```

---

## 📊 Business Logic: The "Golden Window"
The engine utilizes a custom heuristic model to determine the **Best Time to Contact (BTC)**:
* **Historical:** Leverages the user's specific past success timestamps.
* **Persona-Based:** Adjusts for industry-specific shifts (e.g., Tech workers respond better in the evening; Healthcare workers during shift-change windows).
* **Urgency-Weighted:** Accelerates outreach windows as "Pay Drift" increases to mitigate loss.

## 👤 About the Developer
**Jason Shane, PMP**
Senior Operations & Project Management Leader with 25+ years of experience in mortgage default, loss mitigation, and credit lifecycle management. Specializing in leveraging AI/RPA to drive throughput and regulatory alignment.

---
*Disclaimer: This is a professional prototype. For enterprise deployment, the local Ollama instance would be replaced by a secure, private API (e.g., AWS Bedrock or Azure OpenAI) to maintain HIPAA/Financial regulatory compliance.*
