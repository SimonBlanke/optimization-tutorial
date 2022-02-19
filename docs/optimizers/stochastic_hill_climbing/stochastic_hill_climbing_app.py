import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
Stochastic hill climbing extends the normal hill climbing by a simple method against getting 
stuck in local optima. It has a parameter you can set, that determines the probability to 
accept worse solutions as a next position.
"""

para_d = {
    "Parameter": ["epsilon", "distribution", "n_neighbours", "p_down"],
    "Type": ["float", "string", "int", "float"],
    "default": ["0.03", "normal", "3", "0.1"],
    "typical range / possible values": [
        "0.01 ... 0.3",
        "normal, laplace, logistic, gumbel",
        "1 ... 10",
        "0.1 ... 0.9",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- Expect good results for convex optimization problems
- Better adapted for non-convex problems than normal hill climbing
- Useful to do finetuning on a good initial starting position
"""


implementation_ = """

"""


def stochastic_hill_climbing_app():
    st.title("Stochastic Hill Climbing Optimizer")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/stochastic_hill_climbing_0.gif"))
    col3.image(os.path.join(here_, "_images/stochastic_hill_climbing_1.gif"))
    col2.image(os.path.join(here_, "_images/stochastic_hill_climbing_2.gif"))
    col3.image(os.path.join(here_, "_images/stochastic_hill_climbing_3.gif"))

    # col1.subheader("About the implementation")
    # col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
