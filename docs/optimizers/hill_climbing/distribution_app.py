import os
import sys

import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))

para_path_ = os.path.join(here_, "..")
sys.path.append(para_path_)

from parameters_info import distribution_intro_


def distribution_app():
    st.title("distribution")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3, col4 = st.columns((1, 1, 1, 1))

    col1.write("")
    col1.write(distribution_intro_)

    col2.image(os.path.join(here_, "_images/hill_climbing_distribution_0.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_distribution_1.gif"))
    col4.image(os.path.join(here_, "_images/hill_climbing_distribution_2.gif"))

    col2.image(os.path.join(here_, "_images/hill_climbing_distribution_10.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_distribution_11.gif"))
    col4.image(os.path.join(here_, "_images/hill_climbing_distribution_12.gif"))
