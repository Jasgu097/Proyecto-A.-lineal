def pedir_matriz(filas, columnas):
    matriz = []
    print("Introduce los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(float(input("Introduce el elemento [{}, {}]: ".format(i, j))))
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    suma = []
    for i in range(len(matriz1)):
        fila_suma = []
        for j in range(len(matriz1[0])):
            fila_suma.append(matriz1[i][j] + matriz2[i][j])
        suma.append(fila_suma)
    return suma

def restar_matrices(matriz1, matriz2):
    resta = []
    for i in range(len(matriz1)):
        fila_resta = []
        for j in range(len(matriz1[0])):
            fila_resta.append(matriz1[i][j] - matriz2[i][j])
        resta.append(fila_resta)
    return resta

def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        print("No se puede realizar la multiplicación. El número de columnas de la matriz 1 no coincide con el número de filas de la matriz 2.")
        return None

    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz2[0])):
            elemento = 0
            for k in range(len(matriz2)):
                elemento += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(elemento)
        resultado.append(fila_resultado)
    return resultado

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    filas1 = int(input("Ingrese el número de filas de la matriz 1: "))
    columnas1 = int(input("Ingrese el número de columnas de la matriz 1: "))

    print("\nIngrese la matriz 1:")
    matriz1 = pedir_matriz(filas1, columnas1)

    filas2 = int(input("\nIngrese el número de filas de la matriz 2: "))
    columnas2 = int(input("Ingrese el número de columnas de la matriz 2: "))

    print("\nIngrese la matriz 2:")
    matriz2 = pedir_matriz(filas2, columnas2)

    print("\nMatriz 1:")
    mostrar_matriz(matriz1)
    print("\nMatriz 2:")
    mostrar_matriz(matriz2)

    while True:
        print("\nSelecciona la operación:")
        print("1. Suma de matrices")
        print("2. Resta de matrices")
        print("3. Multiplicación de matrices")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            print("\nSumando las matrices...")
            resultado = sumar_matrices(matriz1, matriz2)
            print("\nMatriz resultante:")
            mostrar_matriz(resultado)
        elif opcion == '2':
            print("\nRestando las matrices...")
            resultado = restar_matrices(matriz1, matriz2)
            print("\nMatriz resultante:")
            mostrar_matriz(resultado)
        elif opcion == '3':
            print("\nMultiplicando las matrices...")
            resultado = multiplicar_matrices(matriz1, matriz2)
            if resultado:
                print("\nMatriz resultante:")
                mostrar_matriz(resultado)
        elif opcion == '4':
            print("Regresando al menu principal")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


main()
