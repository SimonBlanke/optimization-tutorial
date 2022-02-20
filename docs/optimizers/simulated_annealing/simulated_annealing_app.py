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
    annealing_rate_intro_,
    start_temp_intro_,
)
from parameters_dicts import (
    epsilon_d_,
    distribution_d_,
    n_neighbours_d_,
    annealing_rate_d,
    start_temp_d,
)

explanation_ = """
Simulated annealing chooses its next possible position similar to hill climbing, but it accepts 
worse results with a probability that decreases with time.
It simulates a temperature that decreases with each iteration, similar to a material cooling down.
"""

para_d = dict()
para_d.update(epsilon_d_)
para_d.update(distribution_d_)
para_d.update(n_neighbours_d_)
para_d.update(annealing_rate_d)
para_d.update(start_temp_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Expect good results for convex optimization problems
- Better adapted for non-convex problems than normal hill climbing
- Useful to do finetuning on a good initial starting position
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
    "title": "Simulated Annealing Optimizer",
    "_name_": "simulated_annealing",
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
annealing_rate_args_d = {
    "title": "annealing_rate",
    "_name_": "annealing_rate",
    "explanation_": annealing_rate_intro_,
    "here_": here_,
}
start_temp_args_d = {
    "title": "start_temp",
    "_name_": "start_temp",
    "explanation_": start_temp_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "epsilon": (parameter_app, epsilon_args_d),
    "distribution": (parameter_app, distribution_args_d),
    "n_neighbours": (parameter_app, n_neighbours_args_d),
    "annealing_rate": (parameter_app, annealing_rate_args_d),
    "start_temp": (parameter_app, start_temp_args_d),
}


def simulated_annealing_app():
    optimizer_app(app_d)
