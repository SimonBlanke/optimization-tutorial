import streamlit as st


def optimizer_app(app_d):
    st.sidebar.write("")
    radio_select = st.sidebar.radio("Algorithm details:", options=list(app_d.keys()))

    _app_, args_d = app_d[radio_select]
    _app_(args_d)
