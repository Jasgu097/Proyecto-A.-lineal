import numpy as np


def inversa_matriz(matriz):
    try:
        matriz_np = np.array(matriz)
        inversa_np = np.linalg.inv(matriz_np)
        inversa = inversa_np.tolist()
        return inversa
    except np.linalg.LinAlgError:
        return "No se puede calcular la inversa de una matriz singular."


def transpuesta_matriz(matriz):
    transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
    return transpuesta

matriz_usuario = []

for i in range(3):
    fila = input(f"Ingrese los 3 números de la columna {i + 1}: ").split()
    fila = [int(num) for num in fila]
    matriz_usuario.append(fila)

inversa_usuario = inversa_matriz(matriz_usuario)
print("Inversa de la matriz proporcionada por el usuario:")
transpuesta_a=transpuesta_matriz(inversa_usuario)
for i in transpuesta_a:
    print(i)
print("__________________")