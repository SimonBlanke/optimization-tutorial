def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import ForestOptimizer


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = ForestOptimizer

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


def generate_gifs_xi_():
    xi_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    xi_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    xi_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    xi_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    xi_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    xi_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.1
    para2 = 0.5
    para3 = 0.9

    xi_0_d["opt_para"] = {"xi": para1}
    xi_0_d["name"] = "xi_0.gif"

    xi_1_d["opt_para"] = {"xi": para2}
    xi_1_d["name"] = "xi_1.gif"

    xi_2_d["opt_para"] = {"xi": para3}
    xi_2_d["name"] = "xi_2.gif"

    xi_10_d["opt_para"] = {"xi": para1}
    xi_10_d["name"] = "xi_3.gif"

    xi_11_d["opt_para"] = {"xi": para2}
    xi_11_d["name"] = "xi_4.gif"

    xi_12_d["opt_para"] = {"xi": para3}
    xi_12_d["name"] = "xi_5.gif"

    search_path_gif(**xi_0_d)
    search_path_gif(**xi_1_d)
    search_path_gif(**xi_2_d)

    search_path_gif(**xi_10_d)
    search_path_gif(**xi_11_d)
    search_path_gif(**xi_12_d)


generate_gifs_xi_()
