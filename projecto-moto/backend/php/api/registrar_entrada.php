<?php
require_once('../config.php'); // Ajusta la ruta si es necesario

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $placa = $_POST["placa"];
    $tipo = $_POST["tipo"];
    $hora_entrada = $_POST["hora_entrada"];

    $sql = "INSERT INTO entradas (placa, tipo_vehiculo, hora_entrada) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sss", $placa, $tipo, $hora_entrada);

    if ($stmt->execute()) {
        echo "Entrada registrada correctamente.";
    } else {
        echo "Error al registrar: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
} else {
    echo "Método no permitido.";
}
