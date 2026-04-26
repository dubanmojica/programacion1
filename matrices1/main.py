import entrada
import operaciones_matrices
import menu
def ejecut ar():
    while True:
        opcion = menu.mostrar_menu()
        if opcion == 5:
            print("\nSaliendo del programa... ¡Hasta pronto!")
            break
        print("\n--- Ingrese los datos para la Matriz A ---")
        matriz_a = entrada.ingresar_matriz()
        print("\n--- Ingrese los datos para la Matriz B ---")
        matriz_b = entrada.ingresar_matriz()
        resultado = None
        if opcion == 1:
            resultado = operaciones_matrices.sumar_matrices(matriz_a, matriz_b)
        elif opcion == 2:
            resultado = operaciones_matrices.multiplicar_matrices(matriz_a, matriz_b)
        elif opcion == 3:
            resultado = operaciones_matrices.hadamard(matriz_a, matriz_b)
        elif opcion == 4:
            resultado = operaciones_matrices.kronecker(matriz_a, matriz_b)
        if resultado is not None:
            print("\n" + "="*25)
            print("RESULTADO DE LA OPERACIÓN:")
            entrada.mostrar_matriz(resultado)
            print("="*25)
        else:
            print("\n[!] No se pudo mostrar el resultado debido a un error en las dimensiones.")
if __name__ == "__main__":
    ejecutar()
