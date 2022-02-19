import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
Random restart hill climbing works by starting a hill climbing search and jumping to a random 
new position after `n_iter_restart` iterations."""

para_d = {
    "Parameter": ["epsilon", "distribution", "n_neighbours", "n_iter_restart"],
    "Type": ["float", "string", "int", "int"],
    "default": ["0.03", "normal", "3", "10"],
    "typical range / possible values": [
        "0.01 ... 0.3",
        "normal, laplace, logistic, gumbel",
        "1 ... 10",
        "5 ... 20",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- Good for convex and nonconvex optimization problems
- Similar to random search for low values of `n_iter_restart`
"""


implementation_ = """
"""


def random_restart_hill_climbing_app():
    st.title("Random Restart Hill Climbing Optimizer")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/random_restart_hill_climbing_0.gif"))
    col3.image(os.path.join(here_, "_images/random_restart_hill_climbing_1.gif"))
    col2.image(os.path.join(here_, "_images/random_restart_hill_climbing_2.gif"))
    col3.image(os.path.join(here_, "_images/random_restart_hill_climbing_3.gif"))

    # col1.subheader("About the implementation")
    # col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
