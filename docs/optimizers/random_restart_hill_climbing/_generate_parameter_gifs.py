def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import StochasticHillClimbingOptimizer


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = StochasticHillClimbingOptimizer

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
    epsilon_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    epsilon_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    epsilon_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    epsilon_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    epsilon_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    epsilon_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    epsilon_0_d["opt_para"] = {"epsilon": 0.01}
    epsilon_0_d["name"] = "epsilon_0.gif"

    epsilon_1_d["opt_para"] = {"epsilon": 0.08}
    epsilon_1_d["name"] = "epsilon_1.gif"

    epsilon_2_d["opt_para"] = {"epsilon": 0.3}
    epsilon_2_d["name"] = "epsilon_2.gif"

    epsilon_10_d["opt_para"] = {"epsilon": 0.01}
    epsilon_10_d["name"] = "epsilon_3.gif"

    epsilon_11_d["opt_para"] = {"epsilon": 0.08}
    epsilon_11_d["name"] = "epsilon_4.gif"

    epsilon_12_d["opt_para"] = {"epsilon": 0.3}
    epsilon_12_d["name"] = "epsilon_5.gif"

    search_path_gif(**epsilon_0_d)
    search_path_gif(**epsilon_1_d)
    search_path_gif(**epsilon_2_d)

    search_path_gif(**epsilon_10_d)
    search_path_gif(**epsilon_11_d)
    search_path_gif(**epsilon_12_d)


def generate_gifs_distribution_():
    distribution_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    distribution_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    distribution_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    distribution_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    distribution_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    distribution_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    distribution_0_d["opt_para"] = {"distribution": "normal"}
    distribution_0_d["name"] = "distribution_0.gif"

    distribution_1_d["opt_para"] = {"distribution": "laplace"}
    distribution_1_d["name"] = "distribution_1.gif"

    distribution_2_d["opt_para"] = {"distribution": "logistic"}
    distribution_2_d["name"] = "distribution_2.gif"

    distribution_10_d["opt_para"] = {"distribution": "normal"}
    distribution_10_d["name"] = "distribution_3.gif"

    distribution_11_d["opt_para"] = {"distribution": "laplace"}
    distribution_11_d["name"] = "distribution_4.gif"

    distribution_12_d["opt_para"] = {"distribution": "logistic"}
    distribution_12_d["name"] = "distribution_5.gif"

    search_path_gif(**distribution_0_d)
    search_path_gif(**distribution_1_d)
    search_path_gif(**distribution_2_d)

    search_path_gif(**distribution_10_d)
    search_path_gif(**distribution_11_d)
    search_path_gif(**distribution_12_d)


def generate_gifs_n_neighbours_():
    n_neighbours_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    n_neighbours_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    n_neighbours_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    n_neighbours_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    n_neighbours_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    n_neighbours_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    n_neighbours_0_d["opt_para"] = {"n_neighbours": 1}
    n_neighbours_0_d["name"] = "n_neighbours_0.gif"

    n_neighbours_1_d["opt_para"] = {"n_neighbours": 4}
    n_neighbours_1_d["name"] = "n_neighbours_1.gif"

    n_neighbours_2_d["opt_para"] = {"n_neighbours": 8}
    n_neighbours_2_d["name"] = "n_neighbours_2.gif"

    n_neighbours_10_d["opt_para"] = {"n_neighbours": 1}
    n_neighbours_10_d["name"] = "n_neighbours_3.gif"

    n_neighbours_11_d["opt_para"] = {"n_neighbours": 4}
    n_neighbours_11_d["name"] = "n_neighbours_4.gif"

    n_neighbours_12_d["opt_para"] = {"n_neighbours": 8}
    n_neighbours_12_d["name"] = "n_neighbours_5.gif"

    search_path_gif(**n_neighbours_0_d)
    search_path_gif(**n_neighbours_1_d)
    search_path_gif(**n_neighbours_2_d)

    search_path_gif(**n_neighbours_10_d)
    search_path_gif(**n_neighbours_11_d)
    search_path_gif(**n_neighbours_12_d)


def generate_gifs_p_accept_():
    p_accept_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    p_accept_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    p_accept_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    p_accept_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    p_accept_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    p_accept_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    p_accept_0_d["opt_para"] = {"p_accept": 1}
    p_accept_0_d["name"] = "p_accept_0.gif"

    p_accept_1_d["opt_para"] = {"p_accept": 4}
    p_accept_1_d["name"] = "p_accept_1.gif"

    p_accept_2_d["opt_para"] = {"p_accept": 8}
    p_accept_2_d["name"] = "p_accept_2.gif"

    p_accept_10_d["opt_para"] = {"p_accept": 1}
    p_accept_10_d["name"] = "p_accept_3.gif"

    p_accept_11_d["opt_para"] = {"p_accept": 4}
    p_accept_11_d["name"] = "p_accept_4.gif"

    p_accept_12_d["opt_para"] = {"p_accept": 8}
    p_accept_12_d["name"] = "p_accept_5.gif"

    search_path_gif(**p_accept_0_d)
    search_path_gif(**p_accept_1_d)
    search_path_gif(**p_accept_2_d)

    search_path_gif(**p_accept_10_d)
    search_path_gif(**p_accept_11_d)
    search_path_gif(**p_accept_12_d)


generate_gifs_epsilon_()
generate_gifs_distribution_()
generate_gifs_n_neighbours_()
generate_gifs_p_accept_()
