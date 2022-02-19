import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
Evolution strategy mutates and combines the best individuals of a population across a number of generations without transforming them into an array of bits (like genetic algorithms) but uses the real values of the positions."""

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
- If the search space is very complex and large
- If you have enough time for many model evaluations
"""


implementation_ = """
"""


def evolution_strategy_app():
    st.title("Evolution Strategy")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/evolution_strategy_0.gif"))
    col3.image(os.path.join(here_, "_images/evolution_strategy_1.gif"))
    col2.image(os.path.join(here_, "_images/evolution_strategy_2.gif"))
    col3.image(os.path.join(here_, "_images/evolution_strategy_3.gif"))

    col1.subheader("About the implementation")
    col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
