# Random Annealing

An algorithm that chooses a new position within a large hypersphere around the current position. This hypersphere gets smaller over time.

**Available parameters:**
- epsilon
- distribution
- n_neighbours
- start_temp
- annealing_rate

---

**Use case/properties:**
- Disclaimer: I have not seen this algorithm before, but invented it myself. It seems to be a good alternative to the other random algorithms
- Good as a first method of optimization
- For a short optimization run to get an acceptable solution

<p align="center">
<img src="./plots/search_paths/RandomAnnealing [('epsilon_mod', 3)].png" width= 49%/>
<img src="./plots/search_paths/RandomAnnealing [('epsilon_mod', 10)].png" width= 49%/>
<img src="./plots/search_paths/RandomAnnealing [('epsilon_mod', 25)].png" width= 49%/>
<img src="./plots/search_paths/RandomAnnealing [('epsilon_mod', 25), ('annealing_rate', 0.9)].png" width= 49%/>
</p>
