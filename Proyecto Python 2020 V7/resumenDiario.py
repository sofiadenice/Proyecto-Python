from databaseX import DatabaseX
from colores import Colores
from prettytable import PrettyTable


database = DatabaseX()


class Resumen:
    def __init__(self):
        self.database = DatabaseX()
        self.colores = Colores()

    def imprimeResumenActual(self, idUsuario):
        sqlCount = f"SELECT COUNT(id_registro) from registrodiario where id_usuario = {idUsuario} and fecha = curdate();"
        datos = self.database.executeQueryOneRow(sqlCount)
        count = datos.get("COUNT(id_registro)")
        if count == 1:
            sql = f"select * from registrodiario where fecha = curdate() AND id_usuario = {idUsuario};"
            resumen = self.database.executeQueryRows(sql)
            table = PrettyTable()
            table.field_names = [
                "Fecha",
                "Peso",
                "Cintura",
                "Cuello",
            ]
            for row in resumen:
                table.add_row(
                    [
                        row["fecha"],
                        row["pesoActual"],
                        row["cintura"],
                        row["cuello"],
                    ]
                )
            print("")
            print(table)
        else:
            print("")
            print(self.colores.red("No se encontró ningún registro de este día"))

    def imprimeResumenOtroDia(self, idUsuario):
        anno = 0
        while anno < 1000 or anno > 9999:
            try:
                anno = int(input("Ingresa el año deseado (yyyy): "))
                if anno < 1000 or anno > 9999:
                    print(self.colores.red("Ese valor de año no es válido"))
                else:
                    break
            except Exception:
                print(self.colores.red("El campo de año solo acepta valores numéricos"))

        mes = 0
        while mes < 1 or mes > 12:
            try:
                mes = int(input("Ingresa el mes deseado (mm): "))
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
                    dia = int(input("Ingresa el día deseado(dd): "))
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

        date = str(anno) + "-" + str(mes) + "-" + str(dia)

        sqlCount = f"SELECT COUNT(id_registro) from registrodiario where id_usuario = {idUsuario} and fecha = '{date}';"
        datos = self.database.executeQueryOneRow(sqlCount)
        count = datos.get("COUNT(id_registro)")
        if count == 1:
            sql = f"select * from registrodiario where id_usuario = {idUsuario} and fecha = '{date}';"
            resumen = self.database.executeQueryRows(sql)
            table = PrettyTable()
            table.field_names = [
                "Fecha",
                "Peso",
                "Cintura",
                "Cuello",
            ]
            for row in resumen:
                table.add_row(
                    [
                        row["fecha"],
                        row["pesoActual"],
                        row["cintura"],
                        row["cuello"],
                    ]
                )
            print("")
            print(table)
        else:
            print("")
            print(
                self.colores.red(
                    "No se encontró ningún registro con la fecha proporcionada"
                )
            )
