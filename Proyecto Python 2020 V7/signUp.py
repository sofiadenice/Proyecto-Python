from databaseX import DatabaseX
from colores import Colores
from medidas import Medidas


class SignUp:
    def __init__(self):
        self.dbx = DatabaseX()
        self.colores = Colores()
        self.medidas = Medidas()
        self.user = ""
        self.correo = ""
        self.contra = ""

    def comprobacionUsuario(self, usuario):

        while usuario == "":
            print(self.colores.red("Debe llenar el campo de usuario"))
            usuario = input("Ingrese un nombre de usuario: ")

        sqlCount = f"SELECT COUNT(*) FROM myfitapp.usuario WHERE user = '{usuario:}'"

        # Imprime para comprobar estructura del sqlCount
        # print(sqlCount)

        rowsNumDic = self.dbx.executeQueryOneRow(sqlCount)

        # Imprime el diccionario resultante de ejecutar sqlCount
        # print(rowsNumDic)

        rowsNum = rowsNumDic.get("COUNT(*)")

        # Imprime el numero de filas con ese nombre de usuario
        # print(rowsNum)

        if rowsNum == 0:
            # print("ok")
            self.user = usuario
            return True
        else:
            # print("mal")
            return False

    def comprobacionCorreo(self, correo):

        while correo == "":
            print(self.colores.red("Debe llenar el campo de correo"))
            correo = input("Ingrese su correo electronico: ")

        sqlCount = f"SELECT COUNT(*) FROM myfitapp.usuario WHERE correo = '{correo:}'"

        # Imprime para comprobar estructura del sqlCount
        # print(sqlCount)

        rowsNumDic = self.dbx.executeQueryOneRow(sqlCount)

        # Imprime el diccionario resultante de ejecutar sqlCount
        # print(rowsNumDic)

        rowsNum = rowsNumDic.get("COUNT(*)")

        # Imprime el número de correos con correo
        # print(rowsNum)

        if rowsNum == 0:
            # print("ok")
            self.correo = correo
            return True
        else:
            # print("mal")
            return False
        pass

    def comprobacionContra(self, contra):
        while (len(contra) > 12) or (len(contra) < 4):
            print(self.colores.red("Contraseña no válida"))
            contra = input(
                "Ingrese una contraseña de mínimo 4 y máximo 12 caracteres: "
            )
        self.contra = contra
        return True

    def guardaDatos(self):
        nombre = input("Ingrese su nombre: ")
        while nombre == "":
            print(self.colores.red("Debe llenar el campo nombre"))
            nombre = input("Ingrese su nombre: ")

        apellido = input("Ingrese su apellido: ")
        while apellido == "":
            print(self.colores.red("Debe llenar el campo apellido"))
            apellido = input("Ingrese su apellido: ")

        genero = 0
        while True:
            try:
                print("Ingrese su género: ")
                print("(1) Masculino")
                print("(2) Femenino")
                genero = int(input("Ingrese el número de la opción que desea: "))
            except Exception:
                print(self.colores.red("Valor no válido"))

            if genero == 1 or genero == 2:
                break
            else:
                print(
                    self.colores.red(
                        "Género no válido. Vuelva a ingresar su respuesta."
                    )
                )

        altura = 0
        while altura < 0.5 or altura > 3:
            try:
                altura = float(input("Ingrese su altura en metros: "))
                if altura < 0.5 or altura > 3:
                    print(self.colores.red("Ese valor de altura no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red("El campo de altura solo acepta valores numéricos")
                )

        peso = 0.00
        while peso < 10 or peso > 440:
            try:
                peso = float(input("Ingrese su peso en kilogramos: "))
                if peso < 10 or peso > 440:
                    print(self.colores.red("Ese valor de peso no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red("El campo de peso solo acepta valores numéricos")
                )

        pesoDeseado = 0
        while pesoDeseado < 10 or pesoDeseado > 440:
            try:
                pesoDeseado = float(input("Ingrese su peso deseado en kilogramos: "))
                if pesoDeseado < 10 or pesoDeseado > 440:
                    print(self.colores.red("Ese valor de peso deseado no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red(
                        "El campo de peso deseado solo acepta valores numéricos"
                    )
                )

        print("Ingrese su fecha de nacimiento con números")

        anno = 0
        while anno < 1000 or anno > 9999:
            try:
                anno = int(input("Ingrese su año de nacimiento: "))
                if anno < 1000 or anno > 9999:
                    print(self.colores.red("Ese valor de año no es válido"))
                else:
                    break
            except Exception:
                print(self.colores.red("El campo de año solo acepta valores numéricos"))

        mes = 0
        while mes < 1 or mes > 12:
            try:
                mes = int(input("Ingrese su mes de nacimiento: "))
                if mes < 1 or mes > 12:
                    print(self.colores.red("Ese valor de mes no es válido"))
                else:
                    break
            except Exception:
                print(self.colores.red("El campo de mes solo acepta valores numéricos"))

        while True:
            dia = 0
            while True:
                try:
                    dia = int(input("Ingrese su día de nacimiento: "))
                    break
                except Exception:
                    print(
                        self.colores.red(
                            "El campo de día solo acepta valores numéricos"
                        )
                    )

            if (
                mes == 1
                or mes == 3
                or mes == 5
                or mes == 7
                or mes == 8
                or mes == 10
                or mes == 12
            ):
                if dia < 1 or dia > 31:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia < 1 or dia > 30:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            elif mes == 2 and (
                anno % 4 == 0 and (not (anno % 100 == 0) or anno % 400 == 0)
            ):
                if dia < 1 or dia > 29:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            elif mes == 2:
                if dia < 1 or dia > 28:
                    print(self.colores.red("Valor de día no válido"))
                else:
                    break
            else:
                print(self.colores.red("Ese valor de día no es válido"))

        sql2 = (
            "INSERT INTO myfitapp.usuario (id_usuario, nombre, apellido, correo, user, contra, id_genero, altura, pesoActual, pesoDeseado, nacimiento) "
            + f"VALUES (0, '{nombre}', '{apellido}', '{self.correo}', '{self.user}', '{self.contra}', {genero}, {altura}, {peso}, {pesoDeseado}, '{anno}-{mes}-{dia}');"
        )

        insert = self.dbx.executeNonQueryBool(sql2)

        if insert:
            print(self.colores.green("Usuario registrado correctamente"))
        else:
            print(self.colores.red("No se ha podido registrar el nuevo usuario"))

        # mandar peso actual como primer registro del usuario en la tabla registro diario
        sqlCount = f"SELECT COUNT(id_usuario) from myfitapp.usuario where user = '{self.user}';"
        countDic = self.dbx.executeQueryOneRow(sqlCount)
        count = countDic.get("COUNT(id_usuario)")
        if count == 1:
            sqlId = (
                f"SELECT id_usuario from myfitapp.usuario where user = '{self.user}';"
            )
            IdUsuarioDic = self.dbx.executeQueryOneRow(sqlId)
            idUser = IdUsuarioDic.get("id_usuario")
            self.medidas.ingresarPrimerPeso(peso, idUser)
        else:
            print(
                self.colores.red(
                    "No se ingresó el peso actual a la tabla registros diarios"
                )
            )
