<script>
  import Sidebar from '$lib/components/Sidebar.svelte';
  import { onMount } from 'svelte';

  let sidebarOpen = false;
  
  function toggleSidebar() {
    sidebarOpen = !sidebarOpen;
  }

  // Close sidebar when clicking outside on mobile
  function closeSidebar() {
    sidebarOpen = false;
  }
</script>

<div class="app">
  <Sidebar bind:open={sidebarOpen} />
  
  <main class="main-content" class:shifted={sidebarOpen}>
    <header class="header">
      <button class="sidebar-toggle" on:click={toggleSidebar} aria-label="Toggle sidebar">
        <span class="hamburger"></span>
        <span class="hamburger"></span>
        <span class="hamburger"></span>
      </button>
      <h1>Optimization Tutorial</h1>
    </header>
    
    <div class="content">
      <slot />
    </div>
  </main>
</div>

<!-- Sidebar overlay for mobile -->
{#if sidebarOpen}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div class="sidebar-overlay" on:click={closeSidebar}></div>
{/if}

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background-color: #f8fafc;
    color: #334155;
  }

  :global(*) {
    box-sizing: border-box;
  }

  .app {
    display: flex;
    min-height: 100vh;
  }

  .main-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    transition: margin-left 0.3s ease;
  }

  .main-content.shifted {
    margin-left: 280px;
  }

  .header {
    background: white;
    padding: 1rem 2rem;
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    align-items: center;
    gap: 1rem;
    position: sticky;
    top: 0;
    z-index: 10;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  }

  .sidebar-toggle {
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
    display: flex;
    flex-direction: column;
    gap: 3px;
    border-radius: 4px;
    transition: background-color 0.2s ease;
  }

  .sidebar-toggle:hover {
    background-color: #f1f5f9;
  }

  .hamburger {
    display: block;
    width: 20px;
    height: 2px;
    background-color: #64748b;
    transition: all 0.3s ease;
  }

  .header h1 {
    margin: 0;
    font-size: 1.5rem;
    font-weight: 600;
    color: #1e293b;
  }

  .content {
    flex: 1;
    padding: 2rem;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
  }

  .sidebar-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 15;
    display: none;
  }

  /* Mobile styles */
  @media (max-width: 768px) {
    .main-content.shifted {
      margin-left: 0;
    }
    
    .sidebar-overlay {
      display: block;
    }
    
    .content {
      padding: 1rem;
    }
    
    .header {
      padding: 1rem;
    }
  }
</style>