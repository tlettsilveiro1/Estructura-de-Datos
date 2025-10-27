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

#--------------------------------0000-----------------------------
#Parte B
import numpy as np

def estadisticas_matriz(M):
    matriz = np.array(M)
    filas, columnas = matriz.shape

    # 📏 Estadísticas por fila
    for i in range(filas):
        fila = matriz[i, :]
        media = np.mean(fila)
        mediana = np.median(fila)
        desviacion = np.std(fila)
        print(f"Fila {i+1} - media: {media:.3f}, mediana: {mediana:.3f}, std: {desviacion:.3f}")

    print()  # línea en blanco

    # 📏 Estadísticas por columna
    for j in range(columnas):
        columna = matriz[:, j]
        media = np.mean(columna)
        mediana = np.median(columna)
        desviacion = np.std(columna)
        print(f"Columna {j+1} - media: {media:.3f}, mediana: {mediana:.3f}, std: {desviacion:.3f}")


M = [[1, 2, 3],
     [4, 5, 6]]

estadisticas_matriz(M)