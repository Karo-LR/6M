<?php
class User {
    private $conn;

    public function __construct($db) {
        $this->conn = $db;
    }

    public function login($correo, $password) {
        $query = "SELECT curp, correo, nombre_usuario, apaterno_usuario, amaterno_usuario, telefono FROM usuarios WHERE correo = :correo AND password = :password";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':correo', $correo);
        $stmt->bindParam(':password', $password);
        $stmt->execute();

        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    public function register($curp, $correo, $password, $nombre_usuario, $apaterno_usuario, $amaterno_usuario, $telefono) {
        $query = "INSERT INTO usuarios (curp, correo, password, nombre_usuario, apaterno_usuario, amaterno_usuario, telefono) VALUES (:curp, :correo, :password, :nombre_usuario, :apaterno_usuario, :amaterno_usuario, :telefono)";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':curp', $curp);
        $stmt->bindParam(':correo', $correo);
        $stmt->bindParam(':password', $password);
        $stmt->bindParam(':nombre_usuario', $nombre_usuario);
        $stmt->bindParam(':apaterno_usuario', $apaterno_usuario);
        $stmt->bindParam(':amaterno_usuario', $amaterno_usuario);
        $stmt->bindParam(':telefono', $telefono);
        
        return $stmt->execute();
    }
}
?>
