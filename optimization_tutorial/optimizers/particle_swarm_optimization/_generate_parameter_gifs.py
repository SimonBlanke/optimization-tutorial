def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import ParticleSwarmOptimizer


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = ParticleSwarmOptimizer

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


def generate_gifs_inertia_():
    inertia_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    inertia_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    inertia_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    inertia_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    inertia_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    inertia_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.25
    para2 = 0.6
    para3 = 0.75

    inertia_0_d["opt_para"] = {"inertia": para1}
    inertia_0_d["name"] = "inertia_0.gif"

    inertia_1_d["opt_para"] = {"inertia": para2}
    inertia_1_d["name"] = "inertia_1.gif"

    inertia_2_d["opt_para"] = {"inertia": para3}
    inertia_2_d["name"] = "inertia_2.gif"

    inertia_10_d["opt_para"] = {"inertia": para1}
    inertia_10_d["name"] = "inertia_3.gif"

    inertia_11_d["opt_para"] = {"inertia": para2}
    inertia_11_d["name"] = "inertia_4.gif"

    inertia_12_d["opt_para"] = {"inertia": para3}
    inertia_12_d["name"] = "inertia_5.gif"

    search_path_gif(**inertia_0_d)
    search_path_gif(**inertia_1_d)
    search_path_gif(**inertia_2_d)

    search_path_gif(**inertia_10_d)
    search_path_gif(**inertia_11_d)
    search_path_gif(**inertia_12_d)


def generate_gifs_cognitive_weight_():
    cognitive_weight_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    cognitive_weight_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    cognitive_weight_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    cognitive_weight_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    cognitive_weight_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    cognitive_weight_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.25
    para2 = 0.6
    para3 = 0.75

    cognitive_weight_0_d["opt_para"] = {"cognitive_weight": para1}
    cognitive_weight_0_d["name"] = "cognitive_weight_0.gif"

    cognitive_weight_1_d["opt_para"] = {"cognitive_weight": para2}
    cognitive_weight_1_d["name"] = "cognitive_weight_1.gif"

    cognitive_weight_2_d["opt_para"] = {"cognitive_weight": para3}
    cognitive_weight_2_d["name"] = "cognitive_weight_2.gif"

    cognitive_weight_10_d["opt_para"] = {"cognitive_weight": para1}
    cognitive_weight_10_d["name"] = "cognitive_weight_3.gif"

    cognitive_weight_11_d["opt_para"] = {"cognitive_weight": para2}
    cognitive_weight_11_d["name"] = "cognitive_weight_4.gif"

    cognitive_weight_12_d["opt_para"] = {"cognitive_weight": para3}
    cognitive_weight_12_d["name"] = "cognitive_weight_5.gif"

    search_path_gif(**cognitive_weight_0_d)
    search_path_gif(**cognitive_weight_1_d)
    search_path_gif(**cognitive_weight_2_d)

    search_path_gif(**cognitive_weight_10_d)
    search_path_gif(**cognitive_weight_11_d)
    search_path_gif(**cognitive_weight_12_d)


def generate_gifs_social_weight_():
    social_weight_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    social_weight_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    social_weight_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    social_weight_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    social_weight_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    social_weight_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.25
    para2 = 0.6
    para3 = 0.75

    social_weight_0_d["opt_para"] = {"social_weight": para1}
    social_weight_0_d["name"] = "social_weight_0.gif"

    social_weight_1_d["opt_para"] = {"social_weight": para2}
    social_weight_1_d["name"] = "social_weight_1.gif"

    social_weight_2_d["opt_para"] = {"social_weight": para3}
    social_weight_2_d["name"] = "social_weight_2.gif"

    social_weight_10_d["opt_para"] = {"social_weight": para1}
    social_weight_10_d["name"] = "social_weight_3.gif"

    social_weight_11_d["opt_para"] = {"social_weight": para2}
    social_weight_11_d["name"] = "social_weight_4.gif"

    social_weight_12_d["opt_para"] = {"social_weight": para3}
    social_weight_12_d["name"] = "social_weight_5.gif"

    search_path_gif(**social_weight_0_d)
    search_path_gif(**social_weight_1_d)
    search_path_gif(**social_weight_2_d)

    search_path_gif(**social_weight_10_d)
    search_path_gif(**social_weight_11_d)
    search_path_gif(**social_weight_12_d)


generate_gifs_population_()
generate_gifs_inertia_()
generate_gifs_cognitive_weight_()
generate_gifs_social_weight_()
