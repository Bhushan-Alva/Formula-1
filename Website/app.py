import streamlit as st

# Import page modules
from webpages import home, results, drivers, constructors, circuits, seasons

st.set_page_config(
    page_title="F1 Analytics",
    page_icon="🏎️",
    layout="wide"
)

# ===== Sidebar =====
st.sidebar.title("🏎️ F1 Analytics")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🥇 Results Analysis",
        "👤 Drivers",
        "🏎️ Constructors",
        "🏟️ Circuits",
        "📈 Seasons",
    ]
)

# ===== Page Routing =====
if page == "🏠 Home":
    home.show()

elif page == "🥇 Results Analysis":
    results.show()

elif page == "👤 Drivers":
    drivers.show()

elif page == "🏎️ Constructors":
    constructors.show()

elif page == "🏟️ Circuits":
    circuits.show()

elif page == "📈 Seasons":
    seasons.show()
