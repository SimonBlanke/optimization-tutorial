<script>
  import ParameterControl from '$lib/components/ParameterControl.svelte';
  import VisualizationPanel from '$lib/components/VisualizationPanel.svelte';
  
  const algorithmInfo = {
    name: "Hill Climbing",
    category: "Local Search",
    difficulty: "Beginner",
    description: "Hill climbing is a very basic optimization technique that explores the search space only locally. It starts at an initial point, which is often chosen randomly, and continues to move to positions with better solutions. It has no method against getting stuck in local optima.",
    
    parameters: [
      {
        name: "epsilon",
        type: "number",
        default: 0.05,
        min: 0.001,
        max: 1.0,
        step: 0.001,
        description: "Determines how far the algorithm jumps from one position to the next. Higher epsilon leads to longer jumps."
      },
      {
        name: "distribution",
        type: "select",
        default: "normal",
        options: ["normal", "laplace", "logistic", "gumbel"],
        description: "The mathematical distribution the algorithm draws samples from."
      },
      {
        name: "n_neighbours",
        type: "number", 
        default: 3,
        min: 1,
        max: 50,
        step: 1,
        description: "Number of positions the algorithm explores from its current position before jumping to the best one."
      },
      {
        name: "rand_rest_p",
        type: "number",
        default: 0,
        min: 0,
        max: 1,
        step: 0.01,
        description: "Probability for the optimization algorithm to jump to a random position in an iteration step."
      }
    ],

    strengths: [
      "Fast execution",
      "Simple implementation",
      "Low memory requirements",
      "Good for fine-tuning near optimum"
    ],

    weaknesses: [
      "Gets stuck in local optima",
      "No global search capability", 
      "Sensitive to starting position",
      "No way to escape plateaus"
    ],

    useCases: [
      "When you have a very good initial point to start from",
      "If the search space is very simple and has few local optima",
      "For fine-tuning solutions found by other algorithms",
      "When computational resources are very limited"
    ],

    notRecommendedFor: [
      "Never as a first method of optimization",
      "Complex multi-modal functions",
      "Problems with many local optima",
      "Noisy objective functions"
    ]
  };

  // Parameter state
  let parameterValues = {};
  algorithmInfo.parameters.forEach(param => {
    parameterValues[param.name] = param.default;
  });

  // Visualization assets (these would come from the existing assets)
  const visualizations = [
    {
      name: "Algorithm Behavior",
      type: "gif",
      src: "/assets/hill_climbing/ackley_function.gif",
      description: "Hill climbing optimization on the Ackley function"
    },
    {
      name: "Parameter Effect: Epsilon",
      type: "gif", 
      src: "/assets/hill_climbing/epsilon_comparison.gif",
      description: "How different epsilon values affect the search behavior"
    },
    {
      name: "Parameter Effect: N_neighbours", 
      type: "gif",
      src: "/assets/hill_climbing/n_neighbours_comparison.gif",
      description: "Impact of exploring different numbers of neighbors"
    }
  ];
</script>

<svelte:head>
  <title>Hill Climbing Algorithm - Optimization Tutorial</title>
  <meta name="description" content="Learn about Hill Climbing optimization algorithm with interactive parameter controls and visualizations." />
</svelte:head>

