def mostrar_menu():
    print("\n" + "-"*10 + " MENU DE OPERACIONES CON MATRICES " + "-"*10)
    print("1. Suma de matrices")
    print("2. Multiplicación de matrices")
    print("3. Producto de Hadamard")
    print("4. Producto de Kronecker")
    print("5. Salir")
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion in [1, 2, 3, 4, 5]:
                return opcion
            else:
                print("Error: Opción no válida.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")
