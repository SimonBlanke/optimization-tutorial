import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
The repulsing hill climbing optimization algorithm improves the normal hill 
climbing by adding a way to escape local optimia. If no better position is 
found within the next `n_neighbours` positions the algorithm will increase 
`epsilon` by the `repulsion_factor` for the next iteration.
"""

para_d = {
    "Parameter": ["epsilon", "distribution", "n_neighbours", "repulsion_factor"],
    "Type": ["float", "string", "int", "float"],
    "default": ["0.03", "normal", "3", "5"],
    "typical range / possible values": [
        "0.01 ... 0.3",
        "normal, laplace, logistic, gumbel",
        "1 ... 10",
        "2 ... 7",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- Better exploration of search space than most hill climbing based algorithms
- Good for convex- and non-convex optimization problems
"""


implementation_ = """
"""


def repulsing_hill_climbing_app():
    st.title("Repulsing Hill Climbing Optimizer")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/repulsing_hill_climbing_0.gif"))
    col3.image(os.path.join(here_, "_images/repulsing_hill_climbing_1.gif"))
    col2.image(os.path.join(here_, "_images/repulsing_hill_climbing_2.gif"))
    col3.image(os.path.join(here_, "_images/repulsing_hill_climbing_3.gif"))

    # col1.subheader("About the implementation")
    # col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
