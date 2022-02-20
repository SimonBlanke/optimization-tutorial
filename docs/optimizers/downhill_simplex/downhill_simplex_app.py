import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    alpha_intro_,
    gamma_intro_,
    beta_intro_,
    sigma_intro_,
)
from parameters_dicts import (
    alpha_d,
    gamma_d,
    beta_d,
    sigma_d,
)

explanation_ = """
The downhill simplex optimizer works by grouping `number of dimensions + 1`-positions into a simplex.
The search space is explored by reflecting, expanding, contracting or shrinking the simplex via
the `alpha`, `gamma`, `beta` or `sigma` parameters.
"""

para_d = dict()
para_d.update(alpha_d)
para_d.update(gamma_d)
para_d.update(beta_d)
para_d.update(sigma_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Good results for convex and nonconvex optimization problems
- The performance of the algorithm depends heavily on the positions in the initial simplex
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
    "title": "Downhill Simplex Optimizer",
    "_name_": "downhill_simplex",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}
alpha_args_d = {
    "title": "alpha",
    "_name_": "alpha",
    "explanation_": alpha_intro_,
    "here_": here_,
}
gamma_args_d = {
    "title": "gamma",
    "_name_": "gamma",
    "explanation_": gamma_intro_,
    "here_": here_,
}
beta_args_d = {
    "title": "beta",
    "_name_": "beta",
    "explanation_": beta_intro_,
    "here_": here_,
}
sigma_args_d = {
    "title": "sigma",
    "_name_": "sigma",
    "explanation_": sigma_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "alpha": (parameter_app, alpha_args_d),
    "gamma": (parameter_app, gamma_args_d),
    "beta": (parameter_app, beta_args_d),
    "sigma": (parameter_app, sigma_args_d),
}


def downhill_simplex_app():
    optimizer_app(app_d)
