epsilon_d_ = {
    "epsilon": ["float", "0.03", "0.01 ... 0.3"],
}
distribution_d_ = {
    "distribution": ["string", "normal", "normal, laplace, logistic, gumbel"],
}
n_neighbours_d_ = {
    "n_neighbours": ["int", "3", "1 ... 10"],
}
p_accept_d_ = {
    "p_accept": ["float", "0.1", "0.01 ... 10"],
}
repulsion_factor_d = {
    "repulsion_factor": ["float", "5", "2 ... 10"],
}
annealing_rate_d = {
    "annealing_rate": ["float", "0.97", "0.9 ... 0.99"],
}
start_temp_d = {
    "start_temp": ["float", "1", "0.5 ... 1.5"],
}
alpha_d = {
    "alpha": ["float", "1", "0.5 ... 2"],
}
gamma_d = {
    "gamma": ["float", "2", "0.5 ... 5"],
}
beta_d = {
    "beta": ["float", "0.5", "0.25 ... 3"],
}
sigma_d = {
    "sigma": ["float", "0.5", "0.25 ... 3"],
}
step_size_d = {
    "step_size": ["int", "1", "1 ... 1000"],
}
n_iter_restart_d = {
    "n_iter_restart": ["int", "10", "5 ... 20"],
}
iters_p_dim_d = {
    "iters_p_dim": ["int", "10", "5 ... 15"],
}
n_positions_d = {
    "n_positions": ["int", "4", "2 ... 8"],
}
pattern_size_d = {
    "pattern_size": ["float", "0.25", "0.1 ... 0.5"],
}
reduction_d = {
    "reduction": ["float", "0.9", "0.75 ... 0.99"],
}
population_parallel_temp_d = {
    "population": ["int", "5", "3 ... 15"],
}
n_iter_swap_parallel_temp_d = {
    "n_iter_swap": ["int", "10", "5 ... 50"],
}
population_pso_d = {
    "population": ["int", "10", "4 ... 15"],
}
inertia_d = {
    "inertia": ["float", "0.5", "0.25 ... 0.75"],
}
cognitive_weight_d = {
    "cognitive_weight": ["float", "0.5", "0.25 ... 0.75"],
}
social_weight_d = {
    "social_weight": ["float", "0.5", "0.25 ... 0.75"],
}
temp_weight_d = {
    "temp_weight": ["float", "0.2", "0.05 ... 0.3"],
}
population_evo_strat_d = {
    "population": ["int", "10", "4 ... 15"],
}
mutation_rate_d = {
    "mutation_rate": ["float", "0.7", "0.1 ... 0.9"],
}
crossover_rate_d = {
    "crossover_rate": ["float", "0.3", "0.1 ... 0.9"],
}
gpr_bayes_opt_d = {
    "gpr": ["class", "0.3", "-"],
}
xi_bayes_opt_d = {
    "xi": ["float", "0.3", "0.1 ... 0.9"],
}
warm_start_smbo_d = {
    "warm_start_smbo": ["pandas dataframe", "None", "-"],
}
max_sample_size_d = {
    "max_sample_size": ["int", "10000000", "-"],
}
sampling_d = {
    "sampling": ["dict", "{'random': 1000000}", "-"],
}
gamma_tpe_d = {
    "gamma_tpe": ["float", "0.2", "0.05 ... 0.75"],
}
tree_regressor_d = {
    "tree_regressor": [
        "string",
        "extra_tree",
        "extra_tree, random_forest, gradient_boost",
    ],
}
tree_para_d = {
    "tree_para": ["dict", "{'n_estimators': 100}", "-"],
}
xi_forest_opt_d = {
    "xi": ["float", "0.03", "0.001 ... 0.1"],
}
