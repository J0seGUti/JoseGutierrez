baul = []

while True:
    print("\n¿Qué te gustaría hacer?")
    print("1. Agregar un artículo al baúl")
    print("2. Listar los artículos del baúl")
    print("3. Eliminar el último artículo de la lista")
    print("4. Eliminar un artículo del baúl")
    print("5. Salir")

    opcion = int(input("Por favor ingrese una opción (1-5): "))

    if opcion == 1:
        articulo = input("\nIngrese el nombre del artículo a agregar: ")
        baul.append(articulo)
        print("\nEl artículo", articulo, "ha sido agregado al baúl.")

    elif opcion == 2:
        if not baul:
            print("\nEl baúl está vacío.")
        else:
            print("\nArtículos en el baúl:")
            for i, articulo in enumerate(baul, start=1):
                print(i, ".", articulo)

    elif opcion == 3:
        if not baul:
            print("\nEl baúl ya está vacío.")
        else:
            ultimo_articulo = baul.pop()
            print("\nEl artículo", ultimo_articulo, "ha sido eliminado del baúl.")

    elif opcion == 4:
        if not baul:
            print("\nEl baúl está vacío.")
        else:
            print("\nArtículos en el baúl:")
            for i, articulo in enumerate(baul, start=1):
                print(i, ".", articulo)
            indice = int(input("\nIngrese el número del artículo a borrar: "))
            if 1 <= indice <= len(baul):
                articulo_borrado = baul.pop(indice-1)
                print("\nEl artículo", articulo_borrado, "ha sido eliminado del baúl.")
            else:
                print("\nEl número de artículo ingresado es inválido.")

    elif opcion == 5:
        print("Gracias por utilizar el baúl.")
        break

    else:
        print("La opción ingresada no es válida. Por favor, intente nuevamente.")
