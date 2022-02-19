import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
This powell's method implementation works by optimizing each search space dimension at a 
time with a hill climbing algorithm.
"""

para_d = {
    "Parameter": ["iters_p_dim"],
    "Type": ["int"],
    "default": ["10"],
    "typical range / possible values": [
        "5 ... 25",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- Very well adapted to convex optimization problems
- Expect good results for nonconvex problems
"""


implementation_ = """
"""


def powells_method_app():
    st.title("Powell's Method")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/powells_method_0.gif"))
    col3.image(os.path.join(here_, "_images/powells_method_1.gif"))
    col2.image(os.path.join(here_, "_images/powells_method_2.gif"))
    col3.image(os.path.join(here_, "_images/powells_method_3.gif"))

    # col1.subheader("About the implementation")
    # col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
