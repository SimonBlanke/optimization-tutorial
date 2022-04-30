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
time with a hill climbing algorithm. This works by setting the 
search space range for all dimensions except one to a single value. The hill climbing
algorithms searches the best position within this dimension. 
After `iters_p_dim` iterations the next dimension is searched, while the 
search space range from the previously searched dimension is set to the best position,
This way the algorithm finds new best positions one dimension at a time.
"""

para_d = dict()
para_d.update(iters_p_dim_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Expect good results for convex and nonconvex optimization problems.
"""
bad_ = """ 
- After converging to a solution the algorithm will not continue to explore
the search space.
"""
info_ = """ 
- The first few iterations in each dimension are random initialization
steps.
"""


implementation_ = """
The powell's method implemented in Gradient-Free-Optimizers does only see one dimension at a time.
This differs from the original idea of creating (and searching through) 
one search-vector at a time, that spans through multiple dimensions.
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


def powells_method_app(gfo_version):
    optimizer_app(app_d)
