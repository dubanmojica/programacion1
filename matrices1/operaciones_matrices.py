def sumar_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error: Las matrices deben tener las mismas dimensiones.")
        return None
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        print("Error: Columnas de A deben coincidir con filas de B.")
        return None
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

def hadamard(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error: Las dimensiones deben ser iguales para el producto Hadamard.")
        return None
    return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def kronecker(A, B):
    filas_A, col_A = len(A), len(A[0])
    filas_B, col_B = len(B), len(B[0])
    resultado = [[0 for _ in range(col_A * col_B)] for _ in range(filas_A * filas_B)]
    
    for i in range(filas_A):
        for j in range(col_A):
            for k in range(filas_B):
                for l in range(col_B):
                    resultado[i * filas_B + k][j * col_B + l] = A[i][j] * B[k][l]
    return resultado
