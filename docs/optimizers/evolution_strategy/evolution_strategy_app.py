import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    population_intro_,
    mutation_rate_intro_,
    crossover_rate_intro_,
)
from parameters_dicts import (
    population_parallel_temp_d,
    mutation_rate_d,
    crossover_rate_d,
)

explanation_ = """
Evolution strategy mutates and combines the best individuals of a population across a 
number of generations without transforming them into an array of bits 
(like genetic algorithms) but uses the real values of the positions.
"""

para_d = dict()
para_d.update(population_parallel_temp_d)
para_d.update(mutation_rate_d)
para_d.update(crossover_rate_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- If the search space is very complex and large
- If you have enough time for many model evaluations
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
    "title": "Evolution Strategy",
    "_name_": "evolution_strategy",
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
mutation_rate_args_d = {
    "title": "mutation_rate",
    "_name_": "mutation_rate",
    "explanation_": mutation_rate_intro_,
    "here_": here_,
}
crossover_rate_args_d = {
    "title": "crossover_rate",
    "_name_": "crossover_rate",
    "explanation_": crossover_rate_intro_,
    "here_": here_,
}

app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "population": (parameter_app, population_args_d),
    "mutation_rate": (parameter_app, mutation_rate_args_d),
    "crossover_rate": (parameter_app, crossover_rate_args_d),
}


def evolution_strategy_app():
    optimizer_app(app_d)
