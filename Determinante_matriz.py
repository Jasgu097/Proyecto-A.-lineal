import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np

def calcular_determinante(matriz):
    try:
        return np.linalg.det(matriz)
    except np.linalg.LinAlgError:
        return None

def obtener_matriz_cuadrada():
    n = int(simpledialog.askstring("Input", "Ingrese el tamaño de la matriz (n x n):"))

    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            elemento = float(simpledialog.askstring("Input", f"Ingrese el elemento ({i + 1},{j + 1}):"))
            fila.append(elemento)
        matriz.append(fila)

    matriz = np.array(matriz)
    return matriz

def mostrar_determinante():
    matriz = obtener_matriz_cuadrada()
    determinante = calcular_determinante(matriz)
    if determinante is not None:
        messagebox.showinfo("Determinante de la Matriz", f"El determinante de la matriz es: {determinante:.4f}")
    else:
        messagebox.showerror("Error", "No se pudo calcular el determinante de la matriz.")

def determinante_matriz(root):
    root.withdraw()  # Oculta la ventana principal
    if messagebox.askyesno("Determinante de una Matriz", "¿Desea calcular el determinante de una matriz cuadrada?"):
        mostrar_determinante()
    root.deiconify()  # Muestra la ventana principal nuevamente
