import tkinter as tk
from Operacion_Matrices import operaciones_matrices
from Matriz_Inversa import matriz_inversa
from Cadena_Markov import transposicion_acumulada
from Codificacion import cifrado_matrices

# Funciones dummy para las otras operaciones
def dummy_function():
    tk.messagebox.showinfo("Info", "Esta función aún no está implementada.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Menú de Operaciones con Matrices y Vectores")
root.geometry("400x500")

# Título del menú
label_title = tk.Label(root, text="Menú de Operaciones", font=("Arial", 20))
label_title.pack(pady=20)

# Botones para cada opción del menú
buttons = [
    ("Operaciones entre matrices", lambda: operaciones_matrices(root)),
    ("Matriz inversa", lambda: matriz_inversa(root)),
    ("Determinante de una matriz", dummy_function),
    ("Rango de una matriz", dummy_function),
    ("Cifrado por matrices", lambda: cifrado_matrices(root)),
    ("Cadenas de Markov", lambda: transposicion_acumulada(root)),
    ("Operaciones con vectores", dummy_function),
    ("Salir", root.destroy)
]

for (text, command) in buttons:
    button = tk.Button(root, text=text, command=command, font=("Arial", 14))
    button.pack(fill=tk.X, pady=5, padx=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
