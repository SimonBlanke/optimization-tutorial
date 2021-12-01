# Hill Climbing

Hill climbing is a very basic optimization technique, that explores the search space only localy. It starts at an initial point, which is often chosen randomly and continues to move to positions with a better solution. It has no method against getting stuck in local optima.

**Available parameters:**
- epsilon
- distribution
- n_neighbours

---

**Use case/properties:**
- Never as a first method of optimization
- When you have a very good initial point to start from
- If the search space is very simple and has few local optima or saddle points

<p align="center">
<img src="./plots/search_paths/HillClimbing [('epsilon', 0.03)].png" width= 49%/>
<img src="./plots/search_paths/HillClimbing [('epsilon', 0.1)].png" width= 49%/>
</p>

<p align="center">
<img src="./plots/search_paths/HillClimbing [('distribution', 'laplace')].png" width= 49%/>
<img src="./plots/search_paths/HillClimbing [('distribution', 'logistic')].png" width= 49%/>
</p>

