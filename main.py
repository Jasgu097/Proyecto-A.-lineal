Salir=False
while not Salir:
    print("__________Menu__________")
    eleccion=input("1. Operaciones entre matricez\n2. Matriz iversa\n3. Determiante de una matriz\n4. Rango de una matriz\n5. Cifrado por matricez\n6. Cadenas de markov\n7. Operaciones con vectores\n8. Salir\nPorfavor ingrese una opcion: ")
    if eleccion=="1":
        import Operacion_Matrices
    elif eleccion=="2":
        import Matriz_Inversa
    elif eleccion=="3":
        import Determinante_matriz
    elif eleccion=="4":
        import Rango_Matriz
    elif eleccion=="5":
        import Codificacion
    elif eleccion=="6":
        import Cadena_Markov
    elif eleccion=="7":
        import Operacion_Vectores
    elif eleccion=="8":
        Salir=True
    else:
        print("Operacion no valida porfavor ingrese una valor valido")


