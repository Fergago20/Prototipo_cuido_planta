let chart;
console.log("Gráfico cargado correctamente");
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
                    label: "🌱 Humedad (%)",
                    data: h,
                    borderColor: '#2e7d32',
                    backgroundColor: 'rgba(46, 125, 50, 0.2)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: "🌤️ Temp. Ambiente (°C)",
                    data: tA,
                    borderColor: '#66bb6a',
                    backgroundColor: 'rgba(102, 187, 106, 0.2)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: "🔥 Temp. Objeto (°C)",
                    data: tO,
                    borderColor: '#388e3c',
                    backgroundColor: 'rgba(56, 142, 60, 0.2)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: "🌾 Humedad Suelo (%)",
                    data: hS,
                    borderColor: '#1b5e20',
                    backgroundColor: 'rgba(27, 94, 32, 0.2)',
                    fill: true,
                    tension: 0.4
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: "#1b5e20", // color verde oscuro en las leyendas
                        font: {
                            weight: "bold"
                        }
                    }
                }
            },
            interaction: {
                mode: 'index',
                intersect: false,
            },
            stacked: false,
            scales: {
                x: {
                    ticks: { color: "#2e7d32" }, // verde en el eje X
                    grid: { color: "rgba(46, 125, 50, 0.1)" }
                },
                y: {
                    beginAtZero: true,
                    ticks: { color: "#2e7d32" }, // verde en el eje Y
                    grid: { color: "rgba(46, 125, 50, 0.1)" }
                }
            }
        }
    });
}
