<?php
require_once BASE_PATH . 'models/User.php';

class LoginController {
    private $user;

    public function __construct($db) {
        $this->user = new User($db);
    }

    public function login() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $correo = $_POST['correo'];
            $password = $_POST['password'];

            $user = $this->user->login($correo, $password);

            if ($user) {
                $_SESSION['user'] = $user;
                header('Location: index.php?action=home');
                exit();
            } else {
                $error = "Correo o contraseña inválidos";
                include BASE_PATH . 'views/login.php';
            }
        } else {
            include BASE_PATH . 'views/login.php';
        }
    }

    public function logout() {
        session_destroy();
        header('Location: index.php?action=login');
        exit();
    }

    public function register() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $curp = $_POST['curp'];
            $correo = $_POST['correo'];
            $password = $_POST['password'];
            $nombre_usuario = $_POST['nombre_usuario'];
            $apaterno_usuario = $_POST['apaterno_usuario'];
            $amaterno_usuario = $_POST['amaterno_usuario'];
            $telefono = $_POST['telefono'];

            if ($this->user->register($curp, $correo, $password, $nombre_usuario, $apaterno_usuario, $amaterno_usuario, $telefono)) {
                $success = "Usuario registrado exitosamente";
                $_SESSION['user'] = [
                    'curp' => $curp,
                    'correo' => $correo,
                    'nombre_usuario' => $nombre_usuario,
                    'apaterno_usuario' => $apaterno_usuario,
                    'amaterno_usuario' => $amaterno_usuario,
                    'telefono' => $telefono
                ];
                header('Location: index.php?action=home');
                exit();
            } else {
                $error = "Error al registrar el usuario";
                include BASE_PATH . 'views/register.php';
            }
        } else {
            include BASE_PATH . 'views/register.php';
        }
    }
}
?>
