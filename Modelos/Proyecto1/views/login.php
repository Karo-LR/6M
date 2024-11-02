<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <?php if (isset($error)) : ?>
            <p class="error"><?php echo $error; ?></p>
        <?php endif; ?>
        <?php if (isset($success)) : ?>
            <p class="success"><?php echo $success; ?></p>
        <?php endif; ?>
        <form action="index.php?action=login" method="post">
            <div>
                <label for="correo">Correo electrónico:</label>
                <input type="email" id="correo" name="correo" required maxlength="35">
            </div>
            <div>
                <label for="password">Contraseña:</label>
                <input type="password" id="password" name="password" required maxlength="8">
            </div>
            <button type="submit">Iniciar sesión</button>
        </form>
        <p>¿No tienes una cuenta? <a href="index.php?action=register">Regístrate aquí</a></p>
    </div>
</body>
</html>