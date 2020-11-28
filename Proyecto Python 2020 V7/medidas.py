from databaseX import DatabaseX
from colores import Colores


class Medidas:
    def __init__(self):
        self.colores = Colores()
        self.database = DatabaseX()
        self.peso = 0.00
        self.cintura = 0.00
        self.cuello = 0.00

    def ingresarPrimerPeso(self, peso, idUsuario):
        sql = (
            "INSERT INTO `myfitapp`.`registrodiario`(`id_registro`,`id_usuario`,`cintura`,`cuello`,`pesoActual`,`fecha`) "
            + f"VALUES(0,{idUsuario},{self.cintura},{self.cuello},{peso},curdate());"
        )
        self.database.executeNonQueryBool(sql)

    def ingresarPeso(self, idUsuario):
        peso = 0.00
        while peso < 0.01 or peso > 400:
            try:
                peso = float(input("Ingrese su peso en kilogramos: "))
                if peso < 0.01 or peso > 400:
                    print(self.colores.red("Ese valor de peso no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red("El campo de peso solo acepta valores numéricos")
                )

        self.peso = peso
        sqlCount = f"SELECT COUNT(id_registro) from registrodiario where fecha = curdate() and id_usuario = {idUsuario};"
        datos = self.database.executeQueryOneRow(sqlCount)
        count = datos.get("COUNT(id_registro)")
        if count == 0:
            sql = (
                "INSERT INTO `myfitapp`.`registrodiario`(`id_registro`,`id_usuario`,`cintura`,`cuello`,`pesoActual`,`fecha`) "
                + f"VALUES(0,{idUsuario},{self.cintura},{self.cuello},{self.peso},curdate());"
            )
            self.database.executeNonQueryBool(sql)
        else:
            sql = (
                "UPDATE `myfitapp`.`registrodiario` "
                + f"SET `pesoActual` = {self.peso} where `fecha` = curDate() AND `id_usuario` = {idUsuario};"
            )
            self.database.executeNonQueryBool(sql)

        print("")
        print(self.colores.green("El registro se guardó correctamente"))

        # Actualización del campo Peso Actual en la tabla Usuario

        sql1 = (
            "UPDATE `myfitapp`.`usuario` "
            + f"SET `pesoActual` = {self.peso} where `id_usuario` = {idUsuario};"
        )
        self.database.executeNonQueryBool(sql1)

    def ingresarCintura(self, idUsuario):
        cintura = 0.00
        while cintura < 0.01 or cintura > 300:
            try:
                cintura = float(input("Ingrese su medida de cintura en centímetros: "))
                if cintura < 0.01 or cintura > 300:
                    print(self.colores.red("Ese valor de cintura no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red(
                        "El campo de cintura solo acepta valores numéricos"
                    )
                )

        self.cintura = cintura
        sqlCount = f"SELECT COUNT(id_registro) from registrodiario where fecha = curdate() and id_usuario = {idUsuario};"
        datos = self.database.executeQueryOneRow(sqlCount)
        count = datos.get("COUNT(id_registro)")
        if count == 0:
            sql = (
                "INSERT INTO `myfitapp`.`registrodiario`(`id_registro`,`id_usuario`,`cintura`,`cuello`,`pesoActual`,`fecha`) "
                + f"VALUES(0,{idUsuario},{self.cintura},{self.cuello},{self.peso},curdate());"
            )
            self.database.executeNonQueryBool(sql)
        else:
            sql = (
                "UPDATE `myfitapp`.`registrodiario` "
                + f"SET `cintura` = {self.cintura} where `fecha` = curDate() AND `id_usuario` = {idUsuario};"
            )
            self.database.executeNonQueryBool(sql)

        print("")
        print(self.colores.green("El registro se guardó correctamente"))

    def ingresarCuello(self, idUsuario):
        cuello = 0.00
        while cuello < 0.01 or cuello > 200:
            try:
                cuello = float(input("Ingrese su medida de cuello en centímetros: "))
                if cuello < 0.01 or cuello > 200:
                    print(self.colores.red("Ese valor de cuello no es válido"))
                else:
                    break
            except Exception:
                print(
                    self.colores.red("El campo de cuello solo acepta valores numéricos")
                )

        self.cuello = cuello
        sqlCount = f"SELECT COUNT(id_registro) from registrodiario where fecha = curdate() and id_usuario = {idUsuario};"
        datos = self.database.executeQueryOneRow(sqlCount)
        count = datos.get("COUNT(id_registro)")
        if count == 0:
            sql = (
                "INSERT INTO `myfitapp`.`registrodiario`(`id_registro`,`id_usuario`,`cintura`,`cuello`,`pesoActual`,`fecha`) "
                + f"VALUES(0,{idUsuario},{self.cintura},{self.cuello},{self.peso},curdate());"
            )
            self.database.executeNonQueryBool(sql)
        else:
            sql = (
                "UPDATE `myfitapp`.`registrodiario` "
                + f"SET `cuello` = {self.cuello} where `fecha` = curDate() AND `id_usuario` = {idUsuario};"
            )
            self.database.executeNonQueryBool(sql)

        print("")
        print(self.colores.green("El registro se guardó correctamente"))
