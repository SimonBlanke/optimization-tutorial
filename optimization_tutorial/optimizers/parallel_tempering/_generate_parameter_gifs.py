def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import ParallelTemperingOptimizer


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = ParallelTemperingOptimizer

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


def generate_gifs_population_():
    population_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    population_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    population_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    population_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    population_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    population_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 3
    para2 = 7
    para3 = 15

    population_0_d["opt_para"] = {"population": para1}
    population_0_d["name"] = "population_0.gif"

    population_1_d["opt_para"] = {"population": para2}
    population_1_d["name"] = "population_1.gif"

    population_2_d["opt_para"] = {"population": para3}
    population_2_d["name"] = "population_2.gif"

    population_10_d["opt_para"] = {"population": para1}
    population_10_d["name"] = "population_3.gif"

    population_11_d["opt_para"] = {"population": para2}
    population_11_d["name"] = "population_4.gif"

    population_12_d["opt_para"] = {"population": para3}
    population_12_d["name"] = "population_5.gif"

    search_path_gif(**population_0_d)
    search_path_gif(**population_1_d)
    search_path_gif(**population_2_d)

    search_path_gif(**population_10_d)
    search_path_gif(**population_11_d)
    search_path_gif(**population_12_d)


def generate_gifs_n_iter_swap_():
    n_iter_swap_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    n_iter_swap_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    n_iter_swap_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    n_iter_swap_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    n_iter_swap_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    n_iter_swap_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 5
    para2 = 8
    para3 = 15

    n_iter_swap_0_d["opt_para"] = {"n_iter_swap": para1}
    n_iter_swap_0_d["name"] = "n_iter_swap_0.gif"

    n_iter_swap_1_d["opt_para"] = {"n_iter_swap": para2}
    n_iter_swap_1_d["name"] = "n_iter_swap_1.gif"

    n_iter_swap_2_d["opt_para"] = {"n_iter_swap": para3}
    n_iter_swap_2_d["name"] = "n_iter_swap_2.gif"

    n_iter_swap_10_d["opt_para"] = {"n_iter_swap": para1}
    n_iter_swap_10_d["name"] = "n_iter_swap_3.gif"

    n_iter_swap_11_d["opt_para"] = {"n_iter_swap": para2}
    n_iter_swap_11_d["name"] = "n_iter_swap_4.gif"

    n_iter_swap_12_d["opt_para"] = {"n_iter_swap": para3}
    n_iter_swap_12_d["name"] = "n_iter_swap_5.gif"

    search_path_gif(**n_iter_swap_0_d)
    search_path_gif(**n_iter_swap_1_d)
    search_path_gif(**n_iter_swap_2_d)

    search_path_gif(**n_iter_swap_10_d)
    search_path_gif(**n_iter_swap_11_d)
    search_path_gif(**n_iter_swap_12_d)


generate_gifs_population_()
generate_gifs_n_iter_swap_()
