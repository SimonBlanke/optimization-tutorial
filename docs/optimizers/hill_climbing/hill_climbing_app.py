import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import epsilon_intro_, distribution_intro_, n_neighbours_intro_
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

overview_app_args_d = {
    "title": "Hill Climbing Optimizer",
    "_name_": "hill_climbing",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}
epsilon_args_d = {
    "title": "epsilon",
    "_name_": "epsilon",
    "explanation_": epsilon_intro_,
    "here_": here_,
}
distribution_args_d = {
    "title": "distribution",
    "_name_": "distribution",
    "explanation_": distribution_intro_,
    "here_": here_,
}
n_neighbours_args_d = {
    "title": "n_neighbours",
    "_name_": "n_neighbours",
    "explanation_": n_neighbours_intro_,
    "here_": here_,
}

app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "epsilon": (parameter_app, epsilon_args_d),
    "distribution": (parameter_app, distribution_args_d),
    "n_neighbours": (parameter_app, n_neighbours_args_d),
}


def hill_climbing_app():
    optimizer_app(app_d)
