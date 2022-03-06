def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import PatternSearch


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = PatternSearch

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


def generate_gifs_n_positions_():
    n_positions_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    n_positions_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    n_positions_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    n_positions_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    n_positions_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    n_positions_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 2
    para2 = 5
    para3 = 8

    n_positions_0_d["opt_para"] = {"n_positions": para1}
    n_positions_0_d["name"] = "n_positions_0.gif"

    n_positions_1_d["opt_para"] = {"n_positions": para2}
    n_positions_1_d["name"] = "n_positions_1.gif"

    n_positions_2_d["opt_para"] = {"n_positions": para3}
    n_positions_2_d["name"] = "n_positions_2.gif"

    n_positions_10_d["opt_para"] = {"n_positions": para1}
    n_positions_10_d["name"] = "n_positions_3.gif"

    n_positions_11_d["opt_para"] = {"n_positions": para2}
    n_positions_11_d["name"] = "n_positions_4.gif"

    n_positions_12_d["opt_para"] = {"n_positions": para3}
    n_positions_12_d["name"] = "n_positions_5.gif"

    search_path_gif(**n_positions_0_d)
    search_path_gif(**n_positions_1_d)
    search_path_gif(**n_positions_2_d)

    search_path_gif(**n_positions_10_d)
    search_path_gif(**n_positions_11_d)
    search_path_gif(**n_positions_12_d)


def generate_gifs_pattern_size_():
    pattern_size_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    pattern_size_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    pattern_size_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    pattern_size_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    pattern_size_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    pattern_size_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.1
    para2 = 0.3
    para3 = 0.5

    pattern_size_0_d["opt_para"] = {"pattern_size": para1}
    pattern_size_0_d["name"] = "pattern_size_0.gif"

    pattern_size_1_d["opt_para"] = {"pattern_size": para2}
    pattern_size_1_d["name"] = "pattern_size_1.gif"

    pattern_size_2_d["opt_para"] = {"pattern_size": para3}
    pattern_size_2_d["name"] = "pattern_size_2.gif"

    pattern_size_10_d["opt_para"] = {"pattern_size": para1}
    pattern_size_10_d["name"] = "pattern_size_3.gif"

    pattern_size_11_d["opt_para"] = {"pattern_size": para2}
    pattern_size_11_d["name"] = "pattern_size_4.gif"

    pattern_size_12_d["opt_para"] = {"pattern_size": para3}
    pattern_size_12_d["name"] = "pattern_size_5.gif"

    search_path_gif(**pattern_size_0_d)
    search_path_gif(**pattern_size_1_d)
    search_path_gif(**pattern_size_2_d)

    search_path_gif(**pattern_size_10_d)
    search_path_gif(**pattern_size_11_d)
    search_path_gif(**pattern_size_12_d)


def generate_gifs_reduction_():
    reduction_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    reduction_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    reduction_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    reduction_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    reduction_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    reduction_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.75
    para2 = 0.8
    para3 = 0.99

    reduction_0_d["opt_para"] = {"reduction": para1}
    reduction_0_d["name"] = "reduction_0.gif"

    reduction_1_d["opt_para"] = {"reduction": para2}
    reduction_1_d["name"] = "reduction_1.gif"

    reduction_2_d["opt_para"] = {"reduction": para3}
    reduction_2_d["name"] = "reduction_2.gif"

    reduction_10_d["opt_para"] = {"reduction": para1}
    reduction_10_d["name"] = "reduction_3.gif"

    reduction_11_d["opt_para"] = {"reduction": para2}
    reduction_11_d["name"] = "reduction_4.gif"

    reduction_12_d["opt_para"] = {"reduction": para3}
    reduction_12_d["name"] = "reduction_5.gif"

    search_path_gif(**reduction_0_d)
    search_path_gif(**reduction_1_d)
    search_path_gif(**reduction_2_d)

    search_path_gif(**reduction_10_d)
    search_path_gif(**reduction_11_d)
    search_path_gif(**reduction_12_d)


generate_gifs_n_positions_()
generate_gifs_pattern_size_()
generate_gifs_reduction_()
