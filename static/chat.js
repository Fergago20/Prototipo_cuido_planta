document.getElementById("enviar-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const datos = {
        usuario: document.getElementById("usuario").value,
        mensaje: document.getElementById("mensaje").value
    };

    fetch("/enviar_datos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datos)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("respuesta").textContent = JSON.stringify(data, null, 2);
    })
    .catch(err => {
        document.getElementById("respuesta").textContent = "Error al enviar: " + err;
    });
});

document.getElementById("obtener-btn").addEventListener("click", function () {
    const workflowId = document.getElementById("workflow_id").value;

    fetch(`/obtener_dados?workflow_id=${encodeURIComponent(workflowId)}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("respuesta").textContent = JSON.stringify(data, null, 2);
        })
        .catch(err => {
            document.getElementById("respuesta").textContent = "Error al obtener datos: " + err;
        });
});
