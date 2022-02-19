import os
import sys

import pandas as pd
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))

para_path_ = os.path.join(here_)
sys.path.append(para_path_)

from epsilon_app import epsilon_app
from distribution_app import distribution_app
from n_neighbours_app import n_neighbours_app

from parameters_dicts import epsilon_d_, distribution_d_, n_neighbours_d_

explanation_ = """
Hill climbing is a very basic optimization technique, that explores the search space only localy. 
It starts at an initial point, which is often chosen randomly and continues to move to positions 
with a better solution. It has no method against getting stuck in local optima.
"""

para_d = dict()
para_d.update(epsilon_d_)
para_d.update(distribution_d_)
para_d.update(n_neighbours_d_)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Very well adapted to convex optimization problems
- Useful to do finetuning on a good initial starting position
"""
bad_ = """ 
- Expect average/poor results for non-convex problems
"""
info_ = """ 
- Increase `epsilon` for better global exploration or decrease for local exploration
- The `distribution` changes the behaviour of the hill climbing in multiple ways
- A higher `n_neighbours` slows down the movement through the search space and improves selection of next position
"""


implementation_ = """
The hill climbing algorithm is saving the current position in the search space and finds 
a new position by selecting a random position around it. This is done with a gaussian 
`distribution`. So if the position is further away the probability of getting selected is 
lower, but never zero. This makes the hill climbing more heuristic and a bit more adaptable. 
The standard deviation of the gaussian distribution in each dimension is dependend on the size 
of the search space in the corresponding dimension. This improves the exploration performance 
if the sizes of the search space dimensions are differing from each other.
"""


def overview_():
    st.title("Hill Climbing Optimizer")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )
    st.write("")
    col1, col2, col3 = st.columns((2, 1, 1))

    col1.header("Introduction")
    col1.markdown(explanation_)

    col2.image(os.path.join(here_, "_images/hill_climbing_0.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_1.gif"))
    col2.image(os.path.join(here_, "_images/hill_climbing_2.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_3.gif"))
    col2.image(os.path.join(here_, "_images/hill_climbing_4.gif"))
    col3.image(os.path.join(here_, "_images/hill_climbing_5.gif"))

    col1.header("About the implementation")
    col1.markdown(implementation_)

    col1.header("Characteristics")
    col1.success(good_)
    col1.error(bad_)
    col1.info(info_)

    col1.header("Parameters")
    col1.table(para_df)


hill_climbing_app_d = {
    "Overview": overview_,
    "epsilon": epsilon_app,
    "distribution": distribution_app,
    "n_neighbours": n_neighbours_app,
}


def hill_climbing_app():
    st.sidebar.write("")
    radio_select = st.sidebar.radio(
        "Parameters", options=("Overview", "epsilon", "distribution", "n_neighbours")
    )

    hill_climbing_app_d[radio_select]()
