import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
The grid search explores the search space by starting from a corner and progressing `step_size`-steps
per iteration. Increasing the `step_size` enables a more uniform exploration of the search space. 
"""

para_d = {
    "Parameter": ["step_size"],
    "Type": ["int"],
    "default": ["1"],
    "typical range / possible values": [
        "1 ... 100",
    ],
}
para_df = pd.DataFrame(para_d)


properties_ = """
- Does not adapt its behaviour to the optimization problem.
- Best method for exploring the search space completly
- Increasing the `step_size` is advised for better exploration.
"""


implementation_ = """
"""


def grid_search_app():
    st.title("Grid Search")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/grid_search_0.gif"))
    col3.image(os.path.join(here_, "_images/grid_search_1.gif"))
    col2.image(os.path.join(here_, "_images/grid_search_2.gif"))
    col3.image(os.path.join(here_, "_images/grid_search_3.gif"))

    # col1.subheader("About the implementation")
    # col1.markdown(implementation_)

    col1.subheader("Available parameters")
    col1.table(para_df)

    col1.subheader("Use case")
    col1.markdown(properties_)
