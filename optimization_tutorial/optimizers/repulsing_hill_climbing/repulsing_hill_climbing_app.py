import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    epsilon_intro_,
    distribution_intro_,
    n_neighbours_intro_,
    repulsion_factor_intro_,
)
from parameters_dicts import (
    epsilon_d_,
    distribution_d_,
    n_neighbours_d_,
    repulsion_factor_d,
)

explanation_ = """
The repulsing hill climbing optimization algorithm improves the normal hill 
climbing by adding a way to escape local optimia. If no better position is 
found within the next `n_neighbours` positions the algorithm will increase 
`epsilon` by the `repulsion_factor` for the next iteration.
"""

para_d = dict()
para_d.update(epsilon_d_)
para_d.update(distribution_d_)
para_d.update(n_neighbours_d_)
para_d.update(repulsion_factor_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Better exploration of search space than most hill climbing based algorithms
- Good for convex- and non-convex optimization problems
"""
bad_ = """ 
- ...
"""
info_ = """ 
- ...
"""


implementation_ = """
...
"""

overview_app_args_d = {
    "title": "Repulsing Hill Climbing Optimizer",
    "_name_": "repulsing_hill_climbing",
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
repulsion_factor_args_d = {
    "title": "repulsion_factor",
    "_name_": "repulsion_factor",
    "explanation_": repulsion_factor_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "epsilon": (parameter_app, epsilon_args_d),
    "distribution": (parameter_app, distribution_args_d),
    "n_neighbours": (parameter_app, n_neighbours_args_d),
    "repulsion_factor": (parameter_app, repulsion_factor_args_d),
}


def repulsing_hill_climbing_app(gfo_version):
    optimizer_app(app_d)
