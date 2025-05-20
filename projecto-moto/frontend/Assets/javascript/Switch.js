document.addEventListener("DOMContentLoaded", () => {
    mostrarProductos();
    mostrarDestacados();

    // Activar filtros
    document.getElementById("filtroMarca")?.addEventListener("change", filtrarProductos);
    document.getElementById("filtroProposito")?.addEventListener("change", filtrarProductos);
    document.getElementById("filtroModelo")?.addEventListener("input", filtrarProductos);

    // Interruptor de modo oscuro
    const toggleBtn = document.getElementById("modoToggle");
    const modoOscuroActivo = localStorage.getItem("modoOscuro") === "true";

    if (modoOscuroActivo) {
        document.body.classList.add("modo-oscuro");
        toggleBtn.textContent = "☀️";
    }

    toggleBtn.addEventListener("click", () => {
        document.body.classList.toggle("modo-oscuro");
        const oscuro = document.body.classList.contains("modo-oscuro");
        toggleBtn.textContent = oscuro ? "☀️" : "🌙";
        localStorage.setItem("modoOscuro", oscuro);
    });
});
