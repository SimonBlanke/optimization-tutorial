def warn(*args, **kwargs):
    pass


import os
import warnings

warnings.warn = warn


from gradient_free_optimizers import (
    HillClimbingOptimizer,
    StochasticHillClimbingOptimizer,
    RepulsingHillClimbingOptimizer,
    SimulatedAnnealingOptimizer,
    DownhillSimplexOptimizer,
    RandomSearchOptimizer,
    PowellsMethod,
    GridSearchOptimizer,
    RandomRestartHillClimbingOptimizer,
    RandomAnnealingOptimizer,
    PatternSearch,
    ParallelTemperingOptimizer,
    ParallelAnnealingOptimizer,
    ParticleSwarmOptimizer,
    EvolutionStrategyOptimizer,
    BayesianOptimizer,
    TreeStructuredParzenEstimators,
    ForestOptimizer,
)


from surfaces.test_functions import (
    SphereFunction,
    AckleyFunction,
    HimmelblausFunction,
    CrossInTrayFunction,
    GoldsteinPriceFunction,
    EasomFunction,
)
from gradient_free_optimization_plots import search_path_gif


n_iter_single = 150
n_iter_pop = 150
n_iter_smbo = 30


opt_para = {}
random_state = 0


sphere_function = SphereFunction(n_dim=2)
ackley_function = AckleyFunction()
himmelblaus_function = HimmelblausFunction()
cross_in_tray_function = CrossInTrayFunction()
goldstein_price_function = GoldsteinPriceFunction()
easom_function = EasomFunction()


def generate_gifs_single_opt(optimizer_class):
    opt_name = optimizer_class._name_
    path = os.path.join(opt_name, "_images")

    sphere_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_0.gif",
        "n_iter": n_iter_single,
        "objective_function": sphere_function,
        "search_space": sphere_function.search_space(min=-5, max=10),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": sphere_function.name,
    }

    ackley_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_1.gif",
        "n_iter": n_iter_single,
        "objective_function": ackley_function,
        "search_space": ackley_function.search_space(min=-5, max=10),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": ackley_function.name,
    }

    himmelblaus_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_2.gif",
        "n_iter": n_iter_single,
        "objective_function": himmelblaus_function,
        "search_space": himmelblaus_function.search_space(min=-5, max=5),
        "initialize": {"warm_start": [{"x0": -3, "x1": 0}], "vertices": 4},
        "random_state": random_state,
        "title": himmelblaus_function.name,
    }

    cross_in_tray_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_3.gif",
        "n_iter": n_iter_single,
        "objective_function": cross_in_tray_function,
        "search_space": cross_in_tray_function.search_space(min=-10, max=10),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": cross_in_tray_function.name,
    }
    goldstein_price_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_4.gif",
        "n_iter": n_iter_single,
        "objective_function": goldstein_price_function,
        "search_space": goldstein_price_function.search_space(min=-5, max=5),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": goldstein_price_function.name,
    }

    easom_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_5.gif",
        "n_iter": n_iter_single,
        "objective_function": easom_function,
        "search_space": easom_function.search_space(min=-5, max=5),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": easom_function.name,
    }
    search_path_gif(**sphere_function_d)
    search_path_gif(**ackley_function_d)
    search_path_gif(**himmelblaus_function_d)
    search_path_gif(**cross_in_tray_function_d)
    search_path_gif(**goldstein_price_function_d)
    search_path_gif(**easom_function_d)


def generate_gifs_pop_opt(optimizer_class):
    opt_name = optimizer_class._name_
    path = os.path.join(opt_name, "_images")

    sphere_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_0.gif",
        "n_iter": n_iter_pop,
        "objective_function": sphere_function,
        "search_space": sphere_function.search_space(min=-5, max=10),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": sphere_function.name,
    }

    ackley_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_1.gif",
        "n_iter": n_iter_pop,
        "objective_function": ackley_function,
        "search_space": ackley_function.search_space(min=-5, max=10),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": ackley_function.name,
    }

    himmelblaus_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_2.gif",
        "n_iter": n_iter_pop,
        "objective_function": himmelblaus_function,
        "search_space": himmelblaus_function.search_space(min=-5, max=5),
        "initialize": {"warm_start": [{"x0": -3, "x1": 0}], "vertices": 4},
        "random_state": random_state,
        "title": himmelblaus_function.name,
    }

    cross_in_tray_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_4.gif",
        "n_iter": n_iter_pop,
        "objective_function": cross_in_tray_function,
        "search_space": cross_in_tray_function.search_space(min=-10, max=10),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": cross_in_tray_function.name,
    }

    search_path_gif(**sphere_function_d)
    search_path_gif(**ackley_function_d)
    search_path_gif(**himmelblaus_function_d)
    search_path_gif(**cross_in_tray_function_d)


def generate_gifs_smbo_opt(optimizer_class):
    opt_name = optimizer_class._name_
    path = os.path.join(opt_name, "_images")

    sphere_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_0.gif",
        "n_iter": n_iter_smbo,
        "objective_function": sphere_function,
        "search_space": sphere_function.search_space(min=-5, max=10),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": sphere_function.name,
    }

    ackley_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_1.gif",
        "n_iter": n_iter_smbo,
        "objective_function": ackley_function,
        "search_space": ackley_function.search_space(min=-5, max=10),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": ackley_function.name,
    }

    himmelblaus_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_2.gif",
        "n_iter": n_iter_smbo,
        "objective_function": himmelblaus_function,
        "search_space": himmelblaus_function.search_space(min=-5, max=5),
        "initialize": {"warm_start": [{"x0": -3, "x1": 0}], "vertices": 4},
        "random_state": random_state,
        "title": himmelblaus_function.name,
    }

    cross_in_tray_function_d = {
        "path": path,
        "optimizer": optimizer_class,
        "opt_para": opt_para,
        "name": opt_name + "_3.gif",
        "n_iter": n_iter_smbo,
        "objective_function": cross_in_tray_function,
        "search_space": cross_in_tray_function.search_space(min=-10, max=10),
        "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
        "random_state": random_state,
        "title": cross_in_tray_function.name,
    }

    search_path_gif(**sphere_function_d)
    search_path_gif(**ackley_function_d)
    search_path_gif(**himmelblaus_function_d)
    search_path_gif(**cross_in_tray_function_d)


opt_list_single = [
    HillClimbingOptimizer,
    StochasticHillClimbingOptimizer,
    RepulsingHillClimbingOptimizer,
    SimulatedAnnealingOptimizer,
    DownhillSimplexOptimizer,
    RandomSearchOptimizer,
    PowellsMethod,
    GridSearchOptimizer,
    RandomRestartHillClimbingOptimizer,
    RandomAnnealingOptimizer,
    PatternSearch,
]


opt_list_pop = [
    ParallelTemperingOptimizer,
    ParallelAnnealingOptimizer,
    ParticleSwarmOptimizer,
    EvolutionStrategyOptimizer,
]


opt_list_smbo = [
    BayesianOptimizer,
    TreeStructuredParzenEstimators,
    ForestOptimizer,
]


for opt_ in opt_list_single:
    generate_gifs_single_opt(opt_)
"""
for opt_ in opt_list_pop:
    generate_gifs_pop_opt(opt_)

for opt_ in opt_list_smbo:
    generate_gifs_smbo_opt(opt_)
"""
