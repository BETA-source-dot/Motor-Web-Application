<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "parqueadero"; // cámbialo si tu BD se llama diferente

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
