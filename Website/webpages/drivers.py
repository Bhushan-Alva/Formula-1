import streamlit as st
import pandas as pd



def show():
    st.title("👤 Drivers Analysis")

    st.write("Analyze driver performance across seasons.")

    driver = st.selectbox(
        "Select Driver",
        ["Driver A", "Driver B", "Driver C"]
    )

    st.write(f"Showing data for: {driver}")