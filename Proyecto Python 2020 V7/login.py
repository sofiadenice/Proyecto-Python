from databaseX import DatabaseX


class Login:
    def __init__(self):
        self.idUser = 0
        self.dbx = DatabaseX()
        pass

    def comprobacion(self, usuario, contra):

        sqlCount = f"SELECT COUNT(*) FROM myfitapp.usuario WHERE user = '{usuario:}'"

        # Imprime para comprobar el sql que cuenta registros
        # print(sqlCount)

        rowsNumDic = self.dbx.executeQueryOneRow(sqlCount)

        # Imprime para comprobar el diccionario que resulta de la consulta de sqlCount
        # print(rowsNumDic)

        rowsNum = rowsNumDic.get("COUNT(*)")

        # Imprime para comprobar el número contado
        # print(rowsNum)

        if rowsNum == 1:

            sqlSelect = f"SELECT * FROM myfitapp.usuario WHERE user = '{usuario:}'"

            selectUserDic = self.dbx.executeQueryOneRow(sqlSelect)

            # Imprime el diccionario que resulta de ejecutar sqlSelect
            # print(selectUserDic)

            contraBD = selectUserDic.get("contra")

            # Imprime la contraseña de la BD
            # print(contraBD)

            if contraBD == contra:

                idBD = selectUserDic.get("id_usuario")
                self.idUser = idBD
                return True

            else:
                print("Contraseña incorrecta")
                return False

        else:
            print("El usuario que ha ingresado no existe")

    def idUsuario(self):
        return self.idUser
