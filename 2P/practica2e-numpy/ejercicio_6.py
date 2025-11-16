#Parte A
import numpy as np

def estadisticas_vector(vector):
    # Convertir a ndarray por si viene como lista
    v = np.array(vector)

    media = np.mean(v)
    mediana = np.median(v)
    desviacion = np.std(v)

    print("Media:", media)
    print("Mediana:", mediana)
    print("Desviación estándar:", desviacion)
    return media, mediana, desviacion

vector = [1, 2, 2, 3, 4]
estadisticas_vector(vector)
print(f'------------------------------------------------------------------------')
#-------------------------------------------0000--------------------------------------------
#Parte B
def estadisticas_matriz(M):
    matriz = np.array(M)
    
    # Media, mediana y std por fila
    media_filas = np.mean(matriz, axis=1)
    mediana_filas = np.median(matriz, axis=1)
    std_filas = np.std(matriz, axis=1)
    
    # Media, mediana y std por columna
    media_columnas = np.mean(matriz, axis=0)
    mediana_columnas = np.median(matriz, axis=0)
    std_columnas = np.std(matriz, axis=0)
    
    # Mostrar resultados (despues de la variable, '3f' significa que muestre 3 decimales)
    for i in range(matriz.shape[0]):
        print(f"Fila {i+1} - media: {media_filas[i]:.3f}, mediana: {mediana_filas[i]:.3f}, std: {std_filas[i]:.3f}")
    
    print()
    
    for j in range(matriz.shape[1]):
        print(f"Columna {j+1} - media: {media_columnas[j]:.3f}, mediana: {mediana_columnas[j]:.3f}, std: {std_columnas[j]:.3f}")


M = [[1, 2, 3],
     [4, 5, 6]]
estadisticas_matriz(M)