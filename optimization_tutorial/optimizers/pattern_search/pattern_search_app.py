import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    n_positions_intro_,
    pattern_size_intro_,
    reduction_intro_,
)
from parameters_dicts import (
    n_positions_d,
    pattern_size_d,
    reduction_d,
)

explanation_ = """
This powell's method implementation works by optimizing each search space dimension at a 
time with a hill climbing algorithm.
"""

para_d = dict()
para_d.update(n_positions_d)
para_d.update(pattern_size_d)
para_d.update(reduction_d)


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
    "title": "Pattern Search",
    "_name_": "pattern_search",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}
n_positions_args_d = {
    "title": "n_positions",
    "_name_": "n_positions",
    "explanation_": n_positions_intro_,
    "here_": here_,
}
pattern_size_args_d = {
    "title": "pattern_size",
    "_name_": "pattern_size",
    "explanation_": pattern_size_intro_,
    "here_": here_,
}
reduction_args_d = {
    "title": "reduction",
    "_name_": "reduction",
    "explanation_": reduction_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "n_positions": (parameter_app, n_positions_args_d),
    "pattern_size": (parameter_app, pattern_size_args_d),
    "reduction": (parameter_app, reduction_args_d),
}


def pattern_search_app(gfo_version):
    optimizer_app(app_d)
