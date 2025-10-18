import pandas as pd

from constants.constants import CONTINENT_ORDER


def apply_continent_order(df, continent_column="continent"):
    """
    Apply consistent continent ordering to a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing continent data
        continent_column (str): Name of the continent column (default: 'continent')

    Returns:
        pd.DataFrame: DataFrame with continent column ordered according to
        CONTINENT_ORDER
    """
    df_copy = df.copy()
    df_copy[continent_column] = pd.Categorical(
        df_copy[continent_column], categories=CONTINENT_ORDER, ordered=True
    )
    return df_copy.sort_values(continent_column)


def create_continent_time_series_df(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Create a continent-level time series DataFrame for a given metric.

    Aggregates the specified column by year and continent, reorders continents
    consistently, and reshapes the data into a long format suitable for Plotly
    time series visualizations.

    Args:
        df (pd.DataFrame): Input DataFrame containing at least 'year', 'continent',
            and the specified metric column.
        col (str): The column name representing the metric to aggregate (e.g., 'gdp').

    Returns:
        pd.DataFrame: Melted DataFrame with columns 'year', 'continent', and the
            aggregated metric, ordered by predefined continent order.
    """
    # Group data by year and continent for time series
    grouped_df = (
        df.groupby(["year", "continent"], observed=True)[col].mean().reset_index()
    )
    grouped_df = apply_continent_order(grouped_df)

    # Pivot to have continents as columns, ensuring correct order
    pivot_df = grouped_df.pivot(index="year", columns="continent", values=col)

    # Reorder columns according to CONTINENT_ORDER
    available_continents = [col for col in CONTINENT_ORDER if col in pivot_df.columns]
    pivot_df = pivot_df[available_continents]

    # Reset index to make year a column for Plotly
    pivot_df_reset = pivot_df.reset_index()

    # Melt the data to have continent as a column instead of separate columns
    melted_df = pivot_df_reset.melt(
        id_vars=["year"],
        value_vars=available_continents,
        var_name="continent",
        value_name=col,
    )

    return melted_df
