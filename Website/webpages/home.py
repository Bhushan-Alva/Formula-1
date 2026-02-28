import streamlit as st

def show():
    st.title("🏎️ Formula 1 Analytics Dashboard")

    st.markdown("""
    Welcome to the F1 Analytics Platform.

    This app explores Formula 1 race data from 1950 to present,
    covering drivers, teams, circuits, performance, and trends.
    """)

    st.header("Key Highlights")

    col1, col2, col3 = st.columns(3)

    col1.metric("Seasons", "75+")
    col2.metric("Races", "1000+")
    col3.metric("Drivers", "800+")

    st.info("Use the sidebar to explore different aspects of Formula 1.")