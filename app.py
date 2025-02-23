import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# --- USER AUTHENTICATION ---
# Store user credentials (For production, use a database)
user_config = {
    "credentials": {
        "usernames": {
            "admin": {"email": "admin@edutech.com", "name": "Admin User", "password": stauth.Hasher(["admin123"]).generate()[0]},
            "user1": {"email": "user1@example.com", "name": "User One", "password": stauth.Hasher(["password123"]).generate()[0]},
        }
    },
    "cookie": {"expiry_days": 30, "key": "secret_key", "name": "app_auth"},
    "preauthorized": ["admin@edutech.com"]
}

# Load user credentials
authenticator = stauth.Authenticate(
    user_config["credentials"], user_config["cookie"]["name"], user_config["cookie"]["key"], user_config["cookie"]["expiry_days"]
)

# Login widget
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.success(f"Welcome, {name}!")

    # --- Your Investment App Logic ---
    st.title("Investment Decision Framework")

    # Input fields
    investment = st.number_input("Investment Amount ($)", min_value=0, value=100000)
    breakeven = st.number_input("Breakeven Period (Months)", min_value=1, value=6)
    roi_percentage = st.number_input("Expected ROI (%)", min_value=0, max_value=100, value=25)
    risk = st.selectbox("Risk Level", ["Low", "Medium", "High"])

    # Perform calculations
    def calculate_roi(investment, roi_percentage):
        return investment * (roi_percentage / 100)

    def evaluate_decision(investment, breakeven, roi_percentage, risk):
        if roi_percentage > 20 and breakeven <= 6 and risk != "High":
            return "APPROVED"
        elif roi_percentage >= 10 and risk == "Low":
            return "REJECTED"
        else:
            return "CONSIDER IF DATA SUPPORTS"

    roi_in_dollars = calculate_roi(investment, roi_percentage)
    decision = evaluate_decision(investment, breakeven, roi_percentage, risk)

    # Display results
    st.subheader("Investment Analysis")
    st.write(f"**ROI in Dollars:** ${roi_in_dollars:,.2f}")
    st.write(f"**Investment Decision:** {decision}")

    # Logout button
    authenticator.logout("Logout", "sidebar")

elif authentication_status is False:
    st.error("Incorrect username or password")

elif authentication_status is None:
    st.warning("Please enter your credentials to log in.")
