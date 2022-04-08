import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    tree_regressor_intro_,
    xi_intro_,
    warm_start_smbo_intro_,
)
from parameters_dicts import (
    tree_regressor_d,
    xi_forest_opt_d,
    warm_start_smbo_d,
)

explanation_ = """
The forest-optimizer calculates the expected improvement of the position space with a 
tree-based model. This optimization technique is very similar to bayesian-optimization
in every part, except its model.
"""

para_d = dict()
para_d.update(tree_regressor_d)
para_d.update(xi_forest_opt_d)
para_d.update(warm_start_smbo_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Very good performance
"""
bad_ = """
- High computational load compared to non-smb-optimizers.
- Should only be used for 
computationally expensive objective-functions.
- A large search space forces random sampling of the position space, which 
decreases optimizer performance.
"""
info_ = """
- High values of `xi` improves the exploration of the search space.
"""


implementation_ = """
The forest-optimizer shares most of its code base with the bayesian-optimizer. Only its model, to 
calculate the expected score and its standard deviation is different. Tree based models do not 
calculate the standard deviation by them self. A modification is necessary to determine the
standard deviation from the impurity of the trees in the ensemble.
"""

overview_app_args_d = {
    "title": "Forest Optimization",
    "_name_": "forest_optimization",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}
tree_regressor_args_d = {
    "title": "tree_regressor",
    "_name_": "tree_regressor",
    "explanation_": tree_regressor_intro_,
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
    # "tree_regressor": (parameter_app, tree_regressor_args_d),
    "xi": (parameter_app, xi_args_d),
    # "warm_start_smbo": (parameter_app, warm_start_smbo_args_d),
}


def forest_optimization_app(gfo_version):
    optimizer_app(app_d)
