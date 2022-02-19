import streamlit as st

st.set_page_config(page_title="Optimization Tutorial", layout="wide")

st.markdown(
    """
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 5rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 0rem;
                    padding-right: 1rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)


from overview_app import overview_app
from optimizers import (
    hill_climbing_app,
    stochastic_hill_climbing_app,
    repulsing_hill_climbing_app,
    simulated_annealing_app,
    downhill_simplex_app,
    random_search_app,
    grid_search_app,
    random_restart_hill_climbing_app,
    powells_method_app,
    pattern_search_app,
    random_annealing_app,
    parallel_tempering_app,
    parallel_random_annealing_app,
    particle_swarm_optimization_app,
    evolution_strategy_app,
    bayesian_optimization_app,
    tree_structured_parzen_estimators_app,
    forest_optimization_app,
)

app_d = {
    "Hill Climbing Optimizer": hill_climbing_app,
    "Stochastic Hill Climbing Optimizer": stochastic_hill_climbing_app,
    "Repulsing Hill Climbing Optimizer": repulsing_hill_climbing_app,
    "Simulated Annealing Optimizer": simulated_annealing_app,
    "Downhill Simplex Optimizer": downhill_simplex_app,
    "Random Search Optimizer": random_search_app,
    "GridSearch Optimizer": grid_search_app,
    "Random Restart Hill Climbing Optimizer": random_restart_hill_climbing_app,
    "Powell's Method": powells_method_app,
    "Pattern Search": pattern_search_app,
    "Random Annealing Optimizer": random_annealing_app,
    "Parallel Tempering Optimizer": parallel_tempering_app,
    "Parallel Annealing Optimizer": parallel_random_annealing_app,
    "Particle Swarm Optimizer": particle_swarm_optimization_app,
    "Evolution Strategy Optimizer": evolution_strategy_app,
    "Bayesian Optimizer": bayesian_optimization_app,
    "Tree Structured Parzen Estimators": tree_structured_parzen_estimators_app,
    "Forest Optimizer": forest_optimization_app,
}


choice_0 = st.sidebar.radio(" ", options=("Overview", "Optimizer Infos"), index=0)

if choice_0 == "Overview":
    overview_app()
elif choice_0 == "Optimizer Infos":
    st.sidebar.write("")
    choice_opt = st.sidebar.radio("Optimization Algorithms:", options=app_d, index=0)
    app_d[choice_opt]()
