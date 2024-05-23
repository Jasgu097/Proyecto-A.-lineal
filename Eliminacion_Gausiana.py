import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import numpy as np

def imprimir_matriz(matriz, paso, text_box):
    filas, columnas = matriz.shape
    mensaje = f"Paso {paso}:\n"
    for i in range(filas):
        fila = ["{:6.2f}".format(elemento) for elemento in matriz[i]]
        mensaje += "  " + " ".join(fila) + "\n"
    print(mensaje)
    text_box.insert(tk.END, mensaje + "\n")
    text_box.see(tk.END)

def eliminacion_gaussiana(matriz, text_box):
    filas, columnas = matriz.shape
    rango = 0
    paso = 1

    imprimir_matriz(matriz, paso, text_box)  # Imprimir la matriz original

    for columna in range(columnas):
        # Encontrar el pivote
        pivot_fila = None
        for fila in range(rango, filas):
            if matriz[fila, columna] != 0:
                pivot_fila = fila
                break

        # Si no se encuentra pivote, continuar con la siguiente columna
        if pivot_fila is None:
            continue

        # Intercambiar filas para obtener el pivote en la posición correcta
        matriz[[rango, pivot_fila]] = matriz[[pivot_fila, rango]]
        paso += 1
        imprimir_matriz(matriz, paso, text_box)  # Imprimir la matriz después de intercambiar filas

        # Eliminar elementos debajo del pivote
        for fila in range(rango + 1, filas):
            factor = matriz[fila, columna] / matriz[rango, columna]
            matriz[fila] = matriz[fila] - factor * matriz[rango]
            paso += 1
            imprimir_matriz(matriz, paso, text_box)  # Imprimir la matriz después de eliminar elementos debajo del pivote

        rango += 1

    return rango

def calcular_rango(matriz, text_box):
    return eliminacion_gaussiana(matriz, text_box)

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

def mostrar_rango(root):
    ventana_rango = tk.Toplevel(root)
    ventana_rango.title("Rango de la Matriz")
    ventana_rango.geometry("500x450")

    text_box = scrolledtext.ScrolledText(ventana_rango, width=80, height=20)
    text_box.pack(pady=20)

    matriz = obtener_matriz()
    rango = calcular_rango(matriz, text_box)
    text_box.insert(tk.END, f"\nEl rango de la matriz es: {rango}")

def rango_matriz(root):
    root.withdraw()  # Oculta la ventana principal
    if messagebox.askyesno("Rango de una Matriz", "¿Desea calcular el rango de una matriz?"):
        mostrar_rango(root)
    root.deiconify()  # Muestra la ventana principal nuevamente

def main():
    root = tk.Tk()
    rango_matriz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
