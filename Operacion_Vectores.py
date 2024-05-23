import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_vector_input(dim):
    vector = []
    for i in range(dim):
        value = simpledialog.askfloat("Entrada", f"Ingrese el valor para la dimensión {i + 1}:")
        vector.append(value)
    return vector

def plot_vectors(vectors, operation):
    fig = plt.figure()
    if len(vectors[0]) == 2:
        ax = fig.add_subplot(111)
        origin = np.array([[0, 0], [0, 0]])
    else:
        ax = fig.add_subplot(111, projection='3d')
        origin = np.array([[0, 0, 0], [0, 0, 0]])

    colors = ['r', 'g', 'b', 'y']
    for i, vector in enumerate(vectors):
        if len(vector) == 2:
            ax.quiver(*origin[0], *vector, angles='xy', scale_units='xy', scale=1, color=colors[i])
        else:
            ax.quiver(*origin[0], *vector, color=colors[i])

    if len(vectors[0]) == 2:
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal')
    else:
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_zlim(-10, 10)
        ax.set_box_aspect([1, 1, 1])

    ax.set_title(f"Vectores y sus {operation}")
    ax.grid(True)

    return fig

def vector_operations(root):
    dimension = simpledialog.askinteger("Dimensión", "Ingrese la dimensión (2 o 3):")
    if dimension not in [2, 3]:
        messagebox.showerror("Error", "¡Dimensión no válida! Por favor ingrese 2 o 3.")
        return

    vector1 = get_vector_input(dimension)
    vector2 = get_vector_input(dimension)

    sum_result = np.add(vector1, vector2)
    diff_result = np.subtract(vector1, vector2)
    dot_result = np.dot(vector1, vector2)

    vectors_to_plot = [vector1, vector2, sum_result, diff_result]
    fig = plot_vectors(vectors_to_plot, "operaciones")

    # Crear una nueva ventana para mostrar la gráfica y los resultados
    plot_window = tk.Toplevel(root)
    plot_window.title("Gráfica de Vectores")

    # Crear un frame para la gráfica
    frame_plot = tk.Frame(plot_window)
    frame_plot.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Crear un frame para los resultados
    frame_results = tk.Frame(plot_window)
    frame_results.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    result_text = f"Vector 1: {vector1}\nVector 2: {vector2}\n\n" \
                  f"Suma: {sum_result}\nDiferencia: {diff_result}\nProducto Punto: {dot_result}"

    label_results = tk.Label(frame_results, text=result_text, justify=tk.LEFT, font=("Arial", 12))
    label_results.pack(pady=10, padx=10)
