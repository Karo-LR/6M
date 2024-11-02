<?php
class HomeController {
    public function index() {
        // Verificar si el usuario está autenticado
        if (!isset($_SESSION['user'])) {
            header('Location: index.php?action=login');
            exit();
        }
        
        $user = $_SESSION['user'];
        include BASE_PATH . 'views/home.php';
    }
}
?>
