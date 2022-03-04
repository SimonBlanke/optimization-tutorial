def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import GridSearchOptimizer


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = GridSearchOptimizer

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


def generate_gifs_step_size_():
    step_size_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    step_size_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    step_size_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    step_size_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    step_size_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    step_size_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 3
    para2 = 25
    para3 = 120

    step_size_0_d["opt_para"] = {"step_size": para1}
    step_size_0_d["name"] = "step_size_0.gif"

    step_size_1_d["opt_para"] = {"step_size": para2}
    step_size_1_d["name"] = "step_size_1.gif"

    step_size_2_d["opt_para"] = {"step_size": para3}
    step_size_2_d["name"] = "step_size_2.gif"

    step_size_10_d["opt_para"] = {"step_size": para1}
    step_size_10_d["name"] = "step_size_3.gif"

    step_size_11_d["opt_para"] = {"step_size": para2}
    step_size_11_d["name"] = "step_size_4.gif"

    step_size_12_d["opt_para"] = {"step_size": para3}
    step_size_12_d["name"] = "step_size_5.gif"

    search_path_gif(**step_size_0_d)
    search_path_gif(**step_size_1_d)
    search_path_gif(**step_size_2_d)

    search_path_gif(**step_size_10_d)
    search_path_gif(**step_size_11_d)
    search_path_gif(**step_size_12_d)


generate_gifs_step_size_()
