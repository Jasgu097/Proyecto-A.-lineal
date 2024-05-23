import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np

def obtener_matriz():
    matriz = []
    for i in range(3):
        fila = simpledialog.askstring("Entrada", f"Ingrese los 3 números de la fila {i + 1}:").split()
        fila = [float(num) for num in fila]
        matriz.append(fila)
    return matriz

def gauss_jordan(matriz):
    n = len(matriz)
    augmented_matrix = np.hstack((matriz, np.eye(n)))  # Matriz aumentada [A | I]

    for i in range(n):
        # Pivoteamos
        pivot_row = max(range(i, n), key=lambda j: abs(augmented_matrix[j, i]))
        augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]

        # Convertimos el pivote en 1
        pivot = augmented_matrix[i, i]
        augmented_matrix[i] /= pivot

        # Eliminación gaussiana
        for j in range(n):
            if i != j:
                ratio = augmented_matrix[j, i]
                augmented_matrix[j] -= ratio * augmented_matrix[i]

    return augmented_matrix[:, n:]  # Obtenemos la parte derecha de la matriz resultante

def calcular_inversa():
    matriz = obtener_matriz()  # Solicitar la matriz al usuario
    inversa = gauss_jordan(matriz)  # Calcular la inversa
    inversa_str = "\n".join(["\t".join(map(str, fila)) for fila in inversa])  # Convertir la inversa a cadena de texto
    messagebox.showinfo("Inversa de la Matriz", f"La inversa de la matriz es:\n\n{inversa_str}")  # Mostrar la inversa

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    calcular_inversa()
