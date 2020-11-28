from databaseX import DatabaseX
import matplotlib.pyplot as plt
from colores import Colores


class Evolucion:
    def __init__(self):
        self.database = DatabaseX()
        self.colores = Colores()

    def evoPeso(self, idUsuario):
        sql = f"select * from registrodiario where id_usuario = {idUsuario} order by fecha asc;"
        datos = self.database.executeQueryRows(sql)
        listaDato = []
        listaFecha = []
        for row in datos:
            if row["pesoActual"] > 0:
                fechaFixed = str(row["fecha"])
                listaFecha.append(fechaFixed[:10])
                listaDato.append(float(row["pesoActual"]))
        Ejey = listaDato
        Ejex = listaFecha
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(Ejex, Ejey, marker="o", color="#7581bf")
        ax.set(title="Evolución de peso diario", xlabel="Fecha", ylabel="Peso\n(kg)")
        plt.grid(True, color="#b4b5bf")
        plt.show()

    def evoCintura(self, idUsuario):
        sql = f"select * from registrodiario where id_usuario = {idUsuario} order by fecha asc;"
        datos = self.database.executeQueryRows(sql)
        listaDato = []
        listaFecha = []
        for row in datos:
            if row["cintura"] > 0:
                fechaFixed = str(row["fecha"])
                listaFecha.append(fechaFixed[:10])
                listaDato.append(float(row["cintura"]))
        Ejey = listaDato
        Ejex = listaFecha
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(Ejex, Ejey, marker="o", color="#7581bf")
        ax.set(title="Evolución de cintura", xlabel="Fecha", ylabel="Medida\n(cm)")
        plt.grid(True, color="#b4b5bf")
        plt.show()

    def evoCuello(self, idUsuario):
        sql = f"select * from registrodiario where id_usuario = {idUsuario} order by fecha asc;"
        datos = self.database.executeQueryRows(sql)
        listaDato = []
        listaFecha = []
        for row in datos:
            if row["cuello"] > 0:
                fechaFixed = str(row["fecha"])
                listaFecha.append(fechaFixed[:10])
                listaDato.append(float(row["cuello"]))
        Ejey = listaDato
        Ejex = listaFecha
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(Ejex, Ejey, marker="o", color="#7581bf")
        ax.set(title="Evolución de Cuello", xlabel="Fecha", ylabel="Medida\n(cm)")
        plt.grid(True, color="#b4b5bf")
        plt.show()

    def evoCalConsumidas(self, idUsuario):
        sql = (
            "SELECT consumoalimento.fecha,sum(consumoalimento.porcion*producto.calorias) as caloriasTotales "
            + "FROM consumoalimento inner join producto on consumoalimento.id_producto = producto.id_producto "
            + f"where consumoalimento.id_usuario = {idUsuario} group by consumoalimento.fecha order by fecha asc;"
        )
        datos = self.database.executeQueryRows(sql)
        listaDato = []
        listaFecha = []
        for row in datos:
            fechaFixed = str(row["fecha"])
            listaFecha.append(fechaFixed[:10])
            listaDato.append(float(row["caloriasTotales"]))
        Ejey = listaDato
        Ejex = listaFecha
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(Ejex, Ejey, marker="o", color="#7581bf")
        ax.set(
            title="Evolución de calorias consumidas",
            xlabel="Fecha",
            ylabel="Calorias\n(kcal)",
        )
        plt.grid(True, color="#b4b5bf")
        plt.show()

    def evoCalQuemadas(self, idUsuario):
        print(self.colores.red("Fuera de servicio..."))

    def evoEjPeso(self, idUsuario):
        print(self.colores.red("Fuera de servicio..."))

    def evoTiempo(self, idUsuario):
        print(self.colores.red("Fuera de servicio..."))
