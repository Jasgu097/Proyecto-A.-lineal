import numpy as np  # Importamos numpy para calcular la inversa de la matriz

class Codificacion:
    def __init__(self):
        self.conteo = 0

    def nombre_a_matriz(self, nombre):
        matriz = []
        for letra in nombre:
            if letra == ' ':
                matriz.append(27)  # Espacio en blanco corresponde a 27
            else:
                # Restamos el código ASCII de 'a' (97) para obtener la posición relativa de la letra en el alfabeto
                numero_letra = ord(letra.lower()) - 96
                matriz.append(numero_letra)

        # Llenar con espacios en blanco si es necesario para que la matriz tenga 3 filas
        while len(matriz) % 3 != 0:
            matriz.append(27)

        # Crear la matriz de 3 filas
        matriz_3_filas = [matriz[i:i + 3] for i in range(0, len(matriz), 3)]

        self.conteo = len(matriz_3_filas)  # Actualizar el conteo de filas
        return matriz_3_filas

    def multiplicar_matrices(self, matriz1, matriz2):
        resultado = []
        for i in range(self.conteo):
            fila = []
            for j in range(3):
                suma = 0
                for k in range(3):
                    suma += matriz1[i][k] * matriz2[k][j]
                fila.append(suma)
            resultado.append(fila)
        return resultado

    def inversa_matriz(self, matriz):
        try:
            matriz_np = np.array(matriz)
            inversa_np = np.linalg.inv(matriz_np)
            inversa = inversa_np.tolist()
            return inversa
        except np.linalg.LinAlgError:
            return "No se puede calcular la inversa de una matriz singular."

    def transpuesta_matriz(self, matriz):
        transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
        return transpuesta

codificador = Codificacion()

nombre_usuario = input("Ingrese un nombre: ")
matriz_nombre = codificador.nombre_a_matriz(nombre_usuario)
"""
for i in matriz_nombre:
    print(i)
print("Ingrese una matriz de 3x3, separando los números por espacios:")
"""

matriz_usuario = []

for i in range(3):
    fila = input(f"Ingrese los 3 números de la columna {i + 1}: ").split()
    fila = [int(num) for num in fila]
    matriz_usuario.append(fila)


a=Codificacion()
transpuesta_a=a.transpuesta_matriz(matriz_nombre)
print("Matriz de nombre a numeros:")
for i in transpuesta_a:
    print(i)
print("___________________")

resultado_multiplicacion = codificador.multiplicar_matrices(matriz_nombre, matriz_usuario)
"""
print("Matriz resultante de la multiplicación:")
for fila in resultado_multiplicacion:
    print(fila)
"""
transpuesta_a=a.transpuesta_matriz(resultado_multiplicacion)
print("Resultado de la multiplicacion de la clave con la matriz nombre: ")
for i in transpuesta_a:
    print(i)
print("___________________")
# Calculamos la inversa de la matriz proporcionada por el usuario
inversa_usuario = codificador.inversa_matriz(matriz_usuario)
print("Inversa de la matriz proporcionada por el usuario:")
transpuesta_a=a.transpuesta_matriz(inversa_usuario)
for i in transpuesta_a:
    print(i)
print("__________________")
"""
if isinstance(inversa_usuario, str):
    print(inversa_usuario)
else:
    for fila in inversa_usuario:
        print(fila)
"""

# Multiplicamos la inversa de la matriz del usuario con el resultado de la primera multiplicación
if not isinstance(inversa_usuario, str):
    resultado_final = codificador.multiplicar_matrices(resultado_multiplicacion,inversa_usuario)
    print("Matriz resultante de la multiplicación entre la inversa de la matriz usuario y el resultado de la primera multiplicación:")
    transpuesta_a=a.transpuesta_matriz(resultado_final)
    """
    for fila in resultado_final:
        print(fila)
    """
    for i in transpuesta_a:
        print(i)
    print("__________________")
