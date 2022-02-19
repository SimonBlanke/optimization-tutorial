import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
An algorithm that chooses a new position within a large hypersphere around the current position. 
This hypersphere gets smaller over time.
"""

para_d = {
    "Parameter": [
        "epsilon",
        "distribution",
        "n_neighbours",
        "annealing_rate",
        "start_temp",
    ],
    "Type": ["float", "string", "int", "float", "float"],
    "default": ["0.03", "normal", "3", "0.98", "1"],
    "typical range / possible values": [
        "0.01 ... 0.3",
        "normal, laplace, logistic, gumbel",
        "1 ... 10",
        "0.9 ... 0.99",
        "0.5 ... 1.5",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- Disclaimer: I have not seen this algorithm before, but invented it myself. It seems to be a good alternative to the other random algorithms
- Expect good results for convex and nonconvex optimization problems
- For a short optimization run to get an acceptable solution
"""


implementation_ = """
"""


def random_annealing_app():
    st.title("Random Annealing")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/random_annealing_0.gif"))
    col3.image(os.path.join(here_, "_images/random_annealing_1.gif"))
    col2.image(os.path.join(here_, "_images/random_annealing_2.gif"))
    col3.image(os.path.join(here_, "_images/random_annealing_3.gif"))

    # col1.subheader("About the implementation")
    # col1.markdown(implementation_)

    col1.error(properties_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
