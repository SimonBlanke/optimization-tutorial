## Tabu Search

Tabu search is a metaheuristic method, that explores new positions like hill climbing but memorizes previous positions and avoids those. This helps finding new trajectories through the search space.

**Available parameters:**
- epsilon
- distribution
- n_neighbours
- tabu_memory

---

**Use case/properties:**
- When you have a good initial point to start from

<p align="center">
<img src="./plots/search_paths/TabuSearch [('tabu_memory', 1)].png" width= 49%/>
<img src="./plots/search_paths/TabuSearch [('tabu_memory', 3)].png" width= 49%/>
</p>

<p align="center">
<img src="./plots/search_paths/TabuSearch [('tabu_memory', 10)].png" width= 49%/>
<img src="./plots/search_paths/TabuSearch [('tabu_memory', 3), ('epsilon', 0.1)].png" width= 49%/>
</p>
