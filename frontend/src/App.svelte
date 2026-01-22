<script>
  let name = '';
  let message = '';
  let loading = false;
  let error = null;

  // URL del backend - siempre apunta al puerto 8080
  // IMPORTANTE: Desde el navegador siempre usa localhost:8080
  // El nombre 'backend' solo funciona dentro de la red Docker, no desde el navegador
  const getApiUrl = () => {
    // Siempre usa localhost:8080 desde el navegador
    // El puerto 8080 está mapeado desde el contenedor Docker al host
    const apiUrl = 'http://localhost:8080';
    return `${apiUrl}/example`;
  };

  const fetchExample = async () => {
    if (!name.trim()) {
      error = 'Por favor ingresa un nombre';
      return;
    }

    loading = true;
    error = null;
    message = '';

    try {
      const url = `${getApiUrl()}?name=${encodeURIComponent(name)}`;
      console.log('🔍 Haciendo petición a:', url);
      const response = await fetch(url);
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Error al obtener el mensaje');
      }

      message = data.message;
    } catch (err) {
      error = err.message;
      console.error('Error:', err);
    } finally {
      loading = false;
    }
  };
</script>

<main>
  <div class="container">
    <header>
      <h1>🚀 Motia + Svelte Template</h1>
      <p>Una plantilla lista para usar con backend Motia (Python) y frontend Svelte</p>
    </header>

    <div class="card">
      <div class="input-section">
        <label for="name-input">
          <h2>Ejemplo de integración:</h2>
        </label>
        <input
          id="name-input"
          type="text"
          bind:value={name}
          placeholder="Ingresa tu nombre..."
          on:keydown={e => e.key === 'Enter' && fetchExample()}
        />

        {#if error}
          <div class="error-message">
            ⚠️ {error}
          </div>
        {/if}

        {#if message}
          <div class="success-message">
            ✅ {message}
          </div>
        {/if}

        <button on:click={fetchExample} disabled={loading || !name.trim()} class="action-btn">
          {#if loading}
            <span class="spinner"></span> Cargando...
          {:else}
            🎯 Probar API
          {/if}
        </button>
      </div>

      <div class="info-section">
        <h3>📚 Próximos pasos:</h3>
        <ul>
          <li>Edita <code>src/example.step.py</code> para crear tus propios Steps</li>
          <li>Modifica este componente en <code>frontend/src/App.svelte</code></li>
          <li>
            Consulta la <a href="https://www.motia.dev/docs" target="_blank"
              >documentación de Motia</a
            >
          </li>
          <li>Lee <code>docs/ARCHITECTURE.md</code> para entender la estructura</li>
        </ul>
      </div>
    </div>
  </div>
</main>

<style>
  main {
    width: 100%;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
  }

  .container {
    max-width: 800px;
    margin: 0 auto;
  }

  header {
    text-align: center;
    color: white;
    margin-bottom: 30px;
  }

  header h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  }

  header p {
    font-size: 1.1rem;
    opacity: 0.9;
  }

  .card {
    background: white;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  }

  .input-section h2 {
    margin-bottom: 15px;
    color: #333;
  }

  input {
    width: 100%;
    padding: 15px;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-size: 16px;
    font-family: inherit;
    transition: border-color 0.3s;
    margin-bottom: 15px;
  }

  input:focus {
    outline: none;
    border-color: #667eea;
  }

  .error-message {
    margin-bottom: 15px;
    padding: 12px;
    background: #fee;
    border: 1px solid #fcc;
    border-radius: 8px;
    color: #c33;
  }

  .success-message {
    margin-bottom: 15px;
    padding: 12px;
    background: #efe;
    border: 1px solid #cfc;
    border-radius: 8px;
    color: #3c3;
  }

  .action-btn {
    width: 100%;
    padding: 15px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 18px;
    font-weight: 600;
    cursor: pointer;
    transition:
      transform 0.2s,
      box-shadow 0.2s;
  }

  .action-btn:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
  }

  .action-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  .spinner {
    display: inline-block;
    width: 16px;
    height: 16px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    border-top-color: white;
    animation: spin 0.8s linear infinite;
    margin-right: 8px;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  .info-section {
    margin-top: 30px;
    padding-top: 30px;
    border-top: 1px solid #e0e0e0;
  }

  .info-section h3 {
    margin-bottom: 15px;
    color: #333;
  }

  .info-section ul {
    list-style: none;
    padding: 0;
  }

  .info-section li {
    padding: 10px 0;
    color: #666;
    line-height: 1.6;
  }

  .info-section code {
    background: #f5f5f5;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
    color: #667eea;
  }

  .info-section a {
    color: #667eea;
    text-decoration: none;
    font-weight: 500;
  }

  .info-section a:hover {
    text-decoration: underline;
  }

  @media (max-width: 768px) {
    header h1 {
      font-size: 2rem;
    }

    .card {
      padding: 20px;
    }
  }
</style>
