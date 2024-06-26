import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

import numpy as np

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

        matriz_3_filas = [matriz[i::3] for i in range(3)]
        self.conteo = len(matriz_3_filas[0])
        return matriz_3_filas

    def multiplicar_matrices(self, matriz1, matriz2):
        resultado = np.dot(matriz1, matriz2).tolist()
        return resultado

    def inversa_matriz(self, matriz):
        try:
            matriz_np = np.array(matriz)
            inversa_np = np.linalg.inv(matriz_np)
            inversa = inversa_np.tolist()
            return inversa
        except np.linalg.LinAlgError:
            return "No se puede calcular la inversa de una matriz singular."

    def matriz_a_nombre(self, matriz):
        nombre = ""
        for j in range(len(matriz[0])):
            for i in range(3):
                num = round(matriz[i][j])
                if num == 27:
                    nombre += " "
                else:
                    nombre += chr(int(num) + 96)
        return nombre

def cifrado_matrices(root):
    codificador = Codificacion()

    nombre_usuario = simpledialog.askstring("Entrada", "Ingrese un nombre:")
    matriz_nombre = codificador.nombre_a_matriz(nombre_usuario)

    mensaje_matriz_nombre = "\n".join([" ".join(map(str, fila)) for fila in matriz_nombre])
    messagebox.showinfo("Matriz del nombre", f"Matriz del nombre:\n{mensaje_matriz_nombre}")

    matriz_usuario = []

    for i in range(3):
        fila = simpledialog.askstring("Entrada", f"Ingrese los 3 números de la fila {i + 1}:").split()
        fila = [int(num) for num in fila]
        matriz_usuario.append(fila)

    # Convertimos la matriz del usuario en numpy array para poder multiplicar
    matriz_usuario = np.array(matriz_usuario)
    matriz_nombre = np.array(matriz_nombre)

    resultado_multiplicacion = codificador.multiplicar_matrices(matriz_usuario, matriz_nombre)

    mensaje_resultado_multiplicacion = "\n".join([" ".join(map(str, fila)) for fila in resultado_multiplicacion])
    messagebox.showinfo("Matriz Codificada", f"Matriz Codificada:\n{mensaje_resultado_multiplicacion}")

    # Calculamos la inversa de la matriz proporcionada por el usuario
    inversa_usuario = codificador.inversa_matriz(matriz_usuario)
    if isinstance(inversa_usuario, str):
        messagebox.showerror("Error", inversa_usuario)
        return

    mensaje_inversa_usuario = "\n".join([" ".join(map(lambda x: f"{x:.4f}", fila)) for fila in inversa_usuario])
    messagebox.showinfo("Inversa de la Matriz del Usuario", f"Inversa de la Matriz del Usuario:\n{mensaje_inversa_usuario}")

    # Multiplicamos la inversa de la matriz del usuario con la matriz codificada para decodificar
    resultado_final = codificador.multiplicar_matrices(inversa_usuario, resultado_multiplicacion)

    mensaje_resultado_final = "\n".join([" ".join(map(lambda x: f"{x:.4f}", fila)) for fila in resultado_final])
    messagebox.showinfo("Matriz Decodificada", f"Matriz Decodificada:\n{mensaje_resultado_final}")

    # Convertimos la matriz decodificada de nuevo a nombre
    nombre_decodificado = codificador.matriz_a_nombre(resultado_final)
    messagebox.showinfo("Nombre Decodificado", f"Nombre Decodificado:\n{nombre_decodificado}")

    explicar_proceso(root)

def explicar_proceso(root):
    explicacion = """Explicación del proceso de codificación y decodificación:

1. Codificación del nombre:
   a. Convertimos el nombre en una matriz de 3 filas, donde cada letra se convierte en su valor numérico correspondiente en el alfabeto (a=1, b=2, ..., z=26).
   b. Los espacios en blanco se representan con el número 27.
   c. Si la longitud del nombre no es múltiplo de 3, se agregan espacios en blanco al final.

2. Multiplicación de matrices:
   a. El usuario proporciona una matriz de 3x3.
   b. Multiplicamos la matriz del usuario con la matriz del nombre para obtener la matriz codificada.

3. Decodificación:
   a. Calculamos la inversa de la matriz proporcionada por el usuario.
   b. Multiplicamos la inversa de la matriz del usuario con la matriz codificada para obtener la matriz decodificada.
   c. Convertimos la matriz decodificada de vuelta a texto, reemplazando los números por letras y los 27 por espacios en blanco.

Este proceso se basa en la propiedad de que si multiplicamos una matriz por su inversa, obtenemos la matriz identidad. Así, al multiplicar la matriz codificada por la inversa de la matriz del usuario, obtenemos la matriz original del nombre."""

    ventana_explicacion = tk.Toplevel(root)
    ventana_explicacion.title("Explicación del Proceso")

    area_texto = scrolledtext.ScrolledText(ventana_explicacion, width=70, height=20)
    area_texto.insert(tk.END, explicacion)
    area_texto.configure(state='disabled')
    area_texto.pack()

if __name__ == "__main__":
    root = tk.Tk()
    cifrado_matrices(root)
    root.mainloop()