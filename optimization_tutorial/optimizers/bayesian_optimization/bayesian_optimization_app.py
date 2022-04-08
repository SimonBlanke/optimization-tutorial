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
Bayesian optimization chooses new positions by calculating the expected 
improvement of every position in the search space based on a gaussian process 
that trains on already evaluated positions.
"""

para_d = dict()
para_d.update(gpr_bayes_opt_d)
para_d.update(xi_bayes_opt_d)
para_d.update(warm_start_smbo_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Exceptional performance
"""
bad_ = """
- High computational load compared to non-smb-optimizers.
- Should only be used for 
computationally expensive objective-functions.
- A large search space forces random sampling of the position space, which 
decreases optimizer performance.
"""
info_ = """
- Changing `gpr` heavily impacts the optimization algorithm.
- Passing a modified random-forest to `gpr` transforms the bayesian-optimizer to a 
forest-optimizer.
- High values of `xi` improves the exploration of the search space.
"""


implementation_ = """
The bayesian optimizer collects the information about the position and score in each 
iteration. The gaussian process regressor fits to the position (features) and score (target),
and predicts the scores of all unknown positions. This is why the bayesian optimization needs
at least one initial position. The gaussian process returns the standard deviation 
in addition to the prediction (or mean), both of which are required to 
compute the acquisition function.
The position of the best predicted score
is evaluated next. The selected position and its true score is then collected, 
restarting the cycle.
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
    "xi": (parameter_app, xi_args_d),
}


def bayesian_optimization_app(gfo_version):
    optimizer_app(app_d)
