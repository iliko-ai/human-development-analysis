import streamlit as st

st.cache_resource.clear()


def render_sidebar():
    """
    Render the Streamlit sidebar navigation and manage the selected page state.

    Creates sidebar buttons for navigating between app sections and updates the
    session state with the current page selection.

    Returns:
        str: The name of the selected navigation page.
    """
    # Initialize session state
    if "nav" not in st.session_state:
        st.session_state.nav = "Home"

    # Navigation state
    if st.sidebar.button("Home", key="home_button", use_container_width=True):
        st.session_state.nav = "Home"
    if st.sidebar.button(
        "Data Exploration", key="date_explorationbutton", use_container_width=True
    ):
        st.session_state.nav = "Data Exploration"
    if st.sidebar.button(
        "Statistical Analysis", key="stats_analysis_button", use_container_width=True
    ):
        st.session_state.nav = "Stats Analysis"
    if st.sidebar.button(
        "GDP Distribution", key="sunburst_plot_button", use_container_width=True
    ):
        st.session_state.nav = "GDP Distribution"
    if st.sidebar.button(
        "Time Analysis", key="time_analysis_button", use_container_width=True
    ):
        st.session_state.nav = "Time Analysis"

    return st.session_state.nav
