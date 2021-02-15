<h1 align="center"> 
  Optimization Tutorial
</h1>

This tutorial describes the optimization strategies and paramters from the Hyperactive and Gradient-Free-Optimization python-packages. 

<br>

## Overview

The following table shows the expected results for each optimization strategy for the given type of problems:

    - Convex function with fast evaluation time (<0.1s)
    - Non-convex function with fast evaluation time (<0.1s)
    - Machine learning model hyperparameter optimization
    - Deep learning model hyperparameter optimization

<p align="center">
  <br>
  <img src="./docs/_images/optimizer_table-1.png" width="950">
  <br>
</p>
Those recomendations are just estimated based on personal experience and can heavily change dependend on optimization parameters, exact type of problem and number of iterations.


<br>

## Optimizer Classes and Parameters

<details>
<summary><b> HillClimbingOptimizer</b></summary>

    - epsilon=0.05
    - distribution="normal"
    - n_neighbours=3
    - rand_rest_p=0.03

</details>

<details>
<summary><b> RepulsingHillClimbingOptimizer</b></summary>

    - epsilon=0.05
    - distribution="normal"
    - n_neighbours=3
    - rand_rest_p=0.03
    - repulsion_factor=3

</details>

<details>
<summary><b> SimulatedAnnealingOptimizer</b></summary>

    - epsilon=0.05
    - distribution="normal"
    - n_neighbours=3
    - rand_rest_p=0.03
    - p_accept=0.1
    - norm_factor=1
    - annealing_rate=0.975
    - start_temp=1

</details>

<details>
<summary><b> RandomSearchOptimizer</b></summary>

</details>

<details>
<summary><b> RandomRestartHillClimbingOptimizer</b></summary>

    - epsilon=0.05
    - distribution="normal"
    - n_neighbours=3
    - rand_rest_p=0.03
    - n_iter_restart=10

</details>

<details>
<summary><b> RandomAnnealingOptimizer</b></summary>

    - epsilon=0.05
    - distribution="normal"
    - n_neighbours=3
    - rand_rest_p=0.03
    - annealing_rate=0.975
    - start_temp=1

</details>

<details>
<summary><b> ParallelTemperingOptimizer</b></summary>

    - n_iter_swap=10
    - rand_rest_p=0.03

</details>

<details>
<summary><b> ParticleSwarmOptimizer</b></summary>

    - inertia=0.5
    - cognitive_weight=0.5
    - social_weight=0.5
    - temp_weight=0.2
    - rand_rest_p=0.03

</details>

<details>
<summary><b> EvolutionStrategyOptimizer</b></summary>

    - mutation_rate=0.7
    - crossover_rate=0.3
    - rand_rest_p=0.03

</details>

<details>
<summary><b> BayesianOptimizer</b></summary>

    - gpr=gaussian_process["gp_nonlinear"]
    - xi=0.03
    - warm_start_smbo=None
    - rand_rest_p=0.03

</details>

<details>
<summary><b> TreeStructuredParzenEstimators</b></summary>

    - gamma_tpe=0.5
    - warm_start_smbo=None
    - rand_rest_p=0.03

</details>

<details>
<summary><b> DecisionTreeOptimizer</b></summary>

    - tree_regressor="extra_tree"
    - xi=0.01
    - warm_start_smbo=None
    - rand_rest_p=0.03

</details>

