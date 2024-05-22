import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np


class MatrixDeterminantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Determinante de una Matriz")

        self.prompt_matrix_size()

    def prompt_matrix_size(self):
        self.rows = simpledialog.askinteger("Filas", "¿Cuántas filas tendrá la matriz?")
        self.cols = simpledialog.askinteger("Columnas", "¿Cuántas columnas tendrá la matriz?")

        if self.rows and self.cols:
            self.create_matrix_input()
        else:
            messagebox.showerror("Error", "Debe ingresar un número válido de filas y columnas.")
            self.root.destroy()

    def create_matrix_input(self):
        self.entries = []

        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        for i in range(self.rows):
            row_entries = []
            for j in range(self.cols):
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        calc_button = tk.Button(self.root, text="Calcular Determinante", command=self.calculate_determinant)
        calc_button.pack(pady=10)

    def calculate_determinant(self):
        matrix = []

        try:
            for row_entries in self.entries:
                row = []
                for entry in row_entries:
                    row.append(float(entry.get()))
                matrix.append(row)

            matrix_np = np.array(matrix)
            if matrix_np.shape[0] != matrix_np.shape[1]:
                raise ValueError("La matriz debe ser cuadrada para calcular el determinante.")

            determinant = np.linalg.det(matrix_np)
            messagebox.showinfo("Determinante", f"El determinante de la matriz es: {determinant:.2f}")

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")


def main():
    root = tk.Tk()
    app = MatrixDeterminantApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
