import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    iters_p_dim_intro_,
)
from parameters_dicts import (
    iters_p_dim_d,
)

explanation_ = """
This powell's method implementation works by optimizing each search space dimension at a 
time with a hill climbing algorithm.
"""

para_d = dict()
para_d.update(iters_p_dim_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Very well adapted to convex optimization problems
- Expect good results for nonconvex problems
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
    "title": "Powell's Method",
    "_name_": "powells_method",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}
iters_p_dim_args_d = {
    "title": "iters_p_dim",
    "_name_": "iters_p_dim",
    "explanation_": iters_p_dim_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "iters_p_dim": (parameter_app, iters_p_dim_args_d),
}


def powells_method_app():
    optimizer_app(app_d)
