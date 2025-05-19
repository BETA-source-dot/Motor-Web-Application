
const productos = [
    {
        nombre: "Test",
        precio: 40.00,
        imagen: "../Assets/Img/Products/Mototest.jpg",
        estrellas: 4.5,
        marca: "Yamaha",
        proposito: "Urbana",
        modelo: "FZ-25"
    },
    {
        nombre: "Test2",
        precio: 30.10,
        imagen: "../Assets/Img/Products/Mototest2.png",
        estrellas: 5,
        marca: "Suzuki",
        proposito: "Deportiva",
        modelo: "Gixxer SF"
    },
    {
        nombre: "Test3",
        precio: 50.00,
        imagen: "../Assets/Img/Products/Mototest3.png",
        estrellas: 4.5,
        marca: "Honda",
        proposito: "Urbana",
        modelo: "CB 190R"
    },
    {
        nombre: "Test4",
        precio: 60.00,
        imagen: "../Assets/Img/Products/Mototest4.png",
        estrellas: 2.5,
        marca: "Yamaha",
        proposito: "Enduro",
        modelo: "XTZ 125"
    },
];

function generarEstrellas(valor) {
    let html = "";
    const enteras = Math.floor(valor);
    const media = valor % 1 >= 0.5;

    for (let i = 0; i < enteras; i++) {
        html += `<i class="bi bi-star-fill"></i>`;
    }

    if (media) {
        html += `<i class="bi bi-star-half"></i>`;
    }

    const vacías = 5 - enteras - (media ? 1 : 0);
    for (let i = 0; i < vacías; i++) {
        html += `<i class="bi bi-star"></i>`;
    }

    return html;
}

function mostrarProductos(lista = productos) {
    const contenedor = document.querySelector(".on-sale .row");
    contenedor.innerHTML = "";

    if (lista.length === 0) {
        contenedor.innerHTML = "<p class='text-test p-5 m-5 rounded-5 text-secondary shadow text-center fw-bolder'>No se encontraron productos.</p>";
        return;
    }

    lista.forEach(producto => {
        const estrellas = generarEstrellas(producto.estrellas);
        const html = `
        <div class="col-md-3">
            <div class="product-top">
                <img src="${producto.imagen}">
                <div class="overlay-right">
                    <button type="button" class="btn btn-secondary" title="Vista previa"><i class="bi bi-eye"></i></button>
                    <button type="button" class="btn btn-secondary" title="Añadir a favoritos"><i class="bi bi-heart"></i></button>
                    <button type="button" class="btn btn-secondary" title="Añadir al Carrito"><i class="bi bi-cart"></i></button>
                </div>
            </div>
            <div class="product-bottom text-center">
                ${estrellas}
                <h3>${producto.nombre}</h3>
                <h5>$${producto.precio.toFixed(2)}</h5>
            </div>
        </div>
        `;
        contenedor.innerHTML += html;
    });
}

function filtrarProductos() {
    const marca = document.getElementById("filtroMarca")?.value.toLowerCase() || "";
    const proposito = document.getElementById("filtroProposito")?.value.toLowerCase() || "";
    const modelo = document.getElementById("filtroModelo")?.value.toLowerCase() || "";

    const filtrados = productos.filter(p => {
        return (
            (marca === "" || p.marca.toLowerCase() === marca) &&
            (proposito === "" || p.proposito.toLowerCase() === proposito) &&
            (modelo === "" || p.modelo.toLowerCase().includes(modelo))
        );
    });

    mostrarProductos(filtrados);
}

window.filtrarProductos = filtrarProductos; // para uso desde HTML

document.addEventListener("DOMContentLoaded", () => {
    mostrarProductos();

    // Activar filtrado en vivo si existen los elementos
    document.getElementById("filtroMarca")?.addEventListener("change", filtrarProductos);
    document.getElementById("filtroProposito")?.addEventListener("change", filtrarProductos);
    document.getElementById("filtroModelo")?.addEventListener("input", filtrarProductos);
});
