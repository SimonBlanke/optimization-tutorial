import os
import sys
import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(here_, ".."))

from optimizer_template import optimizer_app
from overview_parameters_template import overview_app, parameter_app
from parameters_info import (
    population_intro_,
    inertia_intro_,
    cognitive_weight_intro_,
    social_weight_intro_,
)
from parameters_dicts import (
    population_parallel_temp_d,
    inertia_d,
    cognitive_weight_d,
    social_weight_d,
)

explanation_ = """
Particle swarm optimization works by initializing a number of positions in the search space,
which move according to their own ineratia, the attraction to their own known best positions
and the global best position.
"""

para_d = dict()
para_d.update(population_parallel_temp_d)
para_d.update(inertia_d)
para_d.update(cognitive_weight_d)
para_d.update(social_weight_d)


para_df = pd.DataFrame.from_dict(
    para_d, orient="index", columns=("type", "default", "typical range/possible values")
)


good_ = """ 
- Expect very good results for convex optimization problems.
- Expect good results for nonconvex optimization problems.
"""
bad_ = """ 
- The particle swarm optimizer is not adapted to categorical search space dimensions.
- Population based optimizers generally need a higher minimum number of iterations
to find a good solution (compared to non-population-based algorithms).
- The algorithm will not continue to explore the search space after the particles converged 
to an optimal position.
"""
info_ = """ 
- The `inertia` lets the particle maintain its own velocity. The `cognitive_weight` and 
`social_weight` alter the direction and velocity of the particle.
"""


implementation_ = """
The particle swarm optimizer initializes multiple particle classes, which inherit from
the hill-climbing class. In the current version all movement-calculations are contained in
the particle class. Particles have a velocity, which they maintain even without attraction
to other particles via `cognitive_weight` or `social_weight`.
"""

overview_app_args_d = {
    "title": "Particle Swarm Optimization",
    "_name_": "particle_swarm_optimization",
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
inertia_args_d = {
    "title": "inertia",
    "_name_": "inertia",
    "explanation_": inertia_intro_,
    "here_": here_,
}
cognitive_weight_args_d = {
    "title": "cognitive_weight",
    "_name_": "cognitive_weight",
    "explanation_": cognitive_weight_intro_,
    "here_": here_,
}
social_weight_args_d = {
    "title": "social_weight",
    "_name_": "social_weight",
    "explanation_": social_weight_intro_,
    "here_": here_,
}


app_d = {
    "Overview": (overview_app, overview_app_args_d),
    "population": (parameter_app, population_args_d),
    "inertia": (parameter_app, inertia_args_d),
    "cognitive_weight": (parameter_app, cognitive_weight_args_d),
    "social_weight": (parameter_app, social_weight_args_d),
}


def particle_swarm_optimization_app(gfo_version):
    optimizer_app(app_d)
