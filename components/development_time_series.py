import pandas as pd
import plotly.express as px
import streamlit as st

from constants.constants import CONTINENT_COLOR_MAP
from utils.continent_utils import create_continent_time_series_df


def render_development_time_series(df: pd.DataFrame):
    """
    Render interactive time series charts for GDP, HDI, and CO₂ consumption by
    continent.

    Displays three Plotly line charts in Streamlit showing the development of GDP per
    capita, HDI index, and CO₂ consumption across continents over time. Highlights key
    trends such as the 2008 financial crisis impact on CO₂ consumption.

    Args:
        df (pd.DataFrame): DataFrame containing yearly development indicators with at
        least the following columns: 'year', 'continent', 'gdp', 'hdi_index', and
        'co2_consump'.

    Returns:
        None: The function directly renders charts in the Streamlit app.
    """
    st.subheader(
        f"Development Time Series from {df['year'].min()} to {df['year'].max()} by "
        f"continent."
    )
    st.caption(
        "**Note: Time series charts are not filtered by year, so the data is displayed "
        "for all years.**"
    )

    st.info(
        "🔍 **Key Insight**: The development of life expectancy, GDP, and HDI has been "
        "relatively consistent across continents, with most regions showing a gradual "
        " increase over the years. After the 2008 financial crisis, there was a "
        "significant decrease in CO2 consumption for most continents except for South "
        "American and African countries."
    )

    melted_df = create_continent_time_series_df(df, "gdp")

    # Create line chart using Plotly
    fig = px.line(
        melted_df,
        x="year",
        y="gdp",
        color="continent",
        title=f"GDP Development Time Series ({df['year'].min()}-{df['year'].max()})",
        color_discrete_map=CONTINENT_COLOR_MAP,
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="black",
        title_font_color="black",
        xaxis=dict(
            tickfont=dict(color="black"),
            title=dict(text="Year", font=dict(color="black")),
        ),
        yaxis=dict(
            tickfont=dict(color="black"),
            title=dict(text="GDP per Capita", font=dict(color="black")),
            gridcolor="lightgray",
        ),
        legend=dict(
            title_text="Continent", font_color="black", title_font_color="black"
        ),
    )

    st.plotly_chart(fig, use_container_width=True)

    hdi_melted_df = create_continent_time_series_df(df, "hdi_index")
    fig = px.line(
        hdi_melted_df,
        x="year",
        y="hdi_index",
        color="continent",
        title=f"HDI Development Time Series ({df['year'].min()}-{df['year'].max()})",
        color_discrete_map=CONTINENT_COLOR_MAP,
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="black",
        title_font_color="black",
        xaxis=dict(
            tickfont=dict(color="black"),
            title=dict(text="Year", font=dict(color="black")),
        ),
        yaxis=dict(
            tickfont=dict(color="black"),
            title=dict(text="HDI Index", font=dict(color="black")),
        ),
        legend=dict(
            title_text="Continent", font_color="black", title_font_color="black"
        ),
    )
    st.plotly_chart(fig, use_container_width=True)

    co2_melted_df = create_continent_time_series_df(df, "co2_consump")
    fig = px.line(
        co2_melted_df,
        x="year",
        y="co2_consump",
        color="continent",
        title=f"CO2 Consumption Development Time Series ("
        f"{df['year'].min()}-{df['year'].max()})",
        color_discrete_map=CONTINENT_COLOR_MAP,
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="black",
        title_font_color="black",
        xaxis=dict(
            tickfont=dict(color="black"),
            title=dict(text="Year", font=dict(color="black")),
        ),
        yaxis=dict(
            tickfont=dict(color="black"),
            title=dict(text="CO2 Consumption", font=dict(color="black")),
        ),
        legend=dict(
            title_text="Continent", font_color="black", title_font_color="black"
        ),
    )

    # Add vertical line at year 2008
    fig.add_vline(
        x=2008,
        line_dash="dash",
        line_color="red",
        annotation_text="2008 Financial Crisis",
        annotation_position="top",
    )
    st.plotly_chart(fig, use_container_width=True)
