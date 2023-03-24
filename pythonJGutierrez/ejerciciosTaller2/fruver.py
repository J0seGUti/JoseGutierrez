print("Control de fruver")
Fruver = {}

while True:
    print("\n1. Agregar/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la fruta: ")
        while True:
            try:
                precio = float(input("Ingrese el precio de la fruta: "))
                break
            except ValueError:
                print("Precio no válido. Ingrese un valor numérico.")

        if nombre in Fruver:
            print(f"La fruta '{nombre}' ya se encuentra registrada con un precio de {Fruver[nombre]}")
        else:
            Fruver[nombre] = precio
            print(f"La fruta '{nombre}' ha sido agregada con un precio de {precio}")

    elif opcion == "2":
        busqueda = input("Ingrese un texto de búsqueda: ")
        resultados = [nombre for nombre in Fruver if nombre.startswith(busqueda)]
        if resultados:
            print(f"Resultados de la búsqueda '{busqueda}':")
            for nombre in resultados:
                print(f"{nombre}: {Fruver[nombre]}")
        else:
            print(f"No se encontraron frutas que comiencen con '{busqueda}'")

    elif opcion == "3":
        nombre = input("Ingrese el nombre de la fruta a borrar: ")
        if nombre in Fruver:
            while True:
                confirmacion = input(f"¿Está seguro que desea borrar '{nombre}'? (s/n): ")
                if confirmacion.lower() == "s" or confirmacion.lower() == "n":
                    break
                else:
                    print("Respuesta no válida. Ingrese 's' o 'n' en minúsculas.")
            if confirmacion.lower() == "s":
                del Fruver[nombre]
                print(f"La fruta '{nombre}' ha sido borrada")
            else:
                print(f"No se ha borrado la fruta '{nombre}'")
        else:
            print(f"No se encontró la fruta '{nombre}'")

    elif opcion == "4":
        if Fruver:
            print("Lista de frutas:")
            for nombre, precio in Fruver.items():
                print(f"{nombre}: {precio}")
        else:
            print("No hay frutas registradas")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, seleccione nuevamente")
