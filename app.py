import streamlit as st
import pandas as pd

st.title("🩺 Doctor Demand Optimizer for Expiry Stock")

medicine = st.selectbox("Select Near-Expiry Medicine", ["Metformin 500mg", "Amlodipine 5mg", "Atorvastatin 10mg"])

# Simulated logic from your 500-row data
if st.button("Find Demand"):
    st.subheader(f"Top Doctors for {medicine} in Pune")
    st.table(pd.DataFrame({
        "Doctor": ["Dr. Sharma (Kothrud)", "Dr. Patil (Aundh)", "Dr. Joshi (Hadapsar)"],
        "Monthly Prescriptions": [45, 32, 28],
        "Potential Recovery": ["₹12,400", "₹8,900", "₹7,600"]
    }))
    
    st.warning(f"💡 Suggestion: Transfer 30 units from Pune to Nashik — Demand 3.4x higher there. Save ₹15,000")
    
    st.success("Action Plan: Share this report with MR Amit S — He covers these 3 doctors")
