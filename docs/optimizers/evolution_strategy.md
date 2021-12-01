# Evolution Strategy
Evolution strategy mutates and combines the best individuals of a population across a number of generations without transforming them into an array of bits (like genetic algorithms) but uses the real values of the positions.

**Available parameters:**
- individuals
- mutation_rate
- crossover_rate

---

**Use case/properties:**
- If the search space is very complex and large
- If you have enough time for many model evaluations

<p align="center">
<img src="./plots/search_paths/EvolutionStrategy [('individuals', 4)].png" width= 49%/>
<img src="./plots/search_paths/EvolutionStrategy [('individuals', 10)].png" width= 49%/>
<img src="./plots/search_paths/EvolutionStrategy [('individuals', 10), ('mutation_rate', 0.1), ('crossover_rate', 0.9)].png" width= 49%/>
<img src="./plots/search_paths/EvolutionStrategy [('individuals', 10), ('mutation_rate', 0.9), ('crossover_rate', 0.1)].png" width= 49%/>
</p>
