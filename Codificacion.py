import numpy as np
import tkinter as tk
from tkinter import messagebox


class Codificacion:
    def __init__(self):
        self.conteo = 0

    def nombre_a_matriz(self, nombre):
        matriz = []
        for letra in nombre:
            if letra == ' ':
                matriz.append(27)  # Espacio en blanco corresponde a 27
            else:
                numero_letra = ord(letra.lower()) - 96
                matriz.append(numero_letra)

        while len(matriz) % 3 != 0:
            matriz.append(27)

        matriz_3_filas = [matriz[i:i + 3] for i in range(0, len(matriz), 3)]
        matriz_transpuesta = np.transpose(matriz_3_filas).tolist()

        self.conteo = len(matriz_3_filas)
        return matriz_transpuesta, matriz

    def multiplicar_matrices(self, matriz1, matriz2):
        resultado = np.dot(matriz1, matriz2).tolist()
        return resultado


def cifrado_matrices(root):
    ventana_cifrado = tk.Toplevel(root)
    ventana_cifrado.title("Cifrado por Matrices")
    ventana_cifrado.geometry("700x600")

    codificador = Codificacion()

    tk.Label(ventana_cifrado, text="Ingrese un nombre:", font=("Arial", 14)).pack(pady=10)
    entrada_nombre = tk.Entry(ventana_cifrado, width=30, font=("Arial", 14))
    entrada_nombre.pack(pady=10)

    tk.Label(ventana_cifrado, text="Ingrese una matriz de 3x3 (dejar vacíos para valores cero):",
             font=("Arial", 14)).pack(pady=10)
    entradas_matriz = []
    frame_entradas = tk.Frame(ventana_cifrado)
    frame_entradas.pack(pady=10)

    for i in range(3):
        fila = []
        for j in range(3):
            entrada = tk.Entry(frame_entradas, width=5, font=("Arial", 14))
            entrada.grid(row=i, column=j, padx=5, pady=5)
            fila.append(entrada)
        entradas_matriz.append(fila)

    def obtener_valores_y_calcular():
        nombre_usuario = entrada_nombre.get()
        if not nombre_usuario:
            messagebox.showerror("Error", "Debe ingresar un nombre.")
            return

        matriz_nombre, nombre_numeros = codificador.nombre_a_matriz(nombre_usuario)

        matriz_usuario = []
        for fila in entradas_matriz:
            matriz_fila = []
            for entrada in fila:
                valor = entrada.get()
                if valor:
                    matriz_fila.append(float(valor))
                else:
                    matriz_fila.append(0.0)
            matriz_usuario.append(matriz_fila)

        matriz_usuario_np = np.array(matriz_usuario)
        resultado_multiplicacion = codificador.multiplicar_matrices(matriz_usuario_np, matriz_nombre)

        nombre_numeros_str = "Nombre convertido a números:\n" + str(nombre_numeros) + "\n"
        matriz_nombre_str = "Matriz del nombre (3 filas horizontales):\n" + "\n".join(
            ["\t".join(map(str, fila)) for fila in matriz_nombre]) + "\n"
        resultado_str = "Matriz codificada (3 filas horizontales):\n" + "\n".join(
            ["\t".join([f"{round(elemento, 4)}" for elemento in fila]) for fila in resultado_multiplicacion])

        messagebox.showinfo("Resultado", nombre_numeros_str + matriz_nombre_str + resultado_str)

    tk.Button(ventana_cifrado, text="Calcular", command=obtener_valores_y_calcular, font=("Arial", 14)).pack(pady=20)
    tk.Button(ventana_cifrado, text="Salir", command=ventana_cifrado.destroy, font=("Arial", 14)).pack(pady=10)
