document.addEventListener("DOMContentLoaded", () => {
      const btnEnviar = document.getElementById("btnEnviar");
      const spinner = document.getElementById("spinner");

      btnEnviar.addEventListener("click", async () => {
        spinner.classList.remove("hidden");

        try {
          const res = await fetch("/enviar_datos");
          const data = await res.json();

          if (res.ok && !data.error) {
            window.location.href = "/exito_datos";
          } else {
            window.location.href = "/error_datos";
          }
        } catch (error) {
          window.location.href = "/error_datos";
        }
      });
    });