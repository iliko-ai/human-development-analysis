import pandas as pd
import plotly.express as px
import streamlit as st

from constants.constants import CONTINENT_COLOR_MAP


def render_gdp_distribution_plot(df: pd.DataFrame, year: int):
    """
    Render a sunburst chart showing global GDP distribution by continent and country.

    Displays the share of each country's GDP within its continent and highlights the
    highest-GDP country in every continent for the selected year.

    Args:
        df (pd.DataFrame): DataFrame containing GDP data with columns such as
            'year', 'continent', 'country', and 'gdp'.
        year (int): The selected year for which GDP distribution is visualized.

    Returns:
        None: The function directly renders the chart and summary in the Streamlit app.
    """
    st.subheader(f"Global GDP Distribution by Region and Country for the year {year}")
    selected_year_df = df[df["year"] == year]

    # Get highest GDP country for each continent
    highest_gdp_by_continent = selected_year_df.loc[
        selected_year_df.groupby("continent", observed=True)["gdp"].idxmax()
    ]

    # Create info text with highest GDP countries
    info_text = "🏆 **Highest GDP by Continent**: "
    continent_info = []
    for _, row in highest_gdp_by_continent.iterrows():
        continent_info.append(
            f"{row['continent']}: {row['country']} (${row['gdp']:,.0f})"
        )

    info_text += "\n".join(continent_info)

    st.info(info_text)

    # Calculate percentage of country GDP within each continent
    continent_totals = selected_year_df.groupby("continent", observed=True)["gdp"].sum()
    selected_year_df = selected_year_df.copy()
    selected_year_df["continent_percentage"] = selected_year_df.apply(
        lambda row: (row["gdp"] / continent_totals[row["continent"]]) * 100, axis=1
    )

    # Create sunburst plot with custom hover data
    fig = px.sunburst(
        selected_year_df,
        path=["continent", "country"],
        values="gdp",
        title=f"GDP Distribution by Continent and Country ({year})",
        custom_data=["continent_percentage"],
        color="continent",
        color_discrete_map=CONTINENT_COLOR_MAP,
    )

    # Update hover template to show percentage
    fig.update_traces(
        hovertemplate="<b>%{label}</b><br>"
        + "GDP: %{value:,.0f}<br>"
        + "Continent Share: %{customdata[0]:.1f}%<br>"
        + "<extra></extra>"
    )

    # Update layout for consistent styling and size
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="black",
        title_font_color="black",
        width=1400,  # Set specific width
        height=800,  # Set specific height
    )

    # Create columns to center the plot at 80% width
    col1, col2, col3 = st.columns([0.5, 14, 0.5])
    with col2:
        st.plotly_chart(fig, use_container_width=True)
