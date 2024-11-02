<?php
session_start();
define('BASE_PATH', dirname(__DIR__) . DIRECTORY_SEPARATOR);

require_once BASE_PATH . 'config/database.php';
require_once BASE_PATH . 'controllers/LoginController.php';
require_once BASE_PATH . 'controllers/HomeController.php';

$action = isset($_GET['action']) ? $_GET['action'] : 'login';

$loginController = new LoginController($conn);
$homeController = new HomeController();

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