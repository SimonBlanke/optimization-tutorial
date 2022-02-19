import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
Particle swarm optimization works by initializing a number of positions at the same time and moving all of those closer to the best one after each iteration."""

para_d = {
    "Parameter": ["epsilon", "distribution", "n_neighbours"],
    "Type": ["float", "string", "int"],
    "default": ["0.03", "normal", "3"],
    "typical range / possible values": [
        "0.01 ... 0.3",
        "normal, laplace, logistic, gumbel",
        "1 ... 10",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- If the search space is complex and large
- If you have enough time for many model evaluations
"""


implementation_ = """
"""


def particle_swarm_optimization_app():
    st.title("Particle Swarm Optimization")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/particle_swarm_optimization_0.gif"))
    col3.image(os.path.join(here_, "_images/particle_swarm_optimization_1.gif"))
    col2.image(os.path.join(here_, "_images/particle_swarm_optimization_2.gif"))
    col3.image(os.path.join(here_, "_images/particle_swarm_optimization_3.gif"))

    col1.subheader("About the implementation")
    col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
