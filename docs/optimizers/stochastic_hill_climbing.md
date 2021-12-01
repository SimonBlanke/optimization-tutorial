# Stochastic Hill Climbing
Stochastic hill climbing extends the normal hill climbing by a simple method against getting stuck in local optima. It has a parameter you can set, that determines the probability to accept worse solutions as a next position.

**Available parameters:**
- epsilon
- distribution
- n_neighbours
- p_down

---

**Use case/properties:**
- Never as a first method of optimization
- When you have a very good initial point to start from

<p align="center">
<img src="./plots/search_paths/StochasticHillClimbing [('p_down', 0.1)].png" width= 49%/>
<img src="./plots/search_paths/StochasticHillClimbing [('p_down', 0.3)].png" width= 49%/>
</p>

<p align="center">
<img src="./plots/search_paths/StochasticHillClimbing [('p_down', 0.5)].png" width= 49%/>
<img src="./plots/search_paths/StochasticHillClimbing [('p_down', 0.9)].png" width= 49%/>
</p>
