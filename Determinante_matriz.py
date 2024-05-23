import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np


def calcular_determinante_sarrus(matriz):
    if matriz.shape == (3, 3):
        # Expansión por el método de Sarrus
        determinante = (
                matriz[0, 0] * matriz[1, 1] * matriz[2, 2] +
                matriz[0, 1] * matriz[1, 2] * matriz[2, 0] +
                matriz[0, 2] * matriz[1, 0] * matriz[2, 1] -
                matriz[0, 2] * matriz[1, 1] * matriz[2, 0] -
                matriz[0, 1] * matriz[1, 0] * matriz[2, 2] -
                matriz[0, 0] * matriz[1, 2] * matriz[2, 1]
        )

        # Procesos para mostrar
        procesos = [
            f"{matriz[0, 0]} * {matriz[1, 1]} * {matriz[2, 2]} = {matriz[0, 0] * matriz[1, 1] * matriz[2, 2]:.4f}",
            f"{matriz[0, 1]} * {matriz[1, 2]} * {matriz[2, 0]} = {matriz[0, 1] * matriz[1, 2] * matriz[2, 0]:.4f}",
            f"{matriz[0, 2]} * {matriz[1, 0]} * {matriz[2, 1]} = {matriz[0, 2] * matriz[1, 0] * matriz[2, 1]:.4f}",
            f"- {matriz[0, 2]} * {matriz[1, 1]} * {matriz[2, 0]} = {-matriz[0, 2] * matriz[1, 1] * matriz[2, 0]:.4f}",
            f"- {matriz[0, 1]} * {matriz[1, 0]} * {matriz[2, 2]} = {-matriz[0, 1] * matriz[1, 0] * matriz[2, 2]:.4f}",
            f"- {matriz[0, 0]} * {matriz[1, 2]} * {matriz[2, 1]} = {-matriz[0, 0] * matriz[1, 2] * matriz[2, 1]:.4f}",
        ]

        return determinante, procesos
    else:
        return None, ["El método de Sarrus solo se aplica a matrices 3x3."]


def obtener_matriz_cuadrada():
    n = int(simpledialog.askstring("Entrada", "Ingrese el tamaño de la matriz (n x n):"))

    if n != 3:
        messagebox.showerror("Error", "El método de Sarrus solo se aplica a matrices 3x3.")
        return None

    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            elemento = float(simpledialog.askstring("Entrada", f"Ingrese el elemento ({i + 1},{j + 1}):"))
            fila.append(elemento)
        matriz.append(fila)

    matriz = np.array(matriz)
    return matriz


def mostrar_determinante():
    matriz = obtener_matriz_cuadrada()
    if matriz is not None:
        determinante, procesos = calcular_determinante_sarrus(matriz)
        if determinante is not None:
            proceso_texto = "\n".join(procesos)
            messagebox.showinfo("Determinante de la Matriz",
                                f"El determinante de la matriz es: {determinante:.4f}\n\nProcesos:\n{proceso_texto}")
        else:
            messagebox.showerror("Error", "No se pudo calcular el determinante de la matriz.")


def determinante_matriz(root):
    root.withdraw()  # Oculta la ventana principal
    if messagebox.askyesno("Determinante de una Matriz", "¿Desea calcular el determinante de una matriz 3x3?"):
        mostrar_determinante()
    root.deiconify()  # Muestra la ventana principal nuevamente


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculadora de Determinante")
    root.geometry("300x150")

    btn_calcular = tk.Button(root, text="Calcular Determinante", command=lambda: determinante_matriz(root))
    btn_calcular.pack(pady=20)

    root.mainloop()