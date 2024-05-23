import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox


def imprimir_matriz(matriz, nombre):
    print(f"{nombre}:")
    for fila in matriz:
        print("\t".join(f"{elemento:.4f}" for elemento in fila))
    print()


def transposicion_acumulada(root):
    ventana_transposicion = tk.Toplevel(root)
    ventana_transposicion.title("Transposición y Multiplicación Acumulada")
    ventana_transposicion.geometry("500x500")

    tk.Label(ventana_transposicion, text="Ingrese los elementos de la matriz 3x3:").pack(pady=10)

    entradas_matriz1 = []
    frame_entradas1 = tk.Frame(ventana_transposicion)
    frame_entradas1.pack(pady=10)

    for i in range(3):
        fila = []
        for j in range(3):
            entrada = tk.Entry(frame_entradas1, width=5)
            entrada.grid(row=i, column=j, padx=5, pady=5)
            fila.append(entrada)
        entradas_matriz1.append(fila)

    tk.Label(ventana_transposicion, text="Ingrese los elementos de la matriz 3x1:").pack(pady=10)

    entradas_matriz2 = []
    frame_entradas2 = tk.Frame(ventana_transposicion)
    frame_entradas2.pack(pady=10)

    for i in range(3):
        entrada = tk.Entry(frame_entradas2, width=5)
        entrada.grid(row=i, column=0, padx=5, pady=5)
        entradas_matriz2.append(entrada)

    def obtener_valores_y_calcular():
        matriz1 = []
        for fila in entradas_matriz1:
            matriz_fila = []
            for entrada in fila:
                valor = entrada.get()
                if valor:
                    matriz_fila.append(float(valor))
                else:
                    matriz_fila.append(0.0)
            matriz1.append(matriz_fila)

        matriz2 = []
        for entrada in entradas_matriz2:
            valor = entrada.get()
            if valor:
                matriz2.append([float(valor)])
            else:
                matriz2.append([0.0])

        veces = simpledialog.askinteger("Entrada",
                                        "Ingrese la cantidad de veces que desea multiplicar la matriz transpuesta por la matriz 3x1:",
                                        parent=ventana_transposicion)

        transpuesta = np.transpose(matriz1)
        resultado = matriz2

        print("Proceso:")
        imprimir_matriz(matriz1, "Matriz 1")
        imprimir_matriz(matriz2, "Matriz 2")
        print("Matriz Transpuesta:")
        imprimir_matriz(transpuesta, "Transpuesta")

        for i in range(veces):
            print(f"Iteración {i + 1}:")
            resultado = np.dot(transpuesta, resultado)
            imprimir_matriz(resultado, "Resultado")

        resultado_str = "\n".join([f"{round(fila[0], 4)}" for fila in resultado])
        messagebox.showinfo("Resultado", f"Resultado de la multiplicación acumulada:\n{resultado_str}")

    tk.Button(ventana_transposicion, text="Calcular", command=obtener_valores_y_calcular).pack(pady=20)
    tk.Button(ventana_transposicion, text="Salir", command=ventana_transposicion.destroy).pack(pady=10)
