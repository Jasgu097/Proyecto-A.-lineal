def pedir_matriz(filas):
    matriz = []
    print("Introduce los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(filas):
            fila.append(float(input("Introduce el elemento [{}, {}]: ".format(i, j))))
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    suma = []
    for i in range(len(matriz1)):
        fila_suma = []
        for j in range(len(matriz1)):
            fila_suma.append(matriz1[i][j] + matriz2[i][j])
        suma.append(fila_suma)
    return suma

def restar_matrices(matriz1, matriz2):
    resta = []
    for i in range(len(matriz1)):
        fila_resta = []
        for j in range(len(matriz1)):
            fila_resta.append(matriz1[i][j] - matriz2[i][j])
        resta.append(fila_resta)
    return resta

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    filas = int(input("Introduce el número de filas y columnas de las matrices: "))

    print("\nIngrese la primera matriz:")
    matriz1 = pedir_matriz(filas)

    print("\nIngrese la segunda matriz:")
    matriz2 = pedir_matriz(filas)

    print("\nMatriz 1:")
    mostrar_matriz(matriz1)
    print("\nMatriz 2:")
    mostrar_matriz(matriz2)

    while True:
        print("\nIngrese una opcion:")
        print("1. Suma de matrices")
        print("2. Resta de matrices")
        print("3. Salir")
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
            print("Regresando al menu principal")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


main()
