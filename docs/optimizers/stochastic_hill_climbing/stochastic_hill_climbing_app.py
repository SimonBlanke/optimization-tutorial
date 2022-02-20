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
    p_accept_intro_,
)
from parameters_dicts import epsilon_d_, distribution_d_, n_neighbours_d_, p_accept_d_

explanation_ = """
Stochastic hill climbing extends the normal hill climbing by a simple method against getting 
stuck in local optima. It has a parameter you can set, that determines the probability to 
accept worse solutions as a next position.
"""

para_d = dict()
para_d.update(epsilon_d_)
para_d.update(distribution_d_)
para_d.update(n_neighbours_d_)
para_d.update(p_accept_d_)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Expect good results for convex optimization problems
- Better adapted for non-convex problems than normal hill climbing
- Useful to do finetuning on a good initial starting position
"""
bad_ = """ 
- Worse than hill climbing for convex optimization
"""
info_ = """ 
- ...
"""


implementation_ = """
...
"""

overview_app_args_d = {
    "title": "Stochastic Hill Climbing Optimizer",
    "_name_": "stochastic_hill_climbing",
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
p_accept_args_d = {
    "title": "p_accept",
    "_name_": "p_accept",
    "explanation_": p_accept_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "epsilon": (parameter_app, epsilon_args_d),
    "distribution": (parameter_app, distribution_args_d),
    "n_neighbours": (parameter_app, n_neighbours_args_d),
    "p_accept": (parameter_app, p_accept_args_d),
}


def stochastic_hill_climbing_app():
    optimizer_app(app_d)
