let chart;
console.log("Grafico cargado correctamente");
console.log("Datos recibidos:", datos);
document.addEventListener("DOMContentLoaded", () => {
    if (typeof datos === "undefined") return;

    const fechas = [];
    const humedad = [];
    const tempAmbiente = [];
    const tempObjeto = [];
    const humedadSuelo = [];

    datos.forEach(d => {
        fechas.push(d.fecha_revision);

        humedad.push(parseFloat(d.humedad.replace('%', '').trim()));
        tempAmbiente.push(parseFloat(d.temperatura_ambiente.replace('°C', '').trim()));
        tempObjeto.push(parseFloat(d.temperatura_objeto.replace('°C', '').trim()));
        humedadSuelo.push(parseFloat(d.humedad_suelo.replace('%', '').trim()));
    });

    renderChart(fechas, humedad, tempAmbiente, tempObjeto, humedadSuelo);
});

function renderChart(labels, h, tA, tO, hS) {
    const ctx = document.getElementById("grafico").getContext("2d");
    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels,
            datasets: [
                {
                    label: "Humedad (%)",
                    data: h,
                    borderColor: '#4B0000',
                    backgroundColor: 'rgba(75, 0, 0, 0.2)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: "Temperatura Ambiente (°C)",
                    data: tA,
                    borderColor: '#333333',
                    backgroundColor: 'rgba(51, 51, 51, 0.2)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: "Temperatura Objeto (°C)",
                    data: tO,
                    borderColor: '#8B0000',
                    backgroundColor: 'rgba(139, 0, 0, 0.2)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: "Humedad Suelo (%)",
                    data: hS,
                    borderColor: '#B22222',
                    backgroundColor: 'rgba(178, 34, 34, 0.2)',
                    fill: true,
                    tension: 0.4
                }
            ]
        },
        options: {
            responsive: true,
            interaction: {
                mode: 'index',
                intersect: false,
            },
            stacked: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
