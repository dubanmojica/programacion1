 Operaciones con Matrices
Este un  programa en Python para realizar cálculos de matrices.
1. Descargue todos los archivos `.py` de este repositorio en una misma carpeta.
2. Abra python o consola de comandos.
3. Ejecute el archivo principal con el comando:
   `python main.py`

ahi encontraras las siguientes operaciones
Contiene las funciones matemáticas:
* **Suma**: Suma de matrices de igual dimensión.
* **Multiplicación**: Producto de matrices (filas por columnas).
* **Hadamard**: Producto elemento a elemento.
* **Kronecker**: Producto tensorial que resulta en una matriz de mayor tamaño.

la estructura del programa consta de los siguientes puntos.
* `main.py`: Punto de entrada del programa.
* `entrada.py`: Manejo de lectura y validación de datos.
* `menu.py`: participacion del usuario en la consola.
* `operaciones_matrices.py`: Lógica matemática.
* main: Contiene el archivo principal `main.py` 
* entrada: Contiene el módulo `entrada.py` 
* operaciones: Contiene el módulo `operaciones_matrices.py`
* menu: Contiene el módulo `menu.py` 
1. main.py
Es el punto de entrada. Importa los demás módulos y contiene el bucle principal que seria while True:
  mantiene el programa en ejecución hasta que el usuario decide salir que seria si pusiera el valor de 5.
2. entrada.py
Se encarga de toda la interacción de datos:
* `ingresar_matriz()`: Solicita a la persona que ingrese los datos de la matriz, validando que no se ingresen letras.
* `mostrar_matriz()`: Imprime las matrices de forma organizada en la consola.
3.`operaciones_matrices.py ` es el punto donde se encuentran las operaciones del programa las cuales estan enumeradas para que el usuario escoja la que necesita.
4. `menu.py: ` Gestiona la visualización de las opciones en la consola y la muestra de la selección del usuario.

