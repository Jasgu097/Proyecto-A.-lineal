import numpy as np
matriz_original=[[],[],[]]
print('Llene la matriz de transiciòn')
for i in range(3):
    for j in range(3):
        num=float(input(f'Ingresa los datos de la {i+1} fila: '))
        matriz_original[i].append(num)
print('La matriz trancisiòn es:',matriz_original)
def transpuesta_matriz(matriz_original):
    transpuesta = [[fila[i] for fila in matriz_original] for i in range(len(matriz_original[0]))]
    return transpuesta
trans=transpuesta_matriz(matriz_original)
print('La matriz trans es:',trans)

x=[]
print('Ingrese la matriz probabilidad del periodo 0 ')
for k in range(3):
    num_x=float(input(f'Ingrese la fila {k+1}: '))
    x.append(num_x)
print('La matriz probabilidad 0 es: ',x)
periodo=int(input('Ingrese la cantidad de periodos :'))
multiplicacion = np.matmul(trans, x)
print('Probabilidad periodo 1', multiplicacion)
for t in range(periodo-1):
    multiplicacion=np.matmul(trans,multiplicacion)
    print(f'La probabilidad el periodo {t+2} es: ',multiplicacion)
