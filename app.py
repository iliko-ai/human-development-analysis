import pandas as pd
import streamlit as st

from components.data_exploration import render_data_exploration
from components.development_time_series import render_development_time_series
from components.gdp_distribution import render_gdp_distribution_plot
from components.sidebar import render_sidebar
from components.stastistical_analysis import render_statistical_analysis

# Load data
df = pd.read_csv("data/gapminder_data_graphs.csv")

# Page configuration
st.set_page_config(
    page_title="Gapminder Dashboard",
    page_icon=":globe_with_meridians:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load the CSS file
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.title("Life Expectancy, GDP & Human Development Analysis")
    # Render sidebar
    render_sidebar()

    year = st.selectbox(
        label="Year",
        options=df["year"].unique(),
        index=0,  # Selects first option by default,
        label_visibility="visible",
        help="select the year to display",
    )

    # Main content based on navigation
    nav_state = st.session_state.get("nav")

    if nav_state == "Data Exploration":
        render_data_exploration(df, year)
    elif nav_state == "Stats Analysis":
        render_statistical_analysis(df, year)
    elif nav_state == "Time Analysis":
        render_development_time_series(df)
    elif nav_state == "Sunburst Plot":
        render_gdp_distribution_plot(df, year)
    else:
        render_data_exploration(df, year)
        render_statistical_analysis(df, year)
        render_gdp_distribution_plot(df, year)
        render_development_time_series(df)


if __name__ == "__main__":
    main()
