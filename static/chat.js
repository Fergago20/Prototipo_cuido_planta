document.addEventListener('DOMContentLoaded', () => {
  const btnEnviar = document.getElementById('btnEnviar');
  const btnObtener = document.getElementById('btnObtener');
  const responseBox = document.getElementById('responseBox');

  btnEnviar.addEventListener('click', async () => {
    try {
      const res = await fetch('/enviar_datos');
      const data = await res.json();
      mostrarRespuesta(data);
    } catch (err) {
      mostrarRespuesta({ error: 'Error al enviar datos a N8N' });
    }
  });

  btnObtener.addEventListener('click', async () => {
    const workflowId = document.getElementById('workflowId').value;
    if (!workflowId.trim()) {
      return mostrarRespuesta({ error: 'Debe ingresar un workflow ID' });
    }

    try {
      const res = await fetch(`/obtener_dados?workflow_id=${encodeURIComponent(workflowId)}`);
      const data = await res.json();
      mostrarRespuesta(data);
    } catch (err) {
      mostrarRespuesta({ error: 'Error al obtener datos de N8N' });
    }
  });

  function mostrarRespuesta(data) {
    responseBox.classList.remove('hidden');
    responseBox.textContent = JSON.stringify(data, null, 2);
  }
});