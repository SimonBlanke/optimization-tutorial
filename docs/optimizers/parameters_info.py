epsilon_intro_ = """ 
When climbing to new positions `epsilon` determines how far the hill climbing based algorithm jumps 
from one position to the next points. A higher `epsilon` leads to longer jumps.

In a normal-`distribution` the `epsilon` parameter would correspond to the standard deviation.
"""
distribution_intro_ = """ 
The mathematical `distribution` the algorithm draws samples from.

The distributions can be found in the [numpy documentation](https://numpy.org/doc/1.16/reference/routines.random.html)
"""
n_neighbours_intro_ = """ 
The number of positions the algorithm explores from its current postion 
before jumping to the best one.
"""
p_accept_intro_ = """ 
...
"""
repulsion_factor_intro_ = """
If the algorithm does not find a better position the 
repulsion factor increases epsilon for the next jump.
"""
annealing_rate_intro_ = """
Rate at which the temperatur-value of the algorithm decreases. An annealing 
rate above 1 increases the temperature over time.
"""
start_temp_intro_ = """
The start temperatur determines the probability for the algorithm to jump to a worse position.
"""
alpha_intro_ = """
Reflection parameter of the simplex algorithm.
"""
gamma_intro_ = """
Expansion parameter of the simplex algorithm.
"""
beta_intro_ = """
Contraction parameter of the simplex algorithm.
"""
sigma_intro_ = """
Shrinking parameter of the simplex algorithm.
"""
step_size_intro_ = """
The number of steps the grid search takes after each iteration. If this parameter is 
set to 3 the grid search won't select the next position, but the one it would normally
select after 3 iterations. This way we get a sparse grid after the first pass through
the search space. After the first pass is done the grid search starts at the beginning
and does a second pass with the same step size. And a third pass after that.
"""
n_iter_restart_intro_ = """
The number of iterations the algorithm performs before jumping to a random position.
"""
iters_p_dim_intro_ = """
Number of iterations per dimension of the search space.
"""
n_positions_intro_ = """
Number of positions that the pattern contains.
"""
pattern_size_intro_ = """
Size of the patterns in percentage of the size of the search space in the corresponding dimension.
"""
reduction_intro_ = """
Factor to change the size of the pattern when no better position is found.
"""
n_iter_swap_intro_ = """
The number of iterations the algorithm performs before switching 
temperatures of the individual optimizers in the population.
"""
population_intro_ = """
Size of the population for population-based optimization algorithms.
"""
inertia_intro_ = """
The inertia of the movement of the individual optimizers in the population.
"""
cognitive_weight_intro_ = """
A factor of the movement towards the personal best position 
of the individual optimizers in the population.
"""
social_weight_intro_ = """
A factor of the movement towards the global best 
position of the individual optimizers in the population.
"""
mutation_rate_intro_ = """
Probability of an individual in the population to perform an hill climbing step.
"""
crossover_rate_intro_ = """
Probability of an individual to perform a crossover with the best individual in the population.
"""
gpr_intro_ = """
The access to the surrogate model class. Example 
surrogate model classes can be found in a separate repository.
"""
xi_intro_ = """
Parameter for the expected uncertainty of the estimation.
"""
warm_start_smbo_intro_ = """
Dataframe that contains the search data of a previous optimization run.
"""
gamma_tpe_intro_ = """
Separates the explored positions into good and bad.
"""
tree_regressor_intro_ = """
The access to the surrogate model class. Example surrogate
model classes can be found in a separate repository.
"""
