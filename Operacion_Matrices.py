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
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            elemento = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(elemento)
        resultado.append(fila_resultado)
    return resultado

def restar_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            elemento = matriz1[i][j] - matriz2[i][j]
            fila_resultado.append(elemento)
        resultado.append(fila_resultado)
    return resultado

def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        messagebox.showerror("Error", "No se puede realizar la multiplicación. El número de columnas de la matriz 1 no coincide con el número de filas de la matriz 2.")
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
    return "\n".join(["\t".join(map(str, fila)) for fila in matriz])

def mostrar_proceso(operacion, matriz1, matriz2, resultado):
    ventana_proceso = tk.Toplevel()
    ventana_proceso.title(f"Proceso de {operacion} de matrices")
    ventana_proceso.geometry("800x600")

    label_matriz1 = tk.Label(ventana_proceso, text=f"Matriz 1:\n{mostrar_matriz(matriz1)}", justify=tk.LEFT)
    label_matriz1.pack(pady=10)

    label_matriz2 = tk.Label(ventana_proceso, text=f"Matriz 2:\n{mostrar_matriz(matriz2)}", justify=tk.LEFT)
    label_matriz2.pack(pady=10)

    label_proceso = tk.Label(ventana_proceso, text="Proceso:", justify=tk.LEFT)
    label_proceso.pack(pady=10)

    canvas = tk.Canvas(ventana_proceso, width=600, height=300, bg="white")
    canvas.pack()

    if operacion == 'sumar':
        for i in range(len(matriz1)):
            for j in range(len(matriz1[0])):
                canvas.create_text(50 + j * 100, 50 + i * 30, text=f"{matriz1[i][j]} + {matriz2[i][j]} = {resultado[i][j]}", anchor=tk.W)
    elif operacion == 'restar':
        for i in range(len(matriz1)):
            for j in range(len(matriz1[0])):
                canvas.create_text(50 + j * 100, 50 + i * 30, text=f"{matriz1[i][j]} - {matriz2[i][j]} = {resultado[i][j]}", anchor=tk.W)
    elif operacion == 'multiplicar':
        k = 0
        for i in range(len(matriz1)):
            for j in range(len(matriz2[0])):
                canvas.create_text(50, 50 + k * 30, text=f"{matriz1[i][0]} * {matriz2[0][j]}", anchor=tk.W)
                for l in range(1, len(matriz2)):
                    canvas.create_text(150 + (l - 1) * 100, 50 + k * 30, text=f"+ {matriz1[i][l]} * {matriz2[l][j]}", anchor=tk.W)
                canvas.create_text(550, 50 + k * 30, text=f"= {resultado[i][j]}", anchor=tk.W)
                k += 1

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
                messagebox.showerror("Error", "El número de columnas de la matriz 1 debe ser igual al número de filas de la matriz 2 para multiplicar.")
                return
            resultado = multiplicar_matrices(matriz1, matriz2)
        else:
            resultado = None

        if resultado is not None:
            resultado_str = mostrar_matriz(resultado)
            messagebox.showinfo("Resultado", f"Matriz resultante:\n{resultado_str}")
            mostrar_proceso(operacion, matriz1, matriz2, resultado)

    tk.Label(ventana_operaciones, text="Matriz 1:").pack()
    tk.Label(ventana_operaciones, text=mostrar_matriz(matriz1)).pack()

    tk.Label(ventana_operaciones, text="Matriz 2:").pack()
    tk.Label(ventana_operaciones, text=mostrar_matriz(matriz2)).pack()

    tk.Button(ventana_operaciones, text="Suma de matrices", command=lambda: realizar_operacion('sumar')).pack(pady=5)
    tk.Button(ventana_operaciones, text="Resta de matrices", command=lambda: realizar_operacion('restar')).pack(pady=5)
    tk.Button(ventana_operaciones, text="Multiplicación de matrices", command=lambda: realizar_operacion('multiplicar')).pack(pady=5)
    tk.Button(ventana_operaciones, text="Salir", command=ventana_operaciones.destroy).pack(pady=20)