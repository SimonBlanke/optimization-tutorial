import os
import sys

import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))

para_path_ = os.path.join(here_, "..")
sys.path.append(para_path_)

from parameters_info import n_neighbours_intro_


def n_neighbours_app():
    st.title("n_neighbours")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3, col4 = st.columns((1, 1, 1, 1))

    col1.write("")
    col1.write(n_neighbours_intro_)

    col2.image(os.path.join(here_, "_images/hill_climbing_n_neighbours_0.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_n_neighbours_1.gif"))
    col4.image(os.path.join(here_, "_images/hill_climbing_n_neighbours_2.gif"))

    col2.image(os.path.join(here_, "_images/hill_climbing_n_neighbours_10.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_n_neighbours_11.gif"))
    col4.image(os.path.join(here_, "_images/hill_climbing_n_neighbours_12.gif"))
