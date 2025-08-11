<script>
  import { onMount } from 'svelte';

  const featuredOptimizers = [
    {
      name: "Hill Climbing",
      description: "A simple local search algorithm that starts from a random position and moves to better neighboring solutions.",
      category: "Local Search",
      difficulty: "Beginner",
      path: "/optimizers/hill-climbing"
    },
    {
      name: "Simulated Annealing",
      description: "Inspired by the metallurgical process, this algorithm accepts worse solutions with decreasing probability.",
      category: "Local Search", 
      difficulty: "Intermediate",
      path: "/optimizers/simulated-annealing"
    },
    {
      name: "Particle Swarm Optimization",
      description: "A population-based algorithm inspired by the social behavior of bird flocking or fish schooling.",
      category: "Population-based",
      difficulty: "Intermediate",
      path: "/optimizers/particle-swarm-optimization"
    },
    {
      name: "Bayesian Optimization",
      description: "A model-based approach that uses Gaussian processes to efficiently explore the search space.",
      category: "Model-based",
      difficulty: "Advanced",
      path: "/optimizers/bayesian-optimization"
    }
  ];

  const useCases = [
    {
      icon: "🎯",
      title: "Hyperparameter Tuning",
      description: "Optimize machine learning model parameters for better performance"
    },
    {
      icon: "⚙️",
      title: "Engineering Design",
      description: "Find optimal configurations for engineering systems and processes"
    },
    {
      icon: "📈",
      title: "Financial Optimization",
      description: "Portfolio optimization and algorithmic trading strategies"
    },
    {
      icon: "🧬",
      title: "Scientific Computing",
      description: "Parameter estimation and experimental design optimization"
    }
  ];
</script>

<svelte:head>
  <title>Optimization Tutorial - Learn Gradient-Free Optimization Algorithms</title>
  <meta name="description" content="Interactive tutorial for learning gradient-free optimization algorithms with visualizations and practical examples." />
</svelte:head>

