import pandas as pd
import plotly.express as px
import streamlit as st

from constants.constants import CONTINENT_COLOR_MAP
from utils.continent_utils import apply_continent_order


def render_data_exploration(df: pd.DataFrame, year: int):
    """
    Render key development metrics and a GDP vs. life expectancy scatter plot for a
    given year.

    Displays average GDP, life expectancy, and HDI metrics, along with a Plotly
    scatter chart comparing GDP per capita and life expectancy across continents.
    Highlights insights about continents with the highest concentration of
    countries having very high HDI (≥ 0.8).

    Args:
        df (pd.DataFrame): DataFrame containing development indicators with
        columns such as 'year', 'continent', 'country', 'gdp', 'life_exp', and
        'hdi_index'.

        year (int): The selected year for exploration and visualization.

    Returns:
        None: The function renders metrics and charts directly in the
        Streamlit app.
    """
    st.subheader(f"Data Exploration for the year {year}")

    # Add a year selector
    selected_year_df = df[df["year"] == year]

    # Calculate the average GDP, life expectancy, and HDI for the selected year
    avg_gdp = round(selected_year_df["gdp"].mean(), 2)
    avg_life_exp = round(selected_year_df["life_exp"].mean(), 2)
    avg_hdi = round(selected_year_df["hdi_index"].mean(), 2)

    # Display the average GDP, life expectancy, and HDI for the selected year
    col_avg_gdp, col_avg_life_exp, col_avg_hdi = st.columns([4, 4, 4], gap="small")

    with col_avg_gdp:
        st.metric(
            label="Avg GDP",
            value=f"${avg_gdp}",
        )

    with col_avg_life_exp:
        st.metric(
            label="Avg Life Expectancy",
            value=f"{avg_life_exp}",
            help=f"Average life expectancy for the year {year}",
        )

    with col_avg_hdi:
        st.metric(
            label="Avg HDI", value=f"{avg_hdi}", help=f"Average HDI for the year {year}"
        )

    # Use consistent continent order from constants
    scatter_data = apply_continent_order(selected_year_df)

    # Calculate insight about high HDI countries by continent
    high_hdi_threshold = 0.8  # Very high human development
    high_hdi_data = scatter_data.dropna(subset=["hdi_index"])
    high_hdi_by_continent = (
        high_hdi_data[high_hdi_data["hdi_index"] >= high_hdi_threshold]
        .groupby("continent", observed=True)
        .size()
    )

    if not high_hdi_by_continent.empty:
        max_continent = high_hdi_by_continent.idxmax()
        max_count = high_hdi_by_continent.max()
        st.info(
            f"🔍 **Key Insight**: {max_continent} has the most countries with very "
            f"hight human development (HDI ≥ 0.8) with {max_count} countries, "
            f"indicating superior social and economic development."
        )

    # Create the scatter plot
    fig = px.scatter(
        data_frame=scatter_data,
        title=f"Life Expectancy by GDP per Capita for countries across continents "
        f"({year})",
        x="gdp",
        y="life_exp",
        color="continent",
        template="plotly_white",
        color_discrete_map=CONTINENT_COLOR_MAP,
        opacity=0.7,
        hover_data=["continent", "country", "hdi_index", "gdp", "life_exp"],
    )

    # Force white background and black text
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="black",
        title_font_color="black",
        xaxis=dict(
            color="black",
            gridcolor="lightgray",
            tickfont=dict(color="black"),
            title=dict(text="GDP", font=dict(color="black")),
        ),
        yaxis=dict(
            title="Life Expectancy",
            color="black",
            gridcolor="lightgray",
            tickfont=dict(color="black"),
            title_font_color="black",
        ),
        legend=dict(
            title_text="Continent", font_color="black", title_font_color="black"
        ),
    )

    # Update traces to ensure text is black and format hover data
    fig.update_traces(
        textfont_color="black",
        hovertemplate="<b>%{customdata[1]}</b><br>"
        + "Continent: %{customdata[0]}<br>"
        + "GDP: $%{x:,.0f}<br>"
        + "Life Expectancy: %{y:.1f} years<br>"
        + "HDI: %{customdata[2]:.3f}<br>"
        + "<extra></extra>",
    )

    # Add horizontal line for HDI >= 0.9
    high_hdi_countries = selected_year_df[selected_year_df["hdi_index"] >= 0.8]
    if not high_hdi_countries.empty:
        # Add vertical line at average GDP of high HDI countries
        avg_gdp_high_hdi = high_hdi_countries["gdp"].mean()
        fig.add_vline(
            x=avg_gdp_high_hdi,
            line_dash="dash",
            line_color="red",
            annotation_text=f"HDI ≥ 0.8 indicates very high human development "
            f"(Avg GDP: ${avg_gdp_high_hdi:.0f})",
            annotation_position="top",
        )

    st.plotly_chart(fig)
