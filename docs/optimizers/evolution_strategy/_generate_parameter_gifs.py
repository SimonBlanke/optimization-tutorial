def warn(*args, **kwargs):
    pass


import os
import copy
import warnings

warnings.warn = warn


from gradient_free_optimizers import EvolutionStrategyOptimizer


from surfaces.test_functions import SphereFunction, AckleyFunction
from gradient_free_optimization_plots import search_path_gif


n_iter = 150
random_state = 0
optimizer_class = EvolutionStrategyOptimizer

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


def generate_gifs_mutation_rate_():
    mutation_rate_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    mutation_rate_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    mutation_rate_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    mutation_rate_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    mutation_rate_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    mutation_rate_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.1
    para2 = 0.5
    para3 = 0.9

    mutation_rate_0_d["opt_para"] = {"mutation_rate": para1}
    mutation_rate_0_d["name"] = "mutation_rate_0.gif"

    mutation_rate_1_d["opt_para"] = {"mutation_rate": para2}
    mutation_rate_1_d["name"] = "mutation_rate_1.gif"

    mutation_rate_2_d["opt_para"] = {"mutation_rate": para3}
    mutation_rate_2_d["name"] = "mutation_rate_2.gif"

    mutation_rate_10_d["opt_para"] = {"mutation_rate": para1}
    mutation_rate_10_d["name"] = "mutation_rate_3.gif"

    mutation_rate_11_d["opt_para"] = {"mutation_rate": para2}
    mutation_rate_11_d["name"] = "mutation_rate_4.gif"

    mutation_rate_12_d["opt_para"] = {"mutation_rate": para3}
    mutation_rate_12_d["name"] = "mutation_rate_5.gif"

    search_path_gif(**mutation_rate_0_d)
    search_path_gif(**mutation_rate_1_d)
    search_path_gif(**mutation_rate_2_d)

    search_path_gif(**mutation_rate_10_d)
    search_path_gif(**mutation_rate_11_d)
    search_path_gif(**mutation_rate_12_d)


def generate_gifs_crossover_rate_():
    crossover_rate_0_d = copy.copy(hill_climbing_sphere_function_template_d)
    crossover_rate_1_d = copy.copy(hill_climbing_sphere_function_template_d)
    crossover_rate_2_d = copy.copy(hill_climbing_sphere_function_template_d)

    crossover_rate_10_d = copy.copy(hill_climbing_ackley_function_template_d)
    crossover_rate_11_d = copy.copy(hill_climbing_ackley_function_template_d)
    crossover_rate_12_d = copy.copy(hill_climbing_ackley_function_template_d)

    para1 = 0.1
    para2 = 0.5
    para3 = 0.9

    crossover_rate_0_d["opt_para"] = {"crossover_rate": para1}
    crossover_rate_0_d["name"] = "crossover_rate_0.gif"

    crossover_rate_1_d["opt_para"] = {"crossover_rate": para2}
    crossover_rate_1_d["name"] = "crossover_rate_1.gif"

    crossover_rate_2_d["opt_para"] = {"crossover_rate": para3}
    crossover_rate_2_d["name"] = "crossover_rate_2.gif"

    crossover_rate_10_d["opt_para"] = {"crossover_rate": para1}
    crossover_rate_10_d["name"] = "crossover_rate_3.gif"

    crossover_rate_11_d["opt_para"] = {"crossover_rate": para2}
    crossover_rate_11_d["name"] = "crossover_rate_4.gif"

    crossover_rate_12_d["opt_para"] = {"crossover_rate": para3}
    crossover_rate_12_d["name"] = "crossover_rate_5.gif"

    search_path_gif(**crossover_rate_0_d)
    search_path_gif(**crossover_rate_1_d)
    search_path_gif(**crossover_rate_2_d)

    search_path_gif(**crossover_rate_10_d)
    search_path_gif(**crossover_rate_11_d)
    search_path_gif(**crossover_rate_12_d)


generate_gifs_population_()
generate_gifs_mutation_rate_()
generate_gifs_crossover_rate_()
