def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import TreeStructuredParzenEstimators


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = TreeStructuredParzenEstimators

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


def generate_gifs_gamma_tpe_():
    gamma_tpe_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    gamma_tpe_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    gamma_tpe_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    gamma_tpe_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    gamma_tpe_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    gamma_tpe_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.05
    para2 = 0.1
    para3 = 0.75

    gamma_tpe_0_d["opt_para"] = {"gamma_tpe": para1}
    gamma_tpe_0_d["name"] = "gamma_tpe_0.gif"

    gamma_tpe_1_d["opt_para"] = {"gamma_tpe": para2}
    gamma_tpe_1_d["name"] = "gamma_tpe_1.gif"

    gamma_tpe_2_d["opt_para"] = {"gamma_tpe": para3}
    gamma_tpe_2_d["name"] = "gamma_tpe_2.gif"

    gamma_tpe_10_d["opt_para"] = {"gamma_tpe": para1}
    gamma_tpe_10_d["name"] = "gamma_tpe_3.gif"

    gamma_tpe_11_d["opt_para"] = {"gamma_tpe": para2}
    gamma_tpe_11_d["name"] = "gamma_tpe_4.gif"

    gamma_tpe_12_d["opt_para"] = {"gamma_tpe": para3}
    gamma_tpe_12_d["name"] = "gamma_tpe_5.gif"

    search_path_gif(**gamma_tpe_0_d)
    search_path_gif(**gamma_tpe_1_d)
    search_path_gif(**gamma_tpe_2_d)

    search_path_gif(**gamma_tpe_10_d)
    search_path_gif(**gamma_tpe_11_d)
    search_path_gif(**gamma_tpe_12_d)


generate_gifs_gamma_tpe_()
