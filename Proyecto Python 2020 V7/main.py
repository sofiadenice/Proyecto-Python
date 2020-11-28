from login import Login
from signUp import SignUp
from resumenDiario import Resumen
from medidas import Medidas
from objetivos import Objetivos
from alimentacion import Alimentacion
from ejercicio import Ejercicio
from evolucion import Evolucion
from colores import Colores

eleccion = 0
idUsuario = 0
colores = Colores()


while True:
    print("")
    print(colores.cyan("-------------------------------------------------------"))
    print(colores.blue("APLICACIÓN FIT"))
    print(colores.cyan("-------------------------------------------------------"))
    print("(1) Iniciar sesión")
    print("(2) Crear una cuenta")
    print("(0) Salir")
    print(colores.cyan("-------------------------------------------------------"))
    print("")
    while True:
        try:
            eleccion = int(input("Ingrese el número de la opción que desea: "))
            break
        except Exception:
            print(colores.red("Este campo solo acepta valores numéricos"))
    print("")

    if eleccion == 0:
        break
    elif eleccion == 1:
        login = Login()
        usuario = input("Ingrese su nombre de usuario: ")
        contra = input("Ingrese su contraseña: ")
        comprobacion = login.comprobacion(usuario, contra)
        if comprobacion:
            print("")
            print(colores.green("Iniciando sesión..."))
            idUsuario = login.idUsuario()
            break
        else:
            print("")
            print(colores.red("Usuario o contraseña incorrectos"))
    elif eleccion == 2:
        signUp = SignUp()
        while True:
            usuario = input("Ingrese un nombre de usuario: ")
            compUsuario = signUp.comprobacionUsuario(usuario)
            if compUsuario:
                while True:
                    correo = input("Ingrese su correo electronico: ")
                    compCorreo = signUp.comprobacionCorreo(correo)
                    if compCorreo:
                        while True:
                            contra = input(
                                "Ingrese una contraseña de mínimo 4 y máximo 12 caracteres: "
                            )
                            compContra = signUp.comprobacionContra(contra)
                            if compContra:
                                signUp.guardaDatos()
                                break
                            else:
                                print(colores.red("Contraseña no válida"))
                        break
                    else:
                        print(
                            colores.red(
                                "Ya existe una cuenta vinculada a ese correo electrónico"
                            )
                        )
                break
            else:
                print(colores.red("El usuario que ha ingresado ya existe"))
    else:
        print(colores.red("La opción que ingresó no existe"))

