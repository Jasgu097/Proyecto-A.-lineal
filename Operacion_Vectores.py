import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def get_vector_input(dim):
    vector = []
    for i in range(dim):
        value = simpledialog.askfloat("Input", f"Enter value for dimension {i + 1}:")
        vector.append(value)
    return vector


def plot_vectors(vectors, operation):
    fig, ax = plt.subplots()
    origin = np.array([0, 0, 0])
    colors = ['r', 'g', 'b', 'y']

    for i, vector in enumerate(vectors):
        if len(vector) == 2:
            ax.quiver(*origin[:2], *vector, angles='xy', scale_units='xy', scale=1, color=colors[i])
        elif len(vector) == 3:
            ax.quiver(*origin, *vector, color=colors[i])

    if len(vectors[0]) == 2:
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
    else:
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_zlim(-10, 10)

    ax.set_title(f"Vectors and their {operation}")
    ax.grid(True)

    if len(vectors[0]) == 2:
        ax.set_aspect('equal')
    else:
        plt.gca().set_box_aspect([1, 1, 1])

    return fig


def vector_operations():
    dimension = simpledialog.askinteger("Dimension", "Enter dimension (2 or 3):")
    if dimension not in [2, 3]:
        messagebox.showerror("Error", "Invalid dimension! Please enter 2 or 3.")
        return

    vector1 = get_vector_input(dimension)
    vector2 = get_vector_input(dimension)

    sum_result = np.add(vector1, vector2)
    diff_result = np.subtract(vector1, vector2)
    dot_result = np.dot(vector1, vector2)

    vectors_to_plot = [vector1, vector2, sum_result, diff_result]
    fig = plot_vectors(vectors_to_plot, "operations")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    result_text = f"Vector 1: {vector1}\nVector 2: {vector2}\n\n" \
                  f"Sum: {sum_result}\nDifference: {diff_result}\nDot Product: {dot_result}"

    messagebox.showinfo("Results", result_text)


root = tk.Tk()
root.title("Vector Operations")

operation_button = tk.Button(root, text="Perform Vector Operations", command=vector_operations)
operation_button.pack(pady=20)

root.mainloop()

