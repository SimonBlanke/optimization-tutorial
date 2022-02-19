def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import HillClimbingOptimizer


from surfaces.test_functions import (
    SphereFunction,
    AckleyFunction,
    HimmelblausFunction,
    CrossInTrayFunction,
    GoldsteinPriceFunction,
    EasomFunction,
)
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = HillClimbingOptimizer

sphere_function = SphereFunction(n_dim=2)
ackley_function = AckleyFunction()


hill_climbing_sphere_function_template_d = {
    "path": "_images",
    "optimizer": optimizer_class,
    "n_iter": n_iter,
    "objective_function": sphere_function,
    "search_space": sphere_function.search_space(min=-5, max=10),
    "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
    "random_state": random_state,
}

hill_climbing_ackley_function_template_d = {
    "path": "_images",
    "optimizer": optimizer_class,
    "n_iter": n_iter,
    "objective_function": ackley_function,
    "search_space": ackley_function.search_space(min=-5, max=10),
    "initialize": {"warm_start": [{"x0": 8, "x1": 8}], "vertices": 4},
    "random_state": random_state,
}


def generate_gifs_epsilon_():
    opt_name = optimizer_class._name_

    epsilon_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    epsilon_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    epsilon_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    epsilon_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    epsilon_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    epsilon_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    epsilon_0_d["opt_para"] = {"epsilon": 0.01}
    epsilon_0_d["name"] = opt_name + "_epsilon_0.gif"

    epsilon_1_d["opt_para"] = {"epsilon": 0.08}
    epsilon_1_d["name"] = opt_name + "_epsilon_1.gif"

    epsilon_2_d["opt_para"] = {"epsilon": 0.3}
    epsilon_2_d["name"] = opt_name + "_epsilon_2.gif"

    epsilon_10_d["opt_para"] = {"epsilon": 0.01}
    epsilon_10_d["name"] = opt_name + "_epsilon_10.gif"

    epsilon_11_d["opt_para"] = {"epsilon": 0.08}
    epsilon_11_d["name"] = opt_name + "_epsilon_11.gif"

    epsilon_12_d["opt_para"] = {"epsilon": 0.3}
    epsilon_12_d["name"] = opt_name + "_epsilon_12.gif"

    search_path_gif(**epsilon_0_d)
    search_path_gif(**epsilon_1_d)
    search_path_gif(**epsilon_2_d)

    search_path_gif(**epsilon_10_d)
    search_path_gif(**epsilon_11_d)
    search_path_gif(**epsilon_12_d)


def generate_gifs_distribution_():
    opt_name = optimizer_class._name_

    distribution_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    distribution_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    distribution_2_d = copy.copy(hill_climbing_sphere_function_template_d)
    distribution_3_d = copy.copy(hill_climbing_sphere_function_template_d)

    distribution_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    distribution_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    distribution_12_d = copy.copy(hill_climbing_ackley_function_template_d)
    distribution_13_d = copy.copy(hill_climbing_ackley_function_template_d)

    distribution_0_d["opt_para"] = {"distribution": "normal"}
    distribution_0_d["name"] = opt_name + "_distribution_0.gif"

    distribution_1_d["opt_para"] = {"distribution": "laplace"}
    distribution_1_d["name"] = opt_name + "_distribution_1.gif"

    distribution_2_d["opt_para"] = {"distribution": "logistic"}
    distribution_2_d["name"] = opt_name + "_distribution_2.gif"

    distribution_3_d["opt_para"] = {"distribution": "gumbel"}
    distribution_3_d["name"] = opt_name + "_distribution_3.gif"

    distribution_10_d["opt_para"] = {"distribution": "normal"}
    distribution_10_d["name"] = opt_name + "_distribution_10.gif"

    distribution_11_d["opt_para"] = {"distribution": "laplace"}
    distribution_11_d["name"] = opt_name + "_distribution_11.gif"

    distribution_12_d["opt_para"] = {"distribution": "logistic"}
    distribution_12_d["name"] = opt_name + "_distribution_12.gif"

    distribution_13_d["opt_para"] = {"distribution": "gumbel"}
    distribution_13_d["name"] = opt_name + "_distribution_13.gif"

    search_path_gif(**distribution_0_d)
    search_path_gif(**distribution_1_d)
    search_path_gif(**distribution_2_d)
    search_path_gif(**distribution_3_d)

    search_path_gif(**distribution_10_d)
    search_path_gif(**distribution_11_d)
    search_path_gif(**distribution_12_d)
    search_path_gif(**distribution_13_d)


def generate_gifs_n_neighbours_():
    opt_name = optimizer_class._name_

    n_neighbours_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    n_neighbours_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    n_neighbours_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    n_neighbours_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    n_neighbours_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    n_neighbours_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    n_neighbours_0_d["opt_para"] = {"n_neighbours": 1}
    n_neighbours_0_d["name"] = opt_name + "_n_neighbours_0.gif"

    n_neighbours_1_d["opt_para"] = {"n_neighbours": 4}
    n_neighbours_1_d["name"] = opt_name + "_n_neighbours_1.gif"

    n_neighbours_2_d["opt_para"] = {"n_neighbours": 8}
    n_neighbours_2_d["name"] = opt_name + "_n_neighbours_2.gif"

    n_neighbours_10_d["opt_para"] = {"n_neighbours": 1}
    n_neighbours_10_d["name"] = opt_name + "_n_neighbours_10.gif"

    n_neighbours_11_d["opt_para"] = {"n_neighbours": 4}
    n_neighbours_11_d["name"] = opt_name + "_n_neighbours_11.gif"

    n_neighbours_12_d["opt_para"] = {"n_neighbours": 8}
    n_neighbours_12_d["name"] = opt_name + "_n_neighbours_12.gif"

    search_path_gif(**n_neighbours_0_d)
    search_path_gif(**n_neighbours_1_d)
    search_path_gif(**n_neighbours_2_d)

    search_path_gif(**n_neighbours_10_d)
    search_path_gif(**n_neighbours_11_d)
    search_path_gif(**n_neighbours_12_d)


generate_gifs_epsilon_()
generate_gifs_distribution_()
generate_gifs_n_neighbours_()
