<?php
session_start();
define('BASE_PATH', __DIR__ . DIRECTORY_SEPARATOR);

require_once BASE_PATH . 'config/database.php';
require_once BASE_PATH . 'controllers/LoginController.php';
require_once BASE_PATH . 'controllers/HomeController.php';

$database = new database();
$conn = $database->getConnection();
$loginController = new LoginController($conn);
$homeController = new HomeController();

$action = $_GET['action'] ?? 'login';

switch ($action) {
    case 'login':
        $loginController->login();
        break;
    case 'logout':
        $loginController->logout();
        break;
    case 'register':
        $loginController->register();
        break;
    case 'home':
        $homeController->index();
        break;
    default:
        header('Location: index.php?action=login');
        break;
}
?>
