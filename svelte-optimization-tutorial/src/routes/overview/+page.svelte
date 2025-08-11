<script>
  const optimizers = [
    {
      name: "Hill Climbing",
      category: "Local Search",
      convexFast: "❌",
      nonConvexFast: "⚠️",
      mlHyperparams: "❌", 
      dlHyperparams: "❌",
      description: "Simple local search that moves to better neighbors",
      parameters: ["epsilon", "distribution", "n_neighbours"],
      strengths: ["Fast execution", "Simple implementation"],
      weaknesses: ["Gets stuck in local optima", "No global search capability"],
      path: "/optimizers/hill-climbing"
    },
    {
      name: "Simulated Annealing",
      category: "Local Search",
      convexFast: "✅",
      nonConvexFast: "✅",
      mlHyperparams: "⚠️",
      dlHyperparams: "❌",
      description: "Hill climbing with temperature-based acceptance of worse solutions",
      parameters: ["epsilon", "distribution", "annealing_rate", "start_temp"],
      strengths: ["Escapes local optima", "Good for complex landscapes"],
      weaknesses: ["Requires parameter tuning", "Can be slow to converge"],
      path: "/optimizers/simulated-annealing"
    },
    {
      name: "Random Search",
      category: "Global Search", 
      convexFast: "⚠️",
      nonConvexFast: "✅",
      mlHyperparams: "✅",
      dlHyperparams: "✅",
      description: "Purely random exploration of the search space",
      parameters: [],
      strengths: ["Unbiased exploration", "No local optima issues", "Good baseline"],
      weaknesses: ["Inefficient", "No learning from history"],
      path: "/optimizers/random-search"
    },
    {
      name: "Grid Search",
      category: "Global Search",
      convexFast: "✅",
      nonConvexFast: "⚠️", 
      mlHyperparams: "✅",
      dlHyperparams: "❌",
      description: "Systematic exploration following a grid pattern",
      parameters: ["step_size"],
      strengths: ["Complete coverage", "Reproducible", "Good for low dimensions"],
      weaknesses: ["Curse of dimensionality", "Inefficient for continuous spaces"],
      path: "/optimizers/grid-search"
    },
    {
      name: "Particle Swarm Optimization",
      category: "Population-based",
      convexFast: "✅",
      nonConvexFast: "✅",
      mlHyperparams: "✅",
      dlHyperparams: "⚠️",
      description: "Population-based optimization inspired by swarm behavior",
      parameters: ["population", "inertia", "cognitive_weight", "social_weight"],
      strengths: ["Good global search", "Parallelizable", "Works well with continuous spaces"],
      weaknesses: ["Many parameters to tune", "Can converge prematurely"],
      path: "/optimizers/particle-swarm-optimization"
    },
    {
      name: "Evolution Strategy",
      category: "Population-based",
      convexFast: "⚠️",
      nonConvexFast: "✅",
      mlHyperparams: "✅",
      dlHyperparams: "✅",
      description: "Evolutionary algorithm using real-valued representations",
      parameters: ["population", "mutation_rate", "crossover_rate"],
      strengths: ["Robust global search", "Good for noisy functions", "Self-adaptive"],
      weaknesses: ["Computationally expensive", "Slow convergence"],
      path: "/optimizers/evolution-strategy"
    },
    {
      name: "Bayesian Optimization",
      category: "Model-based",
      convexFast: "⚠️",
      nonConvexFast: "⚠️",
      mlHyperparams: "✅",
      dlHyperparams: "✅",
      description: "Model-based optimization using Gaussian processes",
      parameters: ["xi", "gpr"],
      strengths: ["Sample efficient", "Principled uncertainty", "Good for expensive functions"],
      weaknesses: ["Limited scalability", "GP training overhead"],
      path: "/optimizers/bayesian-optimization"
    },
    {
      name: "Tree-structured Parzen Estimators",
      category: "Model-based", 
      convexFast: "⚠️",
      nonConvexFast: "⚠️",
      mlHyperparams: "✅",
      dlHyperparams: "✅",
      description: "Sequential model-based optimization using kernel density estimation",
      parameters: ["gamma_tpe"],
      strengths: ["Sample efficient", "Works with discrete variables", "Less GP overhead"],
      weaknesses: ["Can get stuck in local regions", "Hyperparameter sensitive"],
      path: "/optimizers/tree-structured-parzen-estimators"
    }
  ];

  const problemTypes = [
    {
      name: "Convex function with fast evaluation (<0.1s)",
      description: "Smooth optimization landscapes with single global optimum"
    },
    {
      name: "Non-convex function with fast evaluation (<0.1s)", 
      description: "Complex landscapes with multiple local optima"
    },
    {
      name: "Machine learning model hyperparameter optimization",
      description: "Tuning parameters for traditional ML models"
    },
    {
      name: "Deep learning model hyperparameter optimization",
      description: "Tuning neural network architectures and training parameters"
    }
  ];

  let selectedCategory = "all";
  let searchTerm = "";

  $: filteredOptimizers = optimizers.filter(opt => {
    const matchesCategory = selectedCategory === "all" || opt.category === selectedCategory;
    const matchesSearch = opt.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         opt.description.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const categories = ["all", ...new Set(optimizers.map(opt => opt.category))];
</script>

<svelte:head>
  <title>Algorithm Overview & Comparison - Optimization Tutorial</title>
</svelte:head>

<div class="overview-page">
  <header class="page-header">
    <h1>Algorithm Overview & Comparison</h1>
    <p class="page-description">
      Compare optimization algorithms across different problem types and find the best fit for your use case.
    </p>
  </header>

  <!-- Problem Types Legend -->
  <section class="legend">
    <h2>Problem Types</h2>
    <div class="problem-types">
      {#each problemTypes as problem, i}
        <div class="problem-type">
          <div class="problem-number">{i + 1}</div>
          <div>
            <h3>{problem.name}</h3>
            <p>{problem.description}</p>
          </div>
        </div>
      {/each}
    </div>
  </section>

  <!-- Filters -->
  <section class="filters">
    <div class="filter-group">
      <label for="category">Filter by Category:</label>
      <select id="category" bind:value={selectedCategory}>
        {#each categories as category}
          <option value={category}>
            {category === "all" ? "All Categories" : category}
          </option>
        {/each}
      </select>
    </div>
    
    <div class="filter-group">
      <label for="search">Search Algorithms:</label>
      <input 
        type="text" 
        id="search"
        placeholder="Search by name or description..." 
        bind:value={searchTerm}
      />
    </div>
  </section>

  <!-- Comparison Table -->
  <section class="comparison">
    <div class="table-container">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Algorithm</th>
            <th>Category</th>
            <th title="Convex function with fast evaluation">Problem 1</th>
            <th title="Non-convex function with fast evaluation">Problem 2</th>
            <th title="ML hyperparameter optimization">Problem 3</th>
            <th title="DL hyperparameter optimization">Problem 4</th>
            <th>Key Parameters</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {#each filteredOptimizers as optimizer}
            <tr>
              <td>
                <div class="algorithm-cell">
                  <strong>{optimizer.name}</strong>
                  <small>{optimizer.description}</small>
                </div>
              </td>
              <td>
                <span class="category-badge category-{optimizer.category.toLowerCase().replace(/[^a-z]/g, '')}">{optimizer.category}</span>
              </td>
              <td class="score-cell">{optimizer.convexFast}</td>
              <td class="score-cell">{optimizer.nonConvexFast}</td>
              <td class="score-cell">{optimizer.mlHyperparams}</td>
              <td class="score-cell">{optimizer.dlHyperparams}</td>
              <td>
                <div class="parameters">
                  {#each optimizer.parameters.slice(0, 3) as param}
                    <span class="param-tag">{param}</span>
                  {/each}
                  {#if optimizer.parameters.length > 3}
                    <span class="param-more">+{optimizer.parameters.length - 3} more</span>
                  {/if}
                </div>
              </td>
              <td>
                <a href={optimizer.path} class="learn-more-btn">Learn More</a>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </section>

  <!-- Algorithm Cards (Mobile-friendly alternative) -->
  <section class="algorithm-cards">
    {#each filteredOptimizers as optimizer}
      <div class="algorithm-card">
        <div class="card-header">
          <h3>{optimizer.name}</h3>
          <span class="category-badge category-{optimizer.category.toLowerCase().replace(/[^a-z]/g, '')}">{optimizer.category}</span>
        </div>
        
        <p class="description">{optimizer.description}</p>
        
        <div class="scores">
          <div class="score-row">
            <span class="label">Convex Fast:</span>
            <span class="score">{optimizer.convexFast}</span>
          </div>
          <div class="score-row">
            <span class="label">Non-convex Fast:</span>
            <span class="score">{optimizer.nonConvexFast}</span>
          </div>
          <div class="score-row">
            <span class="label">ML Hyperparams:</span>
            <span class="score">{optimizer.mlHyperparams}</span>
          </div>
          <div class="score-row">
            <span class="label">DL Hyperparams:</span>
            <span class="score">{optimizer.dlHyperparams}</span>
          </div>
        </div>

        <div class="strengths-weaknesses">
          <div class="strengths">
            <h4>✅ Strengths</h4>
            <ul>
              {#each optimizer.strengths as strength}
                <li>{strength}</li>
              {/each}
            </ul>
          </div>
          <div class="weaknesses">
            <h4>⚠️ Limitations</h4>
            <ul>
              {#each optimizer.weaknesses as weakness}
                <li>{weakness}</li>
              {/each}
            </ul>
          </div>
        </div>

        <div class="card-footer">
          <div class="parameters">
            {#each optimizer.parameters.slice(0, 4) as param}
              <span class="param-tag">{param}</span>
            {/each}
          </div>
          <a href={optimizer.path} class="learn-more-btn">Learn More →</a>
        </div>
      </div>
    {/each}
  </section>

  <!-- Legend -->
  <section class="scoring-legend">
    <h2>Scoring Legend</h2>
    <div class="legend-items">
      <div class="legend-item">
        <span class="legend-symbol">✅</span>
        <span>Excellent - Highly recommended for this problem type</span>
      </div>
      <div class="legend-item">
        <span class="legend-symbol">⚠️</span>
        <span>Good - Works well with proper parameter tuning</span>
      </div>
      <div class="legend-item">
        <span class="legend-symbol">❌</span>
        <span>Poor - Not recommended for this problem type</span>
      </div>
    </div>
  </section>
</div>

<style>
  .page-header {
    text-align: center;
    margin-bottom: 3rem;
  }

  .page-header h1 {
    font-size: 2.5rem;
    color: #1e293b;
    margin-bottom: 1rem;
  }

  .page-description {
    font-size: 1.1rem;
    color: #64748b;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
  }

  /* Problem Types Legend */
  .legend {
    margin-bottom: 3rem;
  }

  .legend h2 {
    color: #1e293b;
    margin-bottom: 1.5rem;
  }

  .problem-types {
    display: grid;
    gap: 1rem;
  }

  .problem-type {
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    padding: 1rem;
    background: #f8fafc;
    border-radius: 8px;
    border-left: 4px solid #3b82f6;
  }

  .problem-number {
    background: #3b82f6;
    color: white;
    width: 2rem;
    height: 2rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    flex-shrink: 0;
  }

  .problem-type h3 {
    margin: 0 0 0.5rem;
    color: #1e293b;
    font-size: 1rem;
  }

  .problem-type p {
    margin: 0;
    color: #64748b;
    font-size: 0.9rem;
  }

  /* Filters */
  .filters {
    display: flex;
    gap: 2rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
  }

  .filter-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .filter-group label {
    font-weight: 500;
    color: #374151;
  }

  .filter-group select,
  .filter-group input {
    padding: 0.5rem;
    border: 1px solid #d1d5db;
    border-radius: 4px;
    font-size: 0.9rem;
  }

  .filter-group input {
    min-width: 300px;
  }

  /* Comparison Table (Desktop) */
  .comparison {
    margin-bottom: 3rem;
  }

  .table-container {
    overflow-x: auto;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    border-radius: 8px;
  }

  .comparison-table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    min-width: 1000px;
  }

  .comparison-table th,
  .comparison-table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #e5e7eb;
  }

  .comparison-table th {
    background: #f9fafb;
    font-weight: 600;
    color: #374151;
    font-size: 0.875rem;
  }

  .algorithm-cell strong {
    display: block;
    color: #1e293b;
    margin-bottom: 0.25rem;
  }

  .algorithm-cell small {
    color: #64748b;
    font-size: 0.8rem;
    line-height: 1.3;
  }

  .score-cell {
    text-align: center;
    font-size: 1.2rem;
  }

  .category-badge {
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 500;
    white-space: nowrap;
  }

  .category-localsearch { background: #dbeafe; color: #1e40af; }
  .category-globalsearch { background: #dcfce7; color: #166534; }
  .category-populationbased { background: #fef3c7; color: #92400e; }
  .category-modelbased { background: #f3e8ff; color: #7c3aed; }

  .parameters {
    display: flex;
    flex-wrap: wrap;
    gap: 0.25rem;
  }

  .param-tag {
    background: #f1f5f9;
    color: #475569;
    padding: 0.125rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
  }

  .param-more {
    color: #64748b;
    font-size: 0.75rem;
    font-style: italic;
  }

  .learn-more-btn {
    background: #3b82f6;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.875rem;
    font-weight: 500;
    transition: background-color 0.2s;
  }

  .learn-more-btn:hover {
    background: #2563eb;
  }

  /* Algorithm Cards (Mobile) */
  .algorithm-cards {
    display: none;
    gap: 1.5rem;
  }

  .algorithm-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    border: 1px solid #e5e7eb;
  }

  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }

  .card-header h3 {
    margin: 0;
    color: #1e293b;
  }

  .description {
    color: #64748b;
    margin-bottom: 1rem;
    line-height: 1.5;
  }

  .scores {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.5rem;
    margin-bottom: 1rem;
    padding: 1rem;
    background: #f8fafc;
    border-radius: 6px;
  }

  .score-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .score-row .label {
    font-size: 0.875rem;
    color: #64748b;
  }

  .score-row .score {
    font-size: 1.1rem;
  }

  .strengths-weaknesses {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .strengths h4,
  .weaknesses h4 {
    margin: 0 0 0.5rem;
    font-size: 0.875rem;
    color: #374151;
  }

  .strengths ul,
  .weaknesses ul {
    margin: 0;
    padding-left: 1.2rem;
    font-size: 0.8rem;
    color: #64748b;
  }

  .strengths li,
  .weaknesses li {
    margin-bottom: 0.25rem;
  }

  .card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 1rem;
    border-top: 1px solid #e5e7eb;
  }

  /* Scoring Legend */
  .scoring-legend {
    background: #f8fafc;
    padding: 2rem;
    border-radius: 8px;
  }

  .scoring-legend h2 {
    color: #1e293b;
    margin-bottom: 1rem;
  }

  .legend-items {
    display: grid;
    gap: 0.75rem;
  }

  .legend-item {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .legend-symbol {
    font-size: 1.2rem;
    width: 2rem;
  }

  /* Mobile Responsive */
  @media (max-width: 768px) {
    .filters {
      flex-direction: column;
      gap: 1rem;
    }

    .filter-group input {
      min-width: auto;
    }

    .comparison {
      display: none;
    }

    .algorithm-cards {
      display: flex;
      flex-direction: column;
    }

    .scores {
      grid-template-columns: 1fr;
    }

    .strengths-weaknesses {
      grid-template-columns: 1fr;
    }

    .card-footer {
      flex-direction: column;
      gap: 1rem;
      align-items: stretch;
    }

    .parameters {
      justify-content: center;
    }
  }
</style>