import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox


def pedir_matriz(root, filas, columnas):
    ventana_entradas = tk.Toplevel(root)
    ventana_entradas.title(f"Ingresar Matriz de {filas}x{columnas}")
    ventana_entradas.geometry("400x400")

    entradas = []
    frame_entradas = tk.Frame(ventana_entradas)
    frame_entradas.pack(pady=10)

    for i in range(filas):
        fila = []
        for j in range(columnas):
            entrada = tk.Entry(frame_entradas, width=5)
            entrada.grid(row=i, column=j, padx=5, pady=5)
            fila.append(entrada)
        entradas.append(fila)

    matriz = []

    def obtener_valores():
        nonlocal matriz
        matriz = []
        for fila in entradas:
            matriz_fila = []
            for entrada in fila:
                valor = entrada.get()
                if valor:
                    matriz_fila.append(float(valor))
                else:
                    matriz_fila.append(0.0)
            matriz.append(matriz_fila)
        ventana_entradas.destroy()

    tk.Button(ventana_entradas, text="Aceptar", command=obtener_valores).pack(pady=20)
    ventana_entradas.wait_window()

    return matriz


def sumar_matrices(matriz1, matriz2):
    return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]


def restar_matrices(matriz1, matriz2):
    return [[matriz1[i][j] - matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]


def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        messagebox.showerror("Error",
                             "No se puede realizar la multiplicación. El número de columnas de la matriz 1 no coincide con el número de filas de la matriz 2.")
        return None
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz2[0])):
            elemento = sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2)))
            fila_resultado.append(elemento)
        resultado.append(fila_resultado)
    return resultado


def mostrar_matriz(matriz):
    return "\n".join(["\t".join(map(str, fila)) for fila in matriz])


def operaciones_matrices(root):
    filas1 = simpledialog.askinteger("Entrada", "Ingrese el número de filas de la matriz 1:", parent=root)
    columnas1 = simpledialog.askinteger("Entrada", "Ingrese el número de columnas de la matriz 1:", parent=root)
    matriz1 = pedir_matriz(root, filas1, columnas1)

    filas2 = simpledialog.askinteger("Entrada", "Ingrese el número de filas de la matriz 2:", parent=root)
    columnas2 = simpledialog.askinteger("Entrada", "Ingrese el número de columnas de la matriz 2:", parent=root)
    matriz2 = pedir_matriz(root, filas2, columnas2)

    ventana_operaciones = tk.Toplevel(root)
    ventana_operaciones.title("Operaciones con Matrices")
    ventana_operaciones.geometry("400x400")

    def realizar_operacion(operacion):
        if operacion == 'sumar':
            if filas1 != filas2 or columnas1 != columnas2:
                messagebox.showerror("Error", "Las matrices deben tener el mismo tamaño para sumar.")
                return
            resultado = sumar_matrices(matriz1, matriz2)
        elif operacion == 'restar':
            if filas1 != filas2 or columnas1 != columnas2:
                messagebox.showerror("Error", "Las matrices deben tener el mismo tamaño para restar.")
                return
            resultado = restar_matrices(matriz1, matriz2)
        elif operacion == 'multiplicar':
            if columnas1 != filas2:
                messagebox.showerror("Error",
                                     "El número de columnas de la matriz 1 debe ser igual al número de filas de la matriz 2 para multiplicar.")
                return
            resultado = multiplicar_matrices(matriz1, matriz2)
        else:
            resultado = None

        if resultado is not None:
            resultado_str = mostrar_matriz(resultado)
            messagebox.showinfo("Resultado", f"Matriz resultante:\n{resultado_str}")

    tk.Label(ventana_operaciones, text="Matriz 1:").pack()
    tk.Label(ventana_operaciones, text=mostrar_matriz(matriz1)).pack()

    tk.Label(ventana_operaciones, text="Matriz 2:").pack()
    tk.Label(ventana_operaciones, text=mostrar_matriz(matriz2)).pack()

    tk.Button(ventana_operaciones, text="Suma de matrices", command=lambda: realizar_operacion('sumar')).pack(pady=5)
    tk.Button(ventana_operaciones, text="Resta de matrices", command=lambda: realizar_operacion('restar')).pack(pady=5)
    tk.Button(ventana_operaciones, text="Multiplicación de matrices",
              command=lambda: realizar_operacion('multiplicar')).pack(pady=5)
    tk.Button(ventana_operaciones, text="Salir", command=ventana_operaciones.destroy).pack(pady=20)
