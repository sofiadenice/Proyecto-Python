from databaseX import DatabaseX

# dbx = DatabaseX()
# usuario = "'User1'"
# contra = "Contra1"
# sql = f"SELECT COUNT(*) FROM myfitapp.usuario WHERE user = {usuario:}"
# print(sql)

# nombre = "Juan"
# apellido = "Ramírez"
# correo = "juan@ramirex.com"
# user = "JuanRex"
# contra = "123456"
# genero = 1
# altura = 1.7
# peso = 100
# pesoDeseado = 80
# anno = 1990
# mes = 6
# dia = 30

# sql2 = "INSERT INTO myfitapp.usuario (id_usuario, nombre, apellido, correo, user, contra, id_genero, altura, pesoInicial, pesoDeseado, nacimiento) "
# + f"VALUES (0, '{nombre}', '{apellido}', '{correo}', '{user}', '{contra}', {genero}, {altura}, {peso}, {pesoDeseado}, '{anno}-{mes}-{dia}');"

# print(sql2)

# insert = dbx.executeNonQueryBool(sql2)

# if insert:
#     print("Usuario registrado correctamente")
# else:
#     print("No se ha podido registrar el nuevo usuario")


while True:
    try:
        genero = int(input("Ingrese género: "))
        break
    except Exception:
        print("Valor no válido")


print(genero)
