import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

def inversa_matriz(matriz):
    try:
        matriz_np = np.array(matriz)
        inversa_np = np.linalg.inv(matriz_np)
        inversa = inversa_np.tolist()
        inversa_redondeada = [[round(elemento, 4) for elemento in fila] for fila in inversa]
        return inversa_redondeada
    except np.linalg.LinAlgError:
        return "No se puede calcular la inversa de una matriz singular."

def matriz_inversa(root):
    ventana_inversa = tk.Toplevel(root)
    ventana_inversa.title("Calcular Inversa de una Matriz")
    ventana_inversa.geometry("400x400")

    tk.Label(ventana_inversa, text="Ingrese los elementos de la matriz 3x3:").pack(pady=10)

    entradas = []
    frame_entradas = tk.Frame(ventana_inversa)
    frame_entradas.pack(pady=10)

    for i in range(3):
        fila = []
        for j in range(3):
            entrada = tk.Entry(frame_entradas, width=5)
            entrada.grid(row=i, column=j, padx=5, pady=5)
            fila.append(entrada)
        entradas.append(fila)

    def calcular_inversa():
        matriz_usuario = []
        for fila in entradas:
            matriz_fila = []
            for entrada in fila:
                matriz_fila.append(float(entrada.get()))
            matriz_usuario.append(matriz_fila)

        inversa_usuario = inversa_matriz(matriz_usuario)
        if isinstance(inversa_usuario, str):
            messagebox.showinfo("Resultado", inversa_usuario)
        else:
            resultado_str = "\n".join(["\t".join(map(str, fila)) for fila in inversa_usuario])
            messagebox.showinfo("Resultado", f"Inversa de la matriz:\n{resultado_str}")

    tk.Button(ventana_inversa, text="Calcular Inversa", command=calcular_inversa).pack(pady=20)
    tk.Button(ventana_inversa, text="Salir", command=ventana_inversa.destroy).pack(pady=10)
