from http.client import BAD_GATEWAY
import os
import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


explanation_ = """
Hill climbing is a very basic optimization technique, that explores the search space only localy. 
It starts at an initial point, which is often chosen randomly and continues to move to positions 
with a better solution. It has no method against getting stuck in local optima.
"""

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


good_ = """ 
- Very well adapted to convex optimization problems
"""
bad_ = """ 
- Expect average/poor results for non-convex problems
"""
info_ = """ 
- Useful to do finetuning a good initial starting position
- Increase `epsilon` for better global exploration or decrease for local exploration
"""


implementation_ = """
The hill climbing algorithm is saving the current position in the search space and finds a new position by selecting a random position around it. This is done with a gaussian distribution. So if the position is further away the probability of getting selected is lower, but never zero. This makes the hill climbing more heuristic and a bit more adaptable. The standard deviation of the gaussian distribution in each dimension is dependend on the size of the search space in the corresponding dimension. This improves the exploration performance if the sizes of the search space dimensions are differing from each other.
"""


def hill_climbing_app():
    st.title("Hill Climbing Optimizer")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.subheader("Introduction")
    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/hill_climbing_0.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_1.gif"))
    col2.image(os.path.join(here_, "_images/hill_climbing_2.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_3.gif"))
    col2.image(os.path.join(here_, "_images/hill_climbing_4.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_5.gif"))

    col1.subheader("About the implementation")
    col1.markdown(implementation_)

    col1.subheader("Parameters")
    col1.table(para_df)

    col1.subheader("Characteristics")
    col1.success(good_)
    col1.error(bad_)
    col1.info(info_)
