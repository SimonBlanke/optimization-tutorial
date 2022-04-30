import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    step_size_intro_,
)
from parameters_dicts import (
    step_size_d,
)

explanation_ = """
The grid search explores the search space by starting from a corner and progressing `step_size`-steps
per iteration. Increasing the `step_size` enables a more uniform exploration of the search space. 
"""

para_d = dict()
para_d.update(step_size_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Best method for exploring the search space completly
"""
bad_ = """ 
- Does not adapt its behaviour to the optimization problem.
"""
info_ = """ 
- Increasing the `step_size` is advised for better exploration.
"""


implementation_ = """
The implementation of this grid-search was realized by
[Thomas Gak-Deluen](https://github.com/tgdn) and his team. The algorithm
works by choosing a direction in the beginning and moving through the search space
one 2-dimensional-plane at a time.
"""

overview_app_args_d = {
    "title": "Grid Search",
    "_name_": "grid_search",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}
step_size_args_d = {
    "title": "step_size",
    "_name_": "step_size",
    "explanation_": step_size_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "step_size": (parameter_app, step_size_args_d),
}


def grid_search_app(gfo_version):
    optimizer_app(app_d)
