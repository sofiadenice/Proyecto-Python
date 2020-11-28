from databaseX import DatabaseX
from prettytable import PrettyTable
from colores import Colores


class Ejercicio:
    def __init__(self, idUser):
        self.idUser = idUser
        self.colores = Colores()
        self.idEjercicio = 0
        self.dbx = DatabaseX()

    def agregarCardio(self):

        while True:

            while True:
                try:
                    idEjercicio = int(
                        input(
                            "Ingrese el ID de su ejercicio, si desconoce el ID ingrese 0 para ir al buscador: "
                        )
                    )

                    if idEjercicio < 0 or idEjercicio is None:
                        print("")
                        print(colores.red("Ese valor de ID de ejercicio no es válido"))
                        print("")
                    else:
                        self.idEjercicio = idEjercicio
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de ID de ejercicio solo acepta valores numéricos"
                        )
                    )
                    print("")

            if idEjercicio == 0:
                result = False
                break

            else:
                sqlCount = f"SELECT COUNT(*) FROM myfitapp.cardiovascular WHERE id_ejercicio = '{self.idEjercicio:}' and (id_usuario = 0 or id_usuario = '{self.idUser:}')"

                # Imprime para comprobar estructura del sqlCount
                # print(sqlCount)

                rowsNumDic = self.dbx.executeQueryOneRow(sqlCount)

                # Imprime el diccionario resultante de ejecutar sqlCount
                # print(rowsNumDic)

                rowsNum = rowsNumDic.get("COUNT(*)")

                # Imprime el numero de filas con ese ID de ejercicio
                # print(rowsNum)

                if rowsNum == 1:
                    result = True
                    break
                else:
                    print("")
                    print(
                        self.colores.red(
                            "El ID que ingresó no existe, por favor ingrese un ID válido"
                        )
                    )
                    print("")

        if result:

            while True:
                try:
                    tiempo = int(
                        input(
                            "Ingrese la cantidad de tiempo que se ejercitó en minutos: "
                        )
                    )
                    if tiempo <= 0 or tiempo is None:
                        print("")
                        print(self.colores.red("Ese valor de tiempo no es válido"))
                        print("")

                    else:

                        # meter a la BD
                        self.dbx.executeNonQueryBool(
                            "INSERT INTO `myfitapp`.`registrousuarioejerciciocardio`(`id_registroUsuarioCardio`,`id_usuario`,`id_ejercicio`,`tiempoTotalEmpleado`,`fecha`) "
                            + f"VALUES(0,{self.idUser},{self.idEjercicio}, {tiempo}, CURDATE());"
                        )

                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de tiempo solo acepta valores numéricos enteros"
                        )
                    )
                    print("")

            return result

        else:
            return result

    def buscarCardio(self):
        print("")

        # variables a ingresar

        EjercicioCardio = str(
            input("Ingrese el ejercicio de cardio que quiere buscar: ")
        )
        print("")

        # meter a la BD
        ejercicio1 = self.dbx.executeQueryRows(
            f"SELECT * FROM myfitapp.cardiovascular where nombreEjercicio like '%{EjercicioCardio}%'and id_usuario = 0 or id_usuario = {self.idUser};"
        )

        # imprimir info con prettytable

        table = PrettyTable()
        table.field_names = [
            "id_ejercicio",
            "nombre Ejercicio",
            "calorias quemadas por minuto",
        ]
        for row in ejercicio1:
            table.add_row(
                [
                    row["id_ejercicio"],
                    row["nombreEjercicio"],
                    row["caloriasQuemadas"],
                ]
            )
        print(table)
        print("")

    def crearCardio(self):
        print("")

        # variables a ingresar

        while True:
            try:
                nombre = str(input("Ingrese el nombre del nuevo ejercicio: "))
                if nombre == "":
                    print("")
                    print(self.colores.red("Ese valor de nombre no es válido"))
                    print("")
                else:
                    break

            except Exception:
                print("")
                print(self.colores.red("El campo de nombre solo acepta texto"))
                print("")

        while True:
            try:
                caloriasQuemadas = float(
                    input("Ingrese la cantidad de calorias quemadas por minuto: ")
                )

                if caloriasQuemadas < 0.0 or caloriasQuemadas is None:
                    print("")
                    print(self.colores.red("Ese valor de porciones no es válido"))
                    print("")
                else:

                    break

            except Exception:
                print("")
                print(
                    self.colores.red(
                        "El campo de calorias quemadas solo acepta valores numericos"
                    )
                )
                print("")

        # ingresar a la BD

        self.dbx.executeNonQueryBool(
            f"INSERT INTO `myfitapp`.`cardiovascular`(`id_ejercicio`,`nombreEjercicio`,`caloriasQuemadas`,`id_usuario`) VALUES(0,'{nombre}', {caloriasQuemadas}, {self.idUser});"
        )

    def agregarPeso(self):

        while True:

            while True:
                try:
                    idEjercicio = int(
                        input(
                            "Ingrese el ID de su ejercicio, si desconoce el ID ingrese 0 para ir al buscador: "
                        )
                    )

                    if idEjercicio < 0 or idEjercicio is None:
                        print("")
                        print(colores.red("Ese valor de ID de ejercicio no es válido"))
                        print("")
                    else:
                        self.idEjercicio = idEjercicio
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de ID de ejercicio solo acepta valores numéricos"
                        )
                    )
                    print("")

            if idEjercicio == 0:
                result = False
                break

            else:
                sqlCount = f"SELECT COUNT(*) FROM myfitapp.fuerza WHERE id_ejercicio = '{self.idEjercicio:}' and (id_usuario = 0 or id_usuario = '{self.idUser:}'"

                # Imprime para comprobar estructura del sqlCount
                # print(sqlCount)

                rowsNumDic = self.dbx.executeQueryOneRow(sqlCount)

                # Imprime el diccionario resultante de ejecutar sqlCount
                # print(rowsNumDic)

                rowsNum = rowsNumDic.get("COUNT(*)")

                # Imprime el numero de filas con ese ID de ejercicio
                # print(rowsNum)

                if rowsNum == 1:
                    result = True
                    break
                else:
                    print("")
                    print(
                        self.colores.red(
                            "El ID que ingresó no existe, por favor ingrese un ID válido"
                        )
                    )
                    print("")

        if result:

            while True:
                try:
                    repeticiones = int(
                        input("Ingrese la cantidad de repeticiones realizadas: ")
                    )

                    if repeticiones <= 0 or repeticiones is None:
                        print("")
                        print(
                            self.colores.red("Ese valor de repeticiones no es válido")
                        )
                        print("")
                    else:
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de repeticiones solo acepta valores numéricos"
                        )
                    )
                    print("")

            while True:
                try:
                    series = int(input("Ingrese la cantidad de series realizadas: "))
                    if series < 0 or series is None:
                        print("")
                        print(self.colores.red("Ese valor de series no es válido"))
                        print("")
                    else:
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de series solo acepta valores numericos"
                        )
                    )
                    print("")

            while True:
                try:
                    peso = int(
                        input(
                            "Ingrese la cantidad de libras aplicadas en su ejercicio: "
                        )
                    )
                    if peso < 0 or peso is None:
                        print("")
                        print(self.colores.red("Ese valor de peso no es válido"))
                        print("")
                    else:
                        break

                except Exception:
                    print("")
                    print(
                        self.colores.red(
                            "El campo de peso solo acepta valores numericos"
                        )
                    )
                    print("")

            # meter a la BD

            self.dbx.executeNonQueryBool(
                "INSERT INTO `myfitapp`.`registrousuarioejerciciofuerza`(`id_registroUsuarioFuerza`,`id_usuario`,`id_ejercicio`,`repeticiones`, series, pesoAplicado, `fecha`) "
                + f"VALUES(0,{self.idUser},{self.idEjercicio}, {repeticiones}, {series}, {peso}, CURDATE());"
            )

            return result

        else:
            return result

    def buscarPeso(self):
        print("")

        # variables a ingresar
        EjercicioPeso = str(input("Ingrese el ejercicio de peso que quiere buscar: "))
        print("")

        # meter a la BD
        ejercicio1 = self.dbx.executeQueryRows(
            f"SELECT * FROM myfitapp.fuerza where nombreEjercicio like '%{EjercicioPeso}%'and id_usuario = 0 or id_usuario = {self.idUser};"
        )

        # imprimir info con prettytable

        table = PrettyTable()
        table.field_names = [
            "id_ejercicio",
            "nombreEjercicio",
            "parteDelCuerpo",
        ]
        for row in ejercicio1:
            table.add_row(
                [
                    row["id_ejercicio"],
                    row["nombreEjercicio"],
                    row["parteDelCuerpo"],
                ]
            )
        print(table)
        print("")

    def crearPeso(self):
        print("")

        # variables a ingresar
        while True:
            try:
                nombre = str(input("Ingrese el nombre del nuevo ejercicio: "))
                if nombre == "":
                    print("")
                    print(self.colores.red("Ese valor de nombre no es válido"))
                    print("")
                else:
                    break

            except Exception:
                print("")
                print(self.colores.red("El campo de nombre solo acepta texto"))
                print("")

        while True:
            try:
                parteDelCuerpo = str(
                    input("Ingrese la parte del cuerpo que ejercita: ")
                )
                if parteDelCuerpo == "":
                    print("")
                    print(
                        self.colores.red("Ese valor de partes del cuerpo no es válido")
                    )
                    print("")
                else:
                    break

            except Exception:
                print("")
                print(
                    self.colores.red("El campo de parte del cuerpo solo acepta texto")
                )
                print("")

        print("")

        # ingresar a la BD

        self.dbx.executeNonQueryBool(
            f"INSERT INTO `myfitapp`.`fuerza`(`id_ejercicio`,`nombreEjercicio`,`parteDelCuerpo`,`id_usuario`) VALUES(0,'{nombre}', '{parteDelCuerpo}', {self.idUser});"
        )
