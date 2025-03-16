def verificar_usuario(usuario, contraseña):
    usuarios_validos = {
        "admin": "1234",
        "tecnico": "abcd"
    }
    return usuarios_validos.get(usuario) == contraseña
