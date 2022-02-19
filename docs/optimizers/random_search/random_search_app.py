import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
The random search explores by choosing a new position at random after each iteration. 
Some random search implementations choose a new position within a large hypersphere around 
the current position. The implementation in hyperactive is purely random across the 
search space in each step."""


properties_ = """
- Does not adapt its behaviour to the optimization problem.
- Very good as a first method of optimization or to start exploring the search space
- For a short optimization run to get an acceptable solution
"""


implementation_ = """
"""


def random_search_app():
    st.title("Random Search")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/random_search_0.gif"))
    col3.image(os.path.join(here_, "_images/random_search_1.gif"))
    col2.image(os.path.join(here_, "_images/random_search_2.gif"))
    col3.image(os.path.join(here_, "_images/random_search_3.gif"))

    # col1.subheader("About the implementation")
    # col1.markdown(implementation_)

    # col1.subheader("Available parameters")
    # col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
