import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    gpr_intro_,
    xi_intro_,
    warm_start_smbo_intro_,
)
from parameters_dicts import (
    gpr_bayes_opt_d,
    xi_bayes_opt_d,
    warm_start_smbo_d,
)

explanation_ = """
...
"""

para_d = dict()
para_d.update(gpr_bayes_opt_d)
para_d.update(xi_bayes_opt_d)
para_d.update(warm_start_smbo_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- ...
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
    "title": "Bayesian Optimization",
    "_name_": "bayesian_optimization",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}
gpr_args_d = {
    "title": "gpr",
    "_name_": "gpr",
    "explanation_": gpr_intro_,
    "here_": here_,
}
xi_args_d = {
    "title": "xi",
    "_name_": "xi",
    "explanation_": xi_intro_,
    "here_": here_,
}
warm_start_smbo_args_d = {
    "title": "warm_start_smbo",
    "_name_": "warm_start_smbo",
    "explanation_": warm_start_smbo_intro_,
    "here_": here_,
}

app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "gpr": (parameter_app, gpr_args_d),
    "xi": (parameter_app, xi_args_d),
    "warm_start_smbo": (parameter_app, warm_start_smbo_args_d),
}


def bayesian_optimization_app():
    optimizer_app(app_d)