<div class="algorithm-page">
  <!-- Algorithm Header -->
  <header class="algorithm-header">
    <div class="header-content">
      <div class="title-section">
        <h1>{algorithmInfo.name}</h1>
        <div class="badges">
          <span class="badge category">{algorithmInfo.category}</span>
          <span class="badge difficulty difficulty-{algorithmInfo.difficulty.toLowerCase()}">{algorithmInfo.difficulty}</span>
        </div>
      </div>
      <p class="description">{algorithmInfo.description}</p>
    </div>
  </header>

  <div class="content-grid">
    <!-- Main Content -->
    <main class="main-content">
      <!-- Theory Section -->
      <section class="theory-section">
        <h2>How It Works</h2>
        <div class="algorithm-explanation">
          <p>
            Hill climbing works by starting at a random point in the search space and iteratively 
            moving to better neighboring solutions. The algorithm follows these steps:
          </p>
          <ol>
            <li><strong>Initialize:</strong> Start at a random position in the search space</li>
            <li><strong>Generate neighbors:</strong> Create {parameterValues.n_neighbours} neighboring solutions using the {parameterValues.distribution} distribution with step size {parameterValues.epsilon}</li>
            <li><strong>Evaluate:</strong> Calculate the objective function for each neighbor</li>
            <li><strong>Select best:</strong> Move to the neighbor with the best objective value</li>
            <li><strong>Repeat:</strong> Continue until no better neighbor is found or maximum iterations reached</li>
          </ol>

          <div class="formula-section">
            <h3>Mathematical Formulation</h3>
            <p>The next position is selected as:</p>
            <div class="formula">
              x<sub>t+1</sub> = x<sub>t</sub> + ε · N(0, 1)
            </div>
            <p>where ε is the step size (epsilon) and N(0, 1) represents the selected distribution.</p>
          </div>
        </div>
      </section>

      <!-- Visualizations -->
      <section class="visualizations">
        <h2>Algorithm Visualization</h2>
        <VisualizationPanel {visualizations} />
      </section>

      <!-- Strengths and Weaknesses -->
      <section class="pros-cons">
        <div class="pros-cons-grid">
          <div class="pros">
            <h3>✅ Strengths</h3>
            <ul>
              {#each algorithmInfo.strengths as strength}
                <li>{strength}</li>
              {/each}
            </ul>
          </div>
          <div class="cons">
            <h3>⚠️ Limitations</h3>
            <ul>
              {#each algorithmInfo.weaknesses as weakness}
                <li>{weakness}</li>
              {/each}
            </ul>
          </div>
        </div>
      </section>

      <!-- Use Cases -->
      <section class="use-cases-section">
        <div class="use-cases-grid">
          <div class="recommended">
            <h3>🎯 Best Used For</h3>
            <ul>
              {#each algorithmInfo.useCases as useCase}
                <li>{useCase}</li>
              {/each}
            </ul>
          </div>
          <div class="not-recommended">
            <h3>❌ Avoid For</h3>
            <ul>
              {#each algorithmInfo.notRecommendedFor as notFor}
                <li>{notFor}</li>
              {/each}
            </ul>
          </div>
        </div>
      </section>

      <!-- Code Example -->
      <section class="code-example">
        <h2>Implementation Example</h2>
        <div class="code-block">
          <pre><code>{`from gradient_free_optimizers import HillClimbingOptimizer

# Define your objective function
def objective_function(para):
    return -(para["x1"]**2 + para["x2"]**2)  # Simple sphere function

# Define search space
search_space = {
    "x1": [-5, 5],
    "x2": [-5, 5],
}

# Initialize optimizer with current parameters
opt = HillClimbingOptimizer(
    search_space,
    epsilon=${parameterValues.epsilon},
    distribution="${parameterValues.distribution}",
    n_neighbours=${parameterValues.n_neighbours},
    rand_rest_p=${parameterValues.rand_rest_p}
)

# Run optimization
opt.search(objective_function, n_iter=1000)`}</code></pre>
        </div>
      </section>
    </main>

    <!-- Parameter Controls Sidebar -->
    <aside class="parameters-sidebar">
      <div class="sticky-content">
        <h2>Interactive Parameters</h2>
        <p class="parameters-description">
          Adjust the parameters below to see how they affect the algorithm's behavior and the code example.
        </p>
        
        <div class="parameter-controls">
          {#each algorithmInfo.parameters as param}
            <ParameterControl 
              {param} 
              bind:value={parameterValues[param.name]} 
            />
          {/each}
        </div>

        <div class="parameter-summary">
          <h3>Current Configuration</h3>
          <div class="config-display">
            {#each Object.entries(parameterValues) as [key, value]}
              <div class="config-item">
                <span class="config-key">{key}:</span>
                <span class="config-value">{value}</span>
              </div>
            {/each}
          </div>
        </div>

        <div class="navigation-links">
          <a href="/optimizers/simulated-annealing" class="nav-link">
            Next: Simulated Annealing →
          </a>
          <a href="/overview" class="nav-link secondary">
            ← Back to Overview
          </a>
        </div>
      </div>
    </aside>
  </div>
</div>

<style>
  .algorithm-page {
    max-width: none;
    padding: 0;
  }

  .algorithm-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 3rem 2rem;
    margin: -2rem -2rem 0 -2rem;
  }

  .header-content {
    max-width: 1200px;
    margin: 0 auto;
  }

  .title-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .algorithm-header h1 {
    font-size: 3rem;
    margin: 0;
    font-weight: 700;
  }

  .badges {
    display: flex;
    gap: 0.75rem;
  }

  .badge {
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.875rem;
    font-weight: 500;
  }

  .badge.category {
    background: rgba(255, 255, 255, 0.2);
    color: white;
  }

  .badge.difficulty-beginner {
    background: #dcfce7;
    color: #166534;
  }

  .description {
    font-size: 1.2rem;
    line-height: 1.6;
    margin: 0;
    opacity: 0.95;
  }

  .content-grid {
    display: grid;
    grid-template-columns: 1fr 350px;
    gap: 3rem;
    margin-top: 3rem;
  }

  .main-content {
    min-width: 0;
  }

  .parameters-sidebar {
    background: #f8fafc;
    border-radius: 12px;
    padding: 0;
    height: fit-content;
  }

  .sticky-content {
    position: sticky;
    top: 2rem;
    padding: 2rem;
  }

  .parameters-sidebar h2 {
    color: #1e293b;
    margin: 0 0 1rem;
    font-size: 1.5rem;
  }

  .parameters-description {
    color: #64748b;
    margin-bottom: 2rem;
    line-height: 1.5;
  }

  .parameter-controls {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  /* Main content sections */
  section {
    margin-bottom: 3rem;
  }

  section h2 {
    color: #1e293b;
    font-size: 2rem;
    margin-bottom: 1.5rem;
    border-bottom: 3px solid #e2e8f0;
    padding-bottom: 0.5rem;
  }

  section h3 {
    color: #374151;
    font-size: 1.3rem;
    margin-bottom: 1rem;
  }

  .algorithm-explanation {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  }

  .algorithm-explanation p {
    line-height: 1.7;
    color: #374151;
    margin-bottom: 1.5rem;
  }

  .algorithm-explanation ol {
    line-height: 1.6;
    color: #374151;
  }

  .algorithm-explanation li {
    margin-bottom: 0.75rem;
  }

  .formula-section {
    background: #f8fafc;
    padding: 1.5rem;
    border-radius: 8px;
    margin-top: 2rem;
  }

  .formula {
    background: white;
    padding: 1rem;
    border-radius: 6px;
    font-family: 'Courier New', monospace;
    font-size: 1.1rem;
    text-align: center;
    border: 2px solid #e2e8f0;
    margin: 1rem 0;
  }

  /* Pros and Cons */
  .pros-cons-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }

  .pros, .cons {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  }

  .pros h3 {
    color: #059669;
    margin-bottom: 1rem;
  }

  .cons h3 {
    color: #dc2626;
    margin-bottom: 1rem;
  }

  .pros ul, .cons ul {
    margin: 0;
    padding-left: 1.5rem;
  }

  .pros li, .cons li {
    margin-bottom: 0.5rem;
    line-height: 1.5;
  }

  /* Use Cases */
  .use-cases-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }

  .recommended, .not-recommended {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  }

  .recommended h3 {
    color: #059669;
    margin-bottom: 1rem;
  }

  .not-recommended h3 {
    color: #dc2626;
    margin-bottom: 1rem;
  }

  .recommended ul, .not-recommended ul {
    margin: 0;
    padding-left: 1.5rem;
  }

  .recommended li, .not-recommended li {
    margin-bottom: 0.5rem;
    line-height: 1.5;
  }

  /* Code Example */
  .code-block {
    background: #1e293b;
    border-radius: 8px;
    overflow-x: auto;
  }

  .code-block pre {
    margin: 0;
    padding: 2rem;
    color: #e2e8f0;
    font-size: 0.9rem;
    line-height: 1.6;
  }

  .code-block code {
    font-family: 'Fira Code', 'Consolas', monospace;
  }

  /* Parameter Summary */
  .parameter-summary {
    background: white;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 2rem;
  }

  .parameter-summary h3 {
    margin: 0 0 1rem;
    color: #1e293b;
    font-size: 1.1rem;
  }

  .config-display {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .config-item {
    display: flex;
    justify-content: space-between;
    padding: 0.25rem 0;
    border-bottom: 1px solid #f1f5f9;
  }

  .config-key {
    font-weight: 500;
    color: #374151;
  }

  .config-value {
    color: #3b82f6;
    font-family: monospace;
  }

  /* Navigation Links */
  .navigation-links {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .nav-link {
    padding: 0.75rem 1rem;
    background: #3b82f6;
    color: white;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 500;
    text-align: center;
    transition: background-color 0.2s;
  }

  .nav-link:hover {
    background: #2563eb;
  }

  .nav-link.secondary {
    background: #64748b;
  }

  .nav-link.secondary:hover {
    background: #475569;
  }

  /* Mobile Responsive */
  @media (max-width: 1024px) {
    .content-grid {
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    .sticky-content {
      position: relative;
      top: auto;
    }

    .parameters-sidebar {
      order: -1;
    }
  }

  @media (max-width: 768px) {
    .algorithm-header {
      padding: 2rem 1rem;
      margin: -1rem -1rem 0 -1rem;
    }

    .algorithm-header h1 {
      font-size: 2rem;
    }

    .title-section {
      flex-direction: column;
      align-items: flex-start;
    }

    .pros-cons-grid,
    .use-cases-grid {
      grid-template-columns: 1fr;
    }

    .code-block pre {
      padding: 1rem;
      font-size: 0.8rem;
    }
  }
</style>