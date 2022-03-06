import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app


explanation_ = """
The random search explores by choosing a new position at random after each iteration. 
Some random search implementations choose a new position within a large hypersphere around 
the current position. The implementation in hyperactive is purely random across the 
search space in each step.
"""

para_d = dict()
para_d.update({})


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Does not adapt its behaviour to the optimization problem.
- Very good as a first method of optimization or to start exploring the search space
- For a short optimization run to get an acceptable solution
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
    "title": "Random Search",
    "_name_": "random_search",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
}


def random_search_app(gfo_version):
    optimizer_app(app_d)
