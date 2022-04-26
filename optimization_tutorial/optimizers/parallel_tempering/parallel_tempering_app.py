import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    n_iter_swap_intro_,
    population_intro_,
)
from parameters_dicts import (
    n_iter_swap_parallel_temp_d,
    population_parallel_temp_d,
)

explanation_ = """
Parallel Tempering initializes multiple simulated annealing searches with different 
temperatures and chooses to swap those temperatures with a probability based on 
its temperature and difference of current scores.
"""

para_d = dict()
para_d.update(population_parallel_temp_d)
para_d.update(n_iter_swap_parallel_temp_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Not as dependend of a good initial position as simulated annealing
- Similar computational load to regular simulated annealing
"""
bad_ = """ 
- Population based optimizers generally need a higher minimum number of iterations
to find a good solution (compared to non-population-based algorithms).
"""
info_ = """ 
-  The parameter `n_iter_swap` should be increased if `population` is increased.
"""


implementation_ = """
The population of the parallel tempering optimizer consists of multiple initializations
of the simulated annealing optimizer class. Each of those receives a random starting temperature.
The algorithm calculates the probability of swapping temperatures
for every combination of annealer instances. 
"""

overview_app_args_d = {
    "title": "Parallel Tempering",
    "_name_": "parallel_tempering",
    "explanation_": explanation_,
    "here_": here_,
    "implementation_": implementation_,
    "good_": good_,
    "bad_": bad_,
    "info_": info_,
    "para_df": para_df,
}
population_args_d = {
    "title": "population",
    "_name_": "population",
    "explanation_": population_intro_,
    "here_": here_,
}
n_iter_swap_args_d = {
    "title": "n_iter_swap",
    "_name_": "n_iter_swap",
    "explanation_": n_iter_swap_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "population": (parameter_app, population_args_d),
    "n_iter_swap": (parameter_app, n_iter_swap_args_d),
}


def parallel_tempering_app(gfo_version):
    optimizer_app(app_d)
