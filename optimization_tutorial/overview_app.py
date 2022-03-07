import os
import streamlit as st

import pandas as pd

here_ = os.path.dirname(os.path.realpath(__file__))


about_ = """
This tutorial describes the optimization strategies 
and parameters from the [Hyperactive](https://github.com/SimonBlanke/Hyperactive) and 
[Gradient-Free-Optimizers](https://github.com/SimonBlanke/Gradient-Free-Optimizers) 
python-packages.
All optimizer- and parameter-names correspond 
to version 1.0 of Gradient-Free-Optimizers. 

The default-paramters 
and algorithm behaviour may change across 
[minor versions](https://semver.org/) of Gradient-Free-Optimizers.
Select the minor/major version of Gradient-Free-Optimizers in the 
selectbox and the documentation will change 
accordingly.
"""

introduction_ = """
...
"""


hill_climbing_d = {
    "Hill Climbing": ["+", "x", "o", "x"],
}

stochastic_hill_climbing_d = {
    "Stochastic Hill Climbing": ["o", "o", "+", "x"],
}
repulsing_hill_climbing_d = {
    "Repulsing Hill Climbing": ["o", "o", "+", "x"],
}
simulated_annealing_d = {
    "Simulted Annealing": ["o", "+", "x", "x"],
}
downhill_simplex_d = {
    "Downhill Simplex": ["+", "o", "o", "x"],
}
random_search_d = {
    "Random Search": ["o", "o", "o", "o"],
}
grid_search_d = {
    "Grid Search": ["o", "o", "o", "o"],
}
random_restart_hill_climbing_d = {
    "Random Restart Hill Climbing": ["+", "o", "+", "x"],
}
powells_method_d = {
    "Powell's Method": ["+", "o", "o", "o"],
}
pattern_search = {
    "Pattern Search": ["+", "o", "o", "o"],
}
random_annealing = {
    "Random Annealing": ["+", "o", "+", "x"],
}
parallel_tempering_d = {
    "Parallel Tempering": ["o", "+", "o", "x"],
}
particle_swarm_d = {
    "Particle Swarm Optimization": ["+", "o", "o", "o"],
}
evolution_strategy_d = {
    "Evolution Strategy": ["o", "+", "+", "o"],
}
bayesian_opt_d = {
    "Bayesian Optimization": ["x", "x", "+", "+"],
}
tpe_d = {
    "Tree Structured Parzen Estimators": ["x", "x", "o", "+"],
}
foest_opt_d = {
    "Forest Optimizer": ["x", "x", "o", "+"],
}


algo_d = dict()
algo_d.update(hill_climbing_d)
algo_d.update(stochastic_hill_climbing_d)
algo_d.update(repulsing_hill_climbing_d)
algo_d.update(downhill_simplex_d)
algo_d.update(random_search_d)
algo_d.update(grid_search_d)
algo_d.update(random_restart_hill_climbing_d)
algo_d.update(powells_method_d)
algo_d.update(pattern_search)
algo_d.update(random_annealing)
algo_d.update(parallel_tempering_d)
algo_d.update(particle_swarm_d)
algo_d.update(evolution_strategy_d)
algo_d.update(bayesian_opt_d)
algo_d.update(tpe_d)
algo_d.update(foest_opt_d)


color_d = {
    "+": "green",
    "o": "blue",
    "x": "red",
}

size_d = {
    "+": "15",
    "o": "15",
    "x": "15",
}


def algo_color(val):
    color = color_d[val]
    size = size_d[val]

    return f"color: {color}; font-size: {size}pt; font-weight: bold;"


def overview_app():
    st.title("Overview")
    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )

    st.header("About this tutorial")
    col1, col2, col3 = st.columns((2, 1, 1))
    col1.write(about_)

    # col2.image(os.path.join(here_, "_images", "optimizer_table.png"))
    # col3.image(os.path.join(here_, "_images", "optimizer_table.png"))

    st.header("Introduction")
    col1, col2 = st.columns((1, 1.5))

    algo_table = pd.DataFrame.from_dict(
        algo_d,
        orient="index",
        columns=(
            "Convex Functions",
            "Non-convex Functions",
            "Machine Learning",
            "Deep Learning",
        ),
    )

    algo_table = algo_table.style.applymap(algo_color)

    col1.write(introduction_)
    col2.table(algo_table)

    # col2.image(os.path.join(here_, "_images", "optimizer_table.png"))
