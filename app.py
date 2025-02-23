import streamlit as st  # ✅ Fixed this line
import pandas as pd

def calculate_roi(investment, roi_percentage):
    return investment * (roi_percentage / 100)

def evaluate_decision(investment, breakeven, roi_percentage, risk):
    if roi_percentage > 20 and breakeven <= 6 and risk != "High":
        return "APPROVED"
    elif roi_percentage >= 10 and risk == "Low":
        return "REJECTED"
    else:
        return "CONSIDER IF DATA SUPPORTS"

def analyze_breakeven(breakeven):
    if breakeven <= 6:
        return "FAST BREAKEVEN"
    elif breakeven <= 12:
        return "MODERATE"
    else:
        return "RISKY"

st.title("Investment Decision Framework")

# Input fields
investment = st.number_input("Investment Amount ($)", min_value=0, value=100000)
breakeven = st.number_input("Breakeven Period (Months)", min_value=1, value=6)
roi_percentage = st.number_input("Expected ROI (%)", min_value=0, max_value=100, value=25)
risk = st.selectbox("Risk Level", ["Low", "Medium", "High"])

# Perform calculations
roi_in_dol
