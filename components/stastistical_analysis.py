import pandas as pd
import plotly.express as px
import streamlit as st

from constants.constants import CONTINENT_COLOR_MAP
from utils.continent_utils import apply_continent_order


def render_statistical_analysis(df: pd.DataFrame, year: int):
    """
    Render statistical charts analyzing GDP, life expectancy, CO₂, and HDI by continent.

    Displays box plots and bar charts comparing life expectancy, GDP, CO₂ consumption,
    and HDI across continents for a selected year, highlighting overall development "
    rends.

    Args:
        df (pd.DataFrame): DataFrame containing development indicators with columns such
        as: 'year', 'continent', 'gdp', 'life_exp', 'hdi_index', and 'co2_consump'.
        year (int): The selected year for statistical visualization.

    Returns:
        None: The function renders multiple charts directly in the Streamlit app.
    """
    st.subheader(f"Statistical Analysis for the year {year}")

    st.info(
        "🔍 **Key Insight**: There is a strong positive correlation between average "
        "life expectancy and average CO2 consumption across continents, with most "
        "regions following a similar ranking pattern."
    )

    selected_year_df = df[df["year"] == year]

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        # Ensure consistent continent order for box plot
        life_exp_data = apply_continent_order(selected_year_df)

        fig = px.box(
            life_exp_data,
            x="continent",
            y="life_exp",
            color="continent",
            title=f"Life Expectancy by Continent ({year})",
            color_discrete_map=CONTINENT_COLOR_MAP,
        )
        fig.update_layout(
            showlegend=False,
            plot_bgcolor="white",
            paper_bgcolor="white",
            title=dict(
                text=f"Life Expectancy by Continent ({year})",
                font=dict(color="black"),
                font_size=15,
            ),
            xaxis=dict(
                tickfont=dict(color="black"),
                title=None,
                tickangle=45,
            ),
            yaxis=dict(
                tickfont=dict(color="black"),
                gridcolor="lightgray",
                title=dict(text="Life Expectancy", font=dict(color="black")),
            ),
            margin=dict(l=0, r=0, t=40, b=0),
        )
        st.plotly_chart(fig)

    with col2:
        # CO2 Consumption bar chart by continent
        co2_data = selected_year_df.dropna(subset=["co2_consump"])
        continent_co2 = (
            co2_data.groupby("continent", observed=True)["co2_consump"]
            .mean()
            .reset_index()
        )

        # Use consistent continent order from constants
        continent_co2 = apply_continent_order(continent_co2)

        title_text = f"Average CO2 Consumption by Continent ({year})"

        fig = px.bar(
            continent_co2,
            x="continent",
            y="co2_consump",
            color="continent",
            title=title_text,
            color_discrete_map=CONTINENT_COLOR_MAP,
        )
        fig.update_layout(
            showlegend=False,
            plot_bgcolor="white",
            paper_bgcolor="white",
            title=dict(text=title_text, font=dict(color="black"), font_size=15),
            xaxis=dict(
                tickfont=dict(color="black"),
                title=None,
                tickangle=45,
                zeroline=False,
                showline=False,
            ),
            yaxis=dict(
                tickfont=dict(color="black"),
                gridcolor="lightgray",
                title=dict(
                    text="CO2 Consumption (per capita)", font=dict(color="black")
                ),
                zeroline=False,
                showline=False,
            ),
            margin=dict(l=0, r=0, t=40, b=0),
        )
        st.plotly_chart(fig)

    # Second box plot
    col3, col4 = st.columns(2, gap="medium")

    with col3:
        # Ensure consistent continent order for GDP box plot
        gdp_data = apply_continent_order(selected_year_df)

        fig = px.box(
            gdp_data,
            x="continent",
            y="gdp",
            color="continent",
            title=f"GDP by Continent ({year})",
            color_discrete_map=CONTINENT_COLOR_MAP,
        )
        fig.update_layout(
            showlegend=False,
            plot_bgcolor="white",
            paper_bgcolor="white",
            title=dict(
                text=f"GDP by Continent ({year})",
                font=dict(color="black"),
                font_size=15,
            ),
            xaxis=dict(
                tickfont=dict(color="black"),
                title=None,
                zeroline=False,
                showline=False,
                tickangle=45,
            ),
            yaxis=dict(
                tickfont=dict(color="black"),
                gridcolor="lightgray",
                title=dict(text="GDP", font=dict(color="black")),
                zeroline=False,
                showline=False,
            ),
            margin=dict(l=0, r=0, t=40, b=0),
        )
        st.plotly_chart(fig)

    with col4:
        hdi_data = selected_year_df.dropna(subset=["hdi_index"])
        continent_hdi = (
            hdi_data.groupby("continent", observed=True)["hdi_index"]
            .mean()
            .reset_index()
        )

        # Use consistent continent order from constants
        continent_hdi = apply_continent_order(continent_hdi)

        fig = px.bar(
            continent_hdi,
            x="continent",
            y="hdi_index",
            color="continent",
            title=f"Average HDI Index by Continent ({year})",
            color_discrete_map=CONTINENT_COLOR_MAP,
        )

        fig.update_layout(
            showlegend=False,
            plot_bgcolor="white",
            paper_bgcolor="white",
            title=dict(
                text=f"Average HDI Index by Continent ({year})",
                font=dict(color="black"),
                font_size=15,
            ),
            xaxis=dict(
                tickfont=dict(color="black"),
                title=None,
                tickangle=45,
                zeroline=False,
                showline=False,
            ),
            yaxis=dict(
                tickfont=dict(color="black"),
                gridcolor="lightgray",
                title=dict(text="HDI Index", font=dict(color="black")),
                zeroline=False,
                showline=False,
            ),
        )
        st.plotly_chart(fig)
