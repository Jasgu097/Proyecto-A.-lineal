import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np

def calcular_rango(matriz):
    return np.linalg.matrix_rank(matriz)

def obtener_matriz():
    filas = int(simpledialog.askstring("Input", "Ingrese el número de filas:"))
    columnas = int(simpledialog.askstring("Input", "Ingrese el número de columnas:"))

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(simpledialog.askstring("Input", f"Ingrese el elemento ({i + 1},{j + 1}):"))
            fila.append(elemento)
        matriz.append(fila)

    matriz = np.array(matriz)
    return matriz

def mostrar_rango():
    matriz = obtener_matriz()
    rango = calcular_rango(matriz)
    messagebox.showinfo("Rango de la Matriz", f"El rango de la matriz es: {rango}")

def rango_matriz(root):
    root.withdraw()  # Oculta la ventana principal
    if messagebox.askyesno("Rango de una Matriz", "¿Desea calcular el rango de una matriz?"):
        mostrar_rango()
    root.deiconify()  # Muestra la ventana principal nuevamente