<div class="landing-page">
  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-content">
      <h1 class="hero-title">
        Master Gradient-Free 
        <span class="highlight">Optimization Algorithms</span>
      </h1>
      <p class="hero-description">
        Learn optimization strategies through interactive visualizations, parameter exploration, 
        and practical examples. Perfect for machine learning practitioners, researchers, and engineers.
      </p>
      <div class="hero-buttons">
        <a href="/overview" class="btn btn-primary">
          🚀 Start Learning
        </a>
        <a href="#featured" class="btn btn-secondary">
          📚 Browse Algorithms
        </a>
      </div>
    </div>
  </section>

  <!-- Featured Algorithms -->
  <section id="featured" class="featured">
    <div class="section-header">
      <h2>Featured Algorithms</h2>
      <p>Start with these popular optimization techniques</p>
    </div>
    
    <div class="optimizer-grid">
      {#each featuredOptimizers as optimizer}
        <div class="optimizer-card">
          <div class="card-header">
            <h3>{optimizer.name}</h3>
            <div class="badges">
              <span class="badge category">{optimizer.category}</span>
              <span class="badge difficulty difficulty-{optimizer.difficulty.toLowerCase()}">{optimizer.difficulty}</span>
            </div>
          </div>
          <p class="card-description">{optimizer.description}</p>
          <a href={optimizer.path} class="card-link">
            Learn More →
          </a>
        </div>
      {/each}
    </div>
  </section>

  <!-- Use Cases -->
  <section class="use-cases">
    <div class="section-header">
      <h2>Applications & Use Cases</h2>
      <p>Discover where optimization algorithms make a difference</p>
    </div>
    
    <div class="use-case-grid">
      {#each useCases as useCase}
        <div class="use-case-card">
          <div class="use-case-icon">{useCase.icon}</div>
          <h3>{useCase.title}</h3>
          <p>{useCase.description}</p>
        </div>
      {/each}
    </div>
  </section>

  <!-- Getting Started -->
  <section class="getting-started">
    <div class="section-header">
      <h2>How to Use This Tutorial</h2>
    </div>
    
    <div class="steps">
      <div class="step">
        <div class="step-number">1</div>
        <h3>Explore the Overview</h3>
        <p>Start with our comparison table to understand different algorithm strengths and use cases.</p>
      </div>
      <div class="step">
        <div class="step-number">2</div>
        <h3>Pick an Algorithm</h3>
        <p>Choose an optimization algorithm that interests you or fits your specific problem.</p>
      </div>
      <div class="step">
        <div class="step-number">3</div>
        <h3>Learn Interactively</h3>
        <p>Adjust parameters, view visualizations, and understand algorithm behavior through examples.</p>
      </div>
    </div>
  </section>
</div>

<style>
  .landing-page {
    max-width: none;
    padding: 0;
  }

  /* Hero Section */
  .hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
    margin: -2rem -2rem 4rem -2rem;
  }

  .hero-content {
    max-width: 800px;
    margin: 0 auto;
  }

  .hero-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    line-height: 1.2;
  }

  .highlight {
    background: linear-gradient(45deg, #ffd89b 0%, #19547b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-description {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    line-height: 1.6;
    opacity: 0.9;
  }

  .hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  .btn {
    padding: 0.75rem 2rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
    font-size: 1rem;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
  }

  .btn-primary {
    background: white;
    color: #667eea;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  }

  .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
  }

  .btn-secondary {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    border: 2px solid rgba(255, 255, 255, 0.3);
  }

  .btn-secondary:hover {
    background: rgba(255, 255, 255, 0.2);
    border-color: rgba(255, 255, 255, 0.5);
  }

  /* Sections */
  section {
    margin-bottom: 4rem;
  }

  .section-header {
    text-align: center;
    margin-bottom: 3rem;
  }

  .section-header h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #1e293b;
  }

  .section-header p {
    font-size: 1.1rem;
    color: #64748b;
  }

  /* Featured Algorithms */
  .optimizer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
  }

  .optimizer-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    border: 1px solid #e2e8f0;
    transition: all 0.2s ease;
  }

  .optimizer-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  }

  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1rem;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .card-header h3 {
    margin: 0;
    color: #1e293b;
    font-size: 1.25rem;
  }

  .badges {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .badge {
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 500;
  }

  .badge.category {
    background: #e0f2fe;
    color: #0369a1;
  }

  .badge.difficulty-beginner {
    background: #dcfce7;
    color: #166534;
  }

  .badge.difficulty-intermediate {
    background: #fef3c7;
    color: #92400e;
  }

  .badge.difficulty-advanced {
    background: #fecaca;
    color: #991b1b;
  }

  .card-description {
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 1.5rem;
  }

  .card-link {
    color: #3b82f6;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
  }

  .card-link:hover {
    color: #1d4ed8;
  }

  /* Use Cases */
  .use-case-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
  }

  .use-case-card {
    text-align: center;
    padding: 2rem 1rem;
  }

  .use-case-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
  }

  .use-case-card h3 {
    margin-bottom: 1rem;
    color: #1e293b;
  }

  .use-case-card p {
    color: #64748b;
    line-height: 1.6;
  }

  /* Getting Started */
  .steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }

  .step {
    text-align: center;
    padding: 2rem;
  }

  .step-number {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0 auto 1.5rem;
  }

  .step h3 {
    margin-bottom: 1rem;
    color: #1e293b;
  }

  .step p {
    color: #64748b;
    line-height: 1.6;
  }

  /* Mobile Responsive */
  @media (max-width: 768px) {
    .hero {
      padding: 3rem 1rem;
      margin: -1rem -1rem 3rem -1rem;
    }

    .hero-title {
      font-size: 2rem;
    }

    .hero-description {
      font-size: 1rem;
    }

    .section-header h2 {
      font-size: 2rem;
    }

    .optimizer-grid,
    .use-case-grid,
    .steps {
      grid-template-columns: 1fr;
    }

    .card-header {
      flex-direction: column;
      align-items: flex-start;
    }
  }
</style>