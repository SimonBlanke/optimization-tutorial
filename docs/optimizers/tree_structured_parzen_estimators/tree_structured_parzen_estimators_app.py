import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    gamma_tpe_intro_,
    warm_start_smbo_intro_,
)
from parameters_dicts import (
    gamma_tpe_d,
    warm_start_smbo_d,
)

explanation_ = """
Tree of Parzen Estimators also chooses new positions by calculating the expected improvement. 
It does so by calculating the ratio of probability being among the best positions and 
the worst positions. Those probabilities are determined with a kernel density estimator,
that is trained on alrady evaluated positions.
"""

para_d = dict()
para_d.update(gamma_tpe_d)
para_d.update(warm_start_smbo_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- If model evaluations take a long time
- If you do not want to do many iterations
- If your search space is not to big
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
    "title": "Tree Structured Parzen Estimators",
    "_name_": "tree_structured_parzen_estimators",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}
gamma_tpe_args_d = {
    "title": "gamma_tpe",
    "_name_": "gamma_tpe",
    "explanation_": gamma_tpe_intro_,
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
    "gamma_tpe": (parameter_app, gamma_tpe_args_d),
    "warm_start_smbo": (parameter_app, warm_start_smbo_args_d),
}


def tree_structured_parzen_estimators_app():
    optimizer_app(app_d)
