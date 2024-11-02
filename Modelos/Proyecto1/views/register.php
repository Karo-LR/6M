<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de usuarios</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h2>Registro de usuarios</h2>
        <?php if (isset($error)) : ?>
            <p class="error"><?php echo $error; ?></p>
        <?php endif; ?>
        <form action="index.php?action=register" method="post">
            <div>
                <label for="curp">CURP:</label>
                <input type="text" id="curp" name="curp" required maxlength="18">
            </div>
            <div>
                <label for="correo">Correo:</label>
                <input type="email" id="correo" name="correo" required maxlength="35">
            </div>
            <div>
                <label for="password">Contraseña:</label>
                <input type="password" id="password" name="password" required maxlength="8">
            </div>
            <div>
                <label for="nombre_usuario">Nombre:</label>
                <input type="text" id="nombre_usuario" name="nombre_usuario" required maxlength="35">
            </div>
            <div>
                <label for="apaterno_usuario">Apellido Paterno:</label>
                <input type="text" id="apaterno_usuario" name="apaterno_usuario" required maxlength="35">
            </div>
            <div>
                <label for="amaterno_usuario">Apellido Materno:</label>
                <input type="text" id="amaterno_usuario" name="amaterno_usuario" required maxlength="35">
            </div>
            <div>
                <label for="telefono">Teléfono:</label>
                <input type="tel" id="telefono" name="telefono" required maxlength="10">
            </div>
            <button type="submit">Registrarse</button>
        </form>
        <p>¿Ya tienes una cuenta? <a href="index.php?action=login">Inicia sesión aquí</a></p>
    </
