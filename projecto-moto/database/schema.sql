-- Crear base de datos
DROP DATABASE IF EXISTS VOLTDB;
CREATE DATABASE VOLTDB;
USE VOLTDB;

-- Tabla de usuarios (clientes y administradores)
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    rol ENUM('cliente', 'admin') DEFAULT 'cliente'
);

-- Tabla de categorías de productos
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla de productos (motos, boutique, repuestos)
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    imagen_url VARCHAR(255),
    categoria_id INT,
    stock INT DEFAULT 0,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

-- Tabla de pedidos
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL,
    estado ENUM('pendiente', 'pagado', 'enviado', 'cancelado') DEFAULT 'pendiente',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Tabla de detalle de pedidos (productos por pedido)
CREATE TABLE detalle_pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Datos de prueba

-- Insertar usuarios
INSERT INTO usuarios (nombre, correo, contraseña, direccion, telefono, rol)
VALUES
('Daniel Reyes', 'daniel@mail.com', '123456', 'Cra 1 #23-45', '3123456789', 'cliente'),
('Admin User', 'admin@mail.com', 'admin123', 'Cra 99 #88-77', '3000000000', 'admin');

-- Insertar categorías
INSERT INTO categorias (nombre, descripcion)
VALUES
('Motos', 'Motos nuevas y usadas'),
('Repuestos', 'Repuestos originales'),
('Boutique', 'Accesorios y ropa para motociclistas'),
('Seguros', 'Servicios de seguros para motos');

-- Insertar productos
INSERT INTO productos (nombre, descripcion, precio, imagen_url, categoria_id, stock)
VALUES
('Yamaha FZ 2.0', 'Moto deportiva de 150cc ideal para ciudad', 8500000, 'img/motos/fz.jpg', 1, 10),
('Honda CB 190R', 'Moto deportiva, excelente rendimiento', 11500000, 'img/motos/cb190r.jpg', 1, 5),
('Casco SHIRO SH-600', 'Casco integral de alta seguridad', 280000, 'img/boutique/casco.jpg', 3, 20),
('Aceite 4T Motul 5100', 'Lubricante semisintético 20W50', 45000, 'img/repuestos/aceite.jpg', 2, 50),
('Seguro Todo Riesgo SURA', 'Cobertura completa anual', 550000, 'img/seguros/sura.jpg', 4, 100);

-- Insertar pedido de prueba
INSERT INTO pedidos (usuario_id, total, estado)
VALUES (1, 11800000, 'pagado');

-- Insertar detalle del pedido
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario)
VALUES
(1, 1, 1, 8500000),
(1, 3, 2, 280000),
(1, 4, 1, 45000);
