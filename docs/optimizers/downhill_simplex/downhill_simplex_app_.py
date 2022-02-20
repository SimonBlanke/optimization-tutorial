import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
The downhill simplex optimizer works by grouping `number of dimensions + 1`-positions into a simplex.
The search space is explored by reflecting, expanding, contracting or shrinking the simplex via
the `alpha`, `gamma`, `beta` or `sigma` parameters.
"""

para_d = {
    "Parameter": ["alpha", "gamma", "beta", "sigma"],
    "Type": ["float", "float", "float", "float"],
    "default": ["1", "2", "0.5", "0.5"],
    "typical range / possible values": [
        "0.5 ... 1.5",
        "1 ... 3",
        "0.25 ... 1",
        "0.25 ... 1",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- Good results for convex and nonconvex optimization problems
- The performance of the algorithm depends heavily on the positions in the initial simplex
"""


implementation_ = """
"""


def downhill_simplex_app():
    st.title("Downhill Simplex Optimizer")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/downhill_simplex_0.gif"))
    col3.image(os.path.join(here_, "_images/downhill_simplex_1.gif"))
    col2.image(os.path.join(here_, "_images/downhill_simplex_2.gif"))
    col3.image(os.path.join(here_, "_images/downhill_simplex_3.gif"))

    col1.subheader("About the implementation")
    col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
