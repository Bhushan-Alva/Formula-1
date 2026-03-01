import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

path = r"C:\Users\bhush\OneDrive\Desktop\DSMP\Formula 1\Overall"

# circuits = pd.read_csv(os.path.join(path, "circuits.csv"))
# constructor_results = pd.read_csv(os.path.join(path, "constructor_results.csv"))
# constructor_standings = pd.read_csv(os.path.join(path, "constructor_standings.csv"))
# constructors = pd.read_csv(os.path.join(path, "constructors.csv"))
# driver_standings = pd.read_csv(os.path.join(path, "driver_standings.csv"))
# drivers = pd.read_csv(os.path.join(path, "drivers.csv"))
# lap_times = pd.read_csv(os.path.join(path, "lap_times.csv"))
# pit_stops = pd.read_csv(os.path.join(path, "pit_stops.csv"))
# qualifying = pd.read_csv(os.path.join(path, "qualifying.csv"))
# races = pd.read_csv(os.path.join(path, "races.csv"))
results = pd.read_csv(os.path.join(path, "results.csv"))
seasons = pd.read_csv(os.path.join(path, "seasons.csv"))
# sprint_results = pd.read_csv(os.path.join(path, "sprint_results.csv"))
# status = pd.read_csv(os.path.join(path, "status.csv"))

# seasons = []

def points_table(season):
    pass



def show():
    st.title("📈 Season Analysis")

    st.write("Championship battles and seasonal trends.")
    st.selectbox(label="Select the season", options=seasons["year"].sort_values(ascending=False))