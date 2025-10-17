# app.py

import streamlit as st
import pandas as pd
import os

# --- Configuration ---
# Set the page to use a wide layout for a more professional dashboard look
st.set_page_config(layout="wide") 

# Define the file path for the CLEANED data (output of Week 1)
CLEANED_DATA_PATH = os.path.join("data", "cleaned_sales_data.csv")

# --- Application Title and Introduction ---
st.title("📊 Week 1: Data Preprocessing & Initial Metrics")
st.markdown(
    "**Objective:** Displaying the results of data collection, cleaning, and initial calculated fields, "
    "setting the foundation for deeper EDA in Week 2."
)
st.markdown("---")


def display_week1_summary():
    """Loads cleaned data and displays the required KPIs and verification table."""
    
    try:
        # Load the data processed by data_prep.py
        df = pd.read_csv(CLEANED_DATA_PATH)
        
        # --- 1. Display Key Performance Indicators (KPIs) ---
        st.subheader("Key Business Metrics from Cleaned Data")
        
        # Calculate the required metrics
        total_revenue = df['Sales'].sum()
        total_profit = df['Profit'].sum()
        
        # Calculate overall Profit Margin Percentage, safely checking for zero division
        if total_revenue != 0:
            profit_margin_pct = (total_profit / total_revenue) * 100
        else:
            profit_margin_pct = 0.0
        
        # Use Streamlit columns to present metrics in a clean, dashboard style
        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
        col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
        col3.metric("🎯 Average Profit Margin", f"{profit_margin_pct:.2f}%")
        
        st.markdown("---")
        
        # --- 2. Display Verification Table (Proof of Week 1 Tasks) ---
        st.subheader("Data Verification: Successful Preprocessing")
        st.caption(
            "The table below verifies that dates are formatted as datetime objects and "
            "the **Profit Margin (%)** field has been successfully calculated."
        )
        
        # Display relevant columns to prove the cleaning and calculation tasks were done
        display_cols = ['Row ID', 'Order Date', 'Ship Date', 'Sales', 'Profit', 'Profit Margin (%)']
        st.dataframe(df[display_cols].head(10), use_container_width=True)
        
        st.success("Week 1 Data Preprocessing Complete. Ready for Week 2 EDA.")

    except FileNotFoundError:
        st.error(
            f"❌ **Data Load Error:** The required file **{CLEANED_DATA_PATH}** was not found. "
            "Please ensure you run **`python src/data_prep.py`** in your terminal first to generate the cleaned dataset."
        )
    except Exception as e:
        st.error(f"An unexpected error occurred while processing data: {e}")

if __name__ == "__main__":
    display_week1_summary()