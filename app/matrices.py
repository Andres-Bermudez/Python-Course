""" Matrices """

matrizA = [[2, 4, 6],
           [1, 3, 5],
           [7, 8, 9]]

matrizB = [[5, 7, 8],
           [9, 6, 2]]

filaA = int(input("Ingresa la fila de A: "))
columnaA = int(input("Ingresa la columna A: "))
print()
filaB = int(input("Ingresa la fila de B: "))
columnaB = int(input("Ingresa la columna B: "))

result = matrizA[filaA][columnaA] * matrizB[filaB][columnaB]

print(f"Result: {result}")
