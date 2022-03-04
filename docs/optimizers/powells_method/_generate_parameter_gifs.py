def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import PowellsMethod


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = PowellsMethod

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


def generate_gifs_iters_p_dim_():
    iters_p_dim_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    iters_p_dim_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    iters_p_dim_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    iters_p_dim_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    iters_p_dim_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    iters_p_dim_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 5
    para2 = 8
    para3 = 15

    iters_p_dim_0_d["opt_para"] = {"iters_p_dim": para1}
    iters_p_dim_0_d["name"] = "iters_p_dim_0.gif"

    iters_p_dim_1_d["opt_para"] = {"iters_p_dim": para2}
    iters_p_dim_1_d["name"] = "iters_p_dim_1.gif"

    iters_p_dim_2_d["opt_para"] = {"iters_p_dim": para3}
    iters_p_dim_2_d["name"] = "iters_p_dim_2.gif"

    iters_p_dim_10_d["opt_para"] = {"iters_p_dim": para1}
    iters_p_dim_10_d["name"] = "iters_p_dim_3.gif"

    iters_p_dim_11_d["opt_para"] = {"iters_p_dim": para2}
    iters_p_dim_11_d["name"] = "iters_p_dim_4.gif"

    iters_p_dim_12_d["opt_para"] = {"iters_p_dim": para3}
    iters_p_dim_12_d["name"] = "iters_p_dim_5.gif"

    search_path_gif(**iters_p_dim_0_d)
    search_path_gif(**iters_p_dim_1_d)
    search_path_gif(**iters_p_dim_2_d)

    search_path_gif(**iters_p_dim_10_d)
    search_path_gif(**iters_p_dim_11_d)
    search_path_gif(**iters_p_dim_12_d)


generate_gifs_iters_p_dim_()
