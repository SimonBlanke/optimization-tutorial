import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
The pattern search creates a cross-like pattern that moves its center position to 
the best surrounding position or shrinks if no better position is available.
"""

para_d = {
    "Parameter": ["n_positions", "pattern_size", "reduction"],
    "Type": ["int", "float", "float"],
    "default": ["4", "0.25", "0.9"],
    "typical range / possible values": [
        "2 ... 10",
        "0.05 ... 0.5",
        "0.75 ... 0.99",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- Expect good results for convex and nonconvex optimization problems
- Stopps exploring search space after converging to best position
"""


implementation_ = """
"""


def pattern_search_app():
    st.title("Pattern Search")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/pattern_search_0.gif"))
    col3.image(os.path.join(here_, "_images/pattern_search_1.gif"))
    col2.image(os.path.join(here_, "_images/pattern_search_2.gif"))
    col3.image(os.path.join(here_, "_images/pattern_search_3.gif"))

    # col1.subheader("About the implementation")
    # col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