while True:

    if eleccion == 0:
        break

    print("")
    print(colores.cyan("-------------------------------------------------------"))
    print(colores.blue("MENÚ PRINCIPAL"))
    print(colores.cyan("-------------------------------------------------------"))
    print("(1) Mostrar resumen diario")
    print("(2) Ingresar medidas")
    print("(3) Objetivos")
    print("(4) Registrar alimento")
    print("(5) Registrar ejercicio")
    print("(6) Evolución de mi progreso")
    print("(0) Salir")
    print(colores.cyan("-------------------------------------------------------"))
    print("")
    while True:
        try:
            eleccion = int(input("Ingrese el número de la opción que desea: "))
            break
        except Exception:
            print(colores.red("Este campo solo acepta valores numéricos"))
    print("")

    if eleccion == 0:
        break
    elif eleccion == 1:
        while True:
            print("")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print(colores.blue("MENÚ DE RESUMEN DIARIO"))
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("(1) Resumen de hoy")
            print("(2) Resumen de otro día")
            print("(0) Regresar al menú principal")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("")
            while True:
                try:
                    opcion = int(input("Ingrese el número de la opción que desea: "))
                    break
                except Exception:
                    print(colores.red("Este campo solo acepta valores numéricos"))
            print("")
            if opcion == 0:
                break
            elif opcion == 1:
                resumen = Resumen()
                resumen.imprimeResumenActual(idUsuario)
            elif opcion == 2:
                resumen = Resumen()
                resumen.imprimeResumenOtroDia(idUsuario)
    elif eleccion == 2:
        medidas = Medidas()
        while True:
            print("")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print(colores.blue("MENÚ DE INGRESO DE MEDIDAS"))
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("(1) Ingresar peso del día")
            print("(2) Ingresar registro de cintura")
            print("(3) Ingresar registro de cuello")
            print("(0) Regresar al menú principal")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("")
            while True:
                try:
                    opcion = int(input("Ingrese el número de la opción que desea: "))
                    break
                except Exception:
                    print(colores.red("Este campo solo acepta valores numéricos"))
            print("")
            if opcion == 0:
                break
            elif opcion == 1:
                medidas.ingresarPeso(idUsuario)
            elif opcion == 2:
                medidas.ingresarCintura(idUsuario)
            elif opcion == 3:
                medidas.ingresarCuello(idUsuario)
    elif eleccion == 3:
        objetivos = Objetivos()
        while True:
            print("")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print(colores.blue("MENÚ DE OBJETIVOS"))
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("(1) Mostrar objetivos")
            print("(2) Agregar objetivos")
            print("(3) Modificar objetivos")
            print("(4) Eliminar objetivos")
            print("(0) Regresar al menú principal")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("")
            while True:
                try:
                    opcion = int(input("Ingrese el número de la opción que desea: "))
                    break
                except Exception:
                    print(colores.red("Este campo solo acepta valores numéricos"))
            print("")
            if opcion == 0:
                break
            elif opcion == 1:
                objetivos.mostrarObjetivos()
            elif opcion == 2:
                objetivos.agregarObjetivos()
            elif opcion == 3:
                objetivos.modificarObjetivos()
            elif opcion == 4:
                objetivos.eliminarObjetivos()
    elif eleccion == 4:
        alimentacion = Alimentacion(idUsuario)
        while True:
            print("")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print(colores.blue("MENÚ DE REGISTROS DE ALIMENTOS"))
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("(1) Agregar alimento")
            print("(2) Buscar alimento")
            print("(3) Crear receta")
            print("(0) Regresar al menú principal")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("")
            while True:
                try:
                    opcion = int(input("Ingrese el número de la opción que desea: "))
                    break
                except Exception:
                    print("")
                    print(colores.red("Este campo solo acepta valores numéricos"))
                    print("")
            print("")
            if opcion == 0:
                break
            elif opcion == 1:
                alimento = alimentacion.agregarAlimento()

                if alimento:
                    print("")
                    print(colores.green("Alimento registrado correctamente"))
                else:
                    alimentacion.buscarAlimento()

            elif opcion == 2:
                alimentacion.buscarAlimento()
            elif opcion == 3:
                alimentacion.crearReceta()
    elif eleccion == 5:
        ejercicio = Ejercicio(idUsuario)
        while True:
            print("")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print(colores.blue("MENÚ DE REGISTROS DE EJERCICIOS"))
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("(1) Agregar ejercicio de cardio")
            print("(2) Buscar ejercicio de cardio")
            print("(3) Crear ejercicio de cardio")
            print("(4) Agregar ejercicio de peso")
            print("(5) Buscar ejercicio de peso")
            print("(6) Crear ejercicio de peso")
            print("(0) Regresar al menú principal")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("")
            while True:
                try:
                    opcion = int(input("Ingrese el número de la opción que desea: "))
                    break
                except Exception:
                    print(colores.red("Este campo solo acepta valores numéricos"))
            print("")
            if opcion == 0:
                break
            elif opcion == 1:

                ejer = ejercicio.agregarCardio()

                if ejer:
                    print("")
                    print(colores.green("Ejercicio registrado correctamente"))
                else:
                    ejercicio.buscarCardio()

            elif opcion == 2:
                ejercicio.buscarCardio()

            elif opcion == 3:
                ejercicio.crearCardio()

            elif opcion == 4:

                ejer = ejercicio.agregarPeso()

                if ejer:
                    print("")
                    print(colores.green("Ejercicio registrado correctamente"))
                else:
                    ejercicio.buscarPeso()

            elif opcion == 5:
                ejercicio.buscarPeso()
            elif opcion == 6:
                ejercicio.crearPeso()
    elif eleccion == 6:
        evolucion = Evolucion()
        while True:
            print("")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print(colores.blue("MENÚ DE EVOLUCIÓN DE PROGRESO"))
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("(1) Evolución de mi peso")
            print("(2) Evolución de cintura")
            print("(3) Evolución de cuello")
            print("(4) Calorías consumidas")
            print("(5) Calorías quemadas")
            print("(6) Parámetro para peso")
            print("(0) Regresar al menú principal")
            print(
                colores.cyan("-------------------------------------------------------")
            )
            print("")
            while True:
                try:
                    opcion = int(input("Ingrese el número de la opción que desea: "))
                    break
                except Exception:
                    print(colores.red("Este campo solo acepta valores numéricos"))
            print("")
            if opcion == 0:
                break
            elif opcion == 1:
                evolucion.evoPeso(idUsuario)
            elif opcion == 2:
                evolucion.evoCintura(idUsuario)
            elif opcion == 3:
                evolucion.evoCuello(idUsuario)
            elif opcion == 4:
                evolucion.evoCalConsumidas(idUsuario)
            elif opcion == 5:
                evolucion.evoCalQuemadas(idUsuario)
            elif opcion == 6:
                evolucion.evoEjPeso(idUsuario)
            elif opcion == 7:
                evolucion.evoTiempo(idUsuario)


print(colores.green("Finalizando app..."))
