def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import DownhillSimplexOptimizer


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = DownhillSimplexOptimizer

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


def generate_gifs_alpha_():
    alpha_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    alpha_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    alpha_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    alpha_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    alpha_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    alpha_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.5
    para2 = 1.5
    para3 = 3

    alpha_0_d["opt_para"] = {"alpha": para1}
    alpha_0_d["name"] = "alpha_0.gif"

    alpha_1_d["opt_para"] = {"alpha": para2}
    alpha_1_d["name"] = "alpha_1.gif"

    alpha_2_d["opt_para"] = {"alpha": para3}
    alpha_2_d["name"] = "alpha_2.gif"

    alpha_10_d["opt_para"] = {"alpha": para1}
    alpha_10_d["name"] = "alpha_3.gif"

    alpha_11_d["opt_para"] = {"alpha": para2}
    alpha_11_d["name"] = "alpha_4.gif"

    alpha_12_d["opt_para"] = {"alpha": para3}
    alpha_12_d["name"] = "alpha_5.gif"

    search_path_gif(**alpha_0_d)
    search_path_gif(**alpha_1_d)
    search_path_gif(**alpha_2_d)

    search_path_gif(**alpha_10_d)
    search_path_gif(**alpha_11_d)
    search_path_gif(**alpha_12_d)


def generate_gifs_gamma_():
    gamma_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    gamma_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    gamma_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    gamma_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    gamma_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    gamma_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.5
    para2 = 1.5
    para3 = 3

    gamma_0_d["opt_para"] = {"gamma": para1}
    gamma_0_d["name"] = "gamma_0.gif"

    gamma_1_d["opt_para"] = {"gamma": para2}
    gamma_1_d["name"] = "gamma_1.gif"

    gamma_2_d["opt_para"] = {"gamma": para3}
    gamma_2_d["name"] = "gamma_2.gif"

    gamma_10_d["opt_para"] = {"gamma": para1}
    gamma_10_d["name"] = "gamma_3.gif"

    gamma_11_d["opt_para"] = {"gamma": para2}
    gamma_11_d["name"] = "gamma_4.gif"

    gamma_12_d["opt_para"] = {"gamma": para3}
    gamma_12_d["name"] = "gamma_5.gif"

    search_path_gif(**gamma_0_d)
    search_path_gif(**gamma_1_d)
    search_path_gif(**gamma_2_d)

    search_path_gif(**gamma_10_d)
    search_path_gif(**gamma_11_d)
    search_path_gif(**gamma_12_d)


def generate_gifs_beta_():
    beta_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    beta_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    beta_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    beta_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    beta_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    beta_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.5
    para2 = 2
    para3 = 5

    beta_0_d["opt_para"] = {"beta": para1}
    beta_0_d["name"] = "beta_0.gif"

    beta_1_d["opt_para"] = {"beta": para2}
    beta_1_d["name"] = "beta_1.gif"

    beta_2_d["opt_para"] = {"beta": para3}
    beta_2_d["name"] = "beta_2.gif"

    beta_10_d["opt_para"] = {"beta": para1}
    beta_10_d["name"] = "beta_3.gif"

    beta_11_d["opt_para"] = {"beta": para2}
    beta_11_d["name"] = "beta_4.gif"

    beta_12_d["opt_para"] = {"beta": para3}
    beta_12_d["name"] = "beta_5.gif"

    search_path_gif(**beta_0_d)
    search_path_gif(**beta_1_d)
    search_path_gif(**beta_2_d)

    search_path_gif(**beta_10_d)
    search_path_gif(**beta_11_d)
    search_path_gif(**beta_12_d)


def generate_gifs_sigma_():
    sigma_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    sigma_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    sigma_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    sigma_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    sigma_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    sigma_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.5
    para2 = 1.5
    para3 = 3

    sigma_0_d["opt_para"] = {"sigma": para1}
    sigma_0_d["name"] = "sigma_0.gif"

    sigma_1_d["opt_para"] = {"sigma": para2}
    sigma_1_d["name"] = "sigma_1.gif"

    sigma_2_d["opt_para"] = {"sigma": para3}
    sigma_2_d["name"] = "sigma_2.gif"

    sigma_10_d["opt_para"] = {"sigma": para1}
    sigma_10_d["name"] = "sigma_3.gif"

    sigma_11_d["opt_para"] = {"sigma": para2}
    sigma_11_d["name"] = "sigma_4.gif"

    sigma_12_d["opt_para"] = {"sigma": para3}
    sigma_12_d["name"] = "sigma_5.gif"

    search_path_gif(**sigma_0_d)
    search_path_gif(**sigma_1_d)
    search_path_gif(**sigma_2_d)

    search_path_gif(**sigma_10_d)
    search_path_gif(**sigma_11_d)
    search_path_gif(**sigma_12_d)


generate_gifs_alpha_()
generate_gifs_gamma_()
generate_gifs_beta_()
generate_gifs_sigma_()
