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
    n_iter_restart_intro_,
)
from parameters_dicts import (
    epsilon_d_,
    distribution_d_,
    n_neighbours_d_,
    n_iter_restart_d,
)

explanation_ = """
Random restart hill climbing works by starting a hill climbing search and jumping to a random 
new position after `n_iter_restart` iterations. 
Those restarts should prevent the algorithm getting stuck in local optima.
"""

para_d = dict()
para_d.update(epsilon_d_)
para_d.update(distribution_d_)
para_d.update(n_neighbours_d_)
para_d.update(n_iter_restart_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Expect good results for convex and nonconvex optimization problems.
"""
bad_ = """ 
- Worse than regular hill climbing algorithm for convex optimization
- Does not intelligently decide when to restart
"""
info_ = """ 
- Similar to random search for low values of `n_iter_restart`
"""


implementation_ = """
The random restart hill climbing inherits its behaviour from the regular hill climbing and 
expands it by jumping to a random position during the iteration step. 
"""

overview_app_args_d = {
    "title": "Random Restart Hill Climbing Optimizer",
    "_name_": "random_restart_hill_climbing",
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
n_iter_restart_args_d = {
    "title": "n_iter_restart",
    "_name_": "n_iter_restart",
    "explanation_": n_iter_restart_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "epsilon": (parameter_app, epsilon_args_d),
    "distribution": (parameter_app, distribution_args_d),
    "n_neighbours": (parameter_app, n_neighbours_args_d),
    "n_iter_restart": (parameter_app, n_iter_restart_args_d),
}


def random_restart_hill_climbing_app(gfo_version):
    optimizer_app(app_d)
