<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenido</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Bienvenido, <?php echo htmlspecialchars($user['nombre_usuario']) . " " . htmlspecialchars($user['apaterno_usuario']); ?></h1>
        <p>Has iniciado sesión correctamente.</p>
        <p>Tu correo electrónico es: <?php echo htmlspecialchars($user['correo']); ?></p>
        <a href="index.php?action=logout" class="btn">Cerrar sesión</a>
    </div>
</body>
</html>
