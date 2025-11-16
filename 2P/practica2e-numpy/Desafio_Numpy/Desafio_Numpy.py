#Desafio1
import numpy as np
"""## Funcionalidades de los Arrays en NumPy
Los arrays de NumPy son estructuras de datos fundamentales para la computación numérica en Python. Ofrecen una serie de funcionalidades eficientes para trabajar con datos multidimensionales.
**Creación de Arrays:**
Puedes crear arrays de diversas formas:
"""

arr1 = np.array([10, 20, 30, 40, 50])
arr_zeros = np.zeros((2, 3))
arr_ones = np.ones((3, 2))

# Acceder a un elemento
print("Elemento en índice 2:", arr1[2])

# Acceder a una fila
print("Primera fila de arr_zeros:", arr_zeros[0])

# Acceder a una columna
print("Primera columna de arr_ones:", arr_ones[:, 0])

# Slicing
print("Slice de arr1:", arr1[1:4])

arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

# Suma
print("Suma:", arr_a + arr_b)

# Multiplicación
print("Multiplicación:", arr_a * arr_b)

# Raíz cuadrada
print("Raíz cuadrada de arr_b:", np.sqrt(arr_b))

# Seno
print("Seno de arr_a:", np.sin(arr_a))

# Reshape
arr_reshaped = arr1.reshape((5, 1))
print("Array redimensionado:\n", arr_reshaped)

# Concatenar
arr_concat = np.concatenate((arr_a, arr_b))
print("Arrays concatenados:", arr_concat)

# Media
print("Media de arr1:", np.mean(arr1))

# Desviación estándar
print("Desviación estándar de arr1:", np.std(arr1))

# Suma
print("Suma de arr1:", np.sum(arr1))

lineas=['Línea A', 'Línea B', 'Línea C', 'Línea D', 'Línea E']
turnos=['D1-Mañana', 'D1-Tarde', 'D2-Mañana', 'D2-Tarde', 'D3-Mañana', 'D3-Tarde']

produccion = np.array([
[145, 152, 138, 148, 155],
[148, 149, 142, 151, 153],
[142, 155, 135, 149, 158],
[151, 148, 140, 152, 156],
[147, 153, 137, 150, 157],
[149, 151, 139, 153, 154] ])

print(f'produccion promedio por linea: ', np.mean(produccion, axis=0))
# print(produccion[1])
# print(np.mean(produccion[:,2]))
print('Total produccion por turno: ',np.sum(produccion, axis = 1 ))
print(max(np.mean(produccion, axis = 0 )))
print(min(np.mean(produccion, axis = 0 )))
print('Desvio Estandard: ', np.std(produccion,axis= 1))
print('menor desvio: ',min(np.std(produccion,axis= 1)))
print('Lineas que cumplieron el objetivo: ',np.where(produccion >= 150))
print('Lineas que cumplieron el objetivo: ',produccion[np.where(produccion >= 150)]) #sirve para que te de los numeros (en un vector)

# 5. Calcular la desviación estándar de cada línea (indica consistencia)
desviacion_estandar_linea = np.std(produccion, axis=0)
print("Desviación estándar por línea:", desviacion_estandar_linea)

# 6. Identificar cuál línea es más consistente (menor desviación)
linea_mas_consistente_index = np.argmin(desviacion_estandar_linea) #Devuelve la posicion del argunmento minimo
linea_mas_consistente = lineas[linea_mas_consistente_index]
print("La línea más consistente es:", linea_mas_consistente)

# 7. Calcular cuántos turnos cada línea cumplió la meta de 150 unidades
turnos_cumplidos = np.sum(produccion >= 150, axis=0)
print("Número de turnos que cada línea cumplió la meta (150 unidades):", turnos_cumplidos)

# 8. Calcular el porcentaje de cumplimiento de meta por línea
porcentaje_cumplimiento = (turnos_cumplidos / len(turnos)) * 100
print("Porcentaje de cumplimiento de meta por línea:", porcentaje_cumplimiento)

# 9. Crear un ranking de líneas ordenadas por producción promedio (de mayor a menor)
produccion_promedio_linea = np.mean(produccion, axis=0)
ranking_indices = np.argsort(produccion_promedio_linea)[::-1] # Sort in descending order
ranking_lineas = [lineas[i] for i in ranking_indices]
print("Ranking de líneas por producción promedio (de mayor a menor):", ranking_lineas)

# 10. Identificar en qué turno se alcanzó la producción máxima total
produccion_total_turno = np.sum(produccion, axis=1)
turno_max_produccion_index = np.argmax(produccion_total_turno)
turno_max_produccion = turnos[turno_max_produccion_index]
print("La producción máxima total se alcanzó en el turno:", turno_max_produccion)

# 11. Calcular la brecha entre la línea más productiva y la menos productiva
produccion_promedio_linea = np.mean(produccion, axis=0)
brecha = np.max(produccion_promedio_linea) - np.min(produccion_promedio_linea)
print("La brecha entre la línea más productiva y la menos productiva es:", brecha)

import matplotlib.pyplot as plt

# 12. Crear DOS gráficos: - Gráfico 1: Gráfico de barras comparando la producción promedio de cada línea (incluir línea horizontal de la meta)
produccion_promedio_linea = np.mean(produccion, axis=0)
meta = 150

plt.figure(figsize=(10, 6))
plt.bar(lineas, produccion_promedio_linea, color='skyblue')
plt.axhline(meta, color='red', linestyle='--', label='Meta (150)')
plt.xlabel("Línea de Producción")
plt.ylabel("Producción Promedio")
plt.title("Producción Promedio por Línea vs. Meta")
plt.legend()
plt.ylim(0, max(produccion_promedio_linea) + 10) # Adjust y-axis limit for better visualization
plt.show()

# Gráfico 2: Gráfico de líneas mostrando la evolución de producción de cada línea a lo largo de los 6 turnos
plt.figure(figsize=(12, 6))
for i in range(len(lineas)):
    plt.plot(turnos, produccion[:, i], marker='o', label=lineas[i])

plt.xlabel("Turno")
plt.ylabel("Producción")
plt.title("Evolución de la Producción por Línea a lo largo de los Turnos")
plt.legend()
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout() # Adjust layout to prevent labels overlapping
plt.show()

"""¿Qué línea recomendarían auditar primero y por qué?
Se recomendaría auditar primero la Línea C. Según nuestro análisis, es la línea con la producción promedio más baja y un 0% de cumplimiento de la meta de 150 unidades. Esto indica que podría tener los problemas más significativos en el proceso.
¿La variabilidad alta es siempre mala? ¿En qué casos podría ser aceptable? No, la variabilidad alta no siempre es mala. En producción, generalmente buscamos baja variabilidad para asegurar consistencia. Sin embargo, podría ser aceptable, por ejemplo, en fases de experimentación o desarrollo de nuevos productos donde se están probando diferentes enfoques, o en situaciones donde la demanda del producto es muy variable y la flexibilidad en la producción es más importante que la consistencia.
¿Qué métodos de NumPy fueron más útiles para este análisis? Para este análisis, los métodos de NumPy más útiles fueron:
np.array() para crear los arrays de datos.
np.mean() para calcular promedios.
np.sum() para sumar producciones (totales por turno y cumplimiento de meta).
np.std() para calcular la desviación estándar (variabilidad).
np.argmin() y np.argmax() para encontrar los índices de valores mínimos y máximos.
np.where() o comparaciones directas (>=) con boolean indexing para identificar cumplimientos de meta.
np.argsort() para obtener los índices que permiten ordenar el ranking.
"""


#Desafio2
rangos_optimos = {
'Reactor 1': (218, 225),
'Reactor 2': (315, 320),
'Reactor 3': (185, 190),
'Reactor 4': (243, 250)
}

reactores = ['Reactor 1', 'Reactor 2', 'Reactor 3', 'Reactor 4']
horas = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00']

temperaturas = np.array([
[220, 315, 185, 245],
[222, 318, 188, 243],
[225, 320, 186, 248],
[219, 322, 190, 246],
[223, 317, 187, 250],
[221, 325, 189, 244],
[224, 319, 191, 247],
[218, 316, 184, 249]
])

rangos_optimos = {
'Reactor 1': (218, 225),
'Reactor 2': (315, 320),
'Reactor 3': (185, 190),
'Reactor 4': (243, 250)
}

reactores = ['Reactor 1', 'Reactor 2', 'Reactor 3', 'Reactor 4']
horas = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00']

temperaturas = np.array([
[220, 315, 185, 245],
[222, 318, 188, 243],
[225, 320, 186, 248],
[219, 322, 190, 246],
[223, 317, 187, 250],
[221, 325, 189, 244],
[224, 319, 191, 247],
[218, 316, 184, 249]
])

# NIVEL 1: Estadísticas Básicas

# 1. Calcular temperatura promedio, máxima y mínima de cada reactor
temp_promedio_reactor = np.mean(temperaturas, axis=0)
temp_max_reactor = np.max(temperaturas, axis=0)
temp_min_reactor = np.min(temperaturas, axis=0)

print("Temperatura promedio por reactor:", temp_promedio_reactor)
print("Temperatura máxima por reactor:", temp_max_reactor)
print("Temperatura mínima por reactor:", temp_min_reactor)

# 2. Calcular la desviación estándar de cada reactor
desviacion_estandar_reactor = np.std(temperaturas, axis=0)
print("Desviación estándar por reactor:", desviacion_estandar_reactor)

# 3. Identificar qué reactor tiene la mayor variabilidad térmica
reactor_mayor_variabilidad_index = np.argmax(desviacion_estandar_reactor)
reactor_mayor_variabilidad = reactores[reactor_mayor_variabilidad_index]
print("Reactor con mayor variabilidad térmica:", reactor_mayor_variabilidad)

# 4. Calcular el rango térmico (max - min) de cada reactor
rango_termico_reactor = temp_max_reactor - temp_min_reactor
print("Rango térmico por reactor:", rango_termico_reactor)

# 5. Para cada reactor, determinar cuántas horas estuvo dentro del rango óptimo
horas_conformidad = np.zeros(len(reactores), dtype=int)

for i, reactor in enumerate(reactores):
    rango_bajo, rango_alto = rangos_optimos[reactor]
    dentro_rango = (temperaturas[:, i] >= rango_bajo) & (temperaturas[:, i] <= rango_alto)
    horas_conformidad[i] = np.sum(dentro_rango)

print("Horas dentro del rango óptimo por reactor:", horas_conformidad)

# 6. Calcular el porcentaje de conformidad de cada reactor
porcentaje_conformidad = (horas_conformidad / len(horas)) * 100
print("Porcentaje de conformidad por reactor:", porcentaje_conformidad)

# 7. Identificar en qué hora específica cada reactor alcanzó su temperatura máxima
hora_max_temp_indices = np.argmax(temperaturas, axis=0)
hora_max_temp_reactor = [horas[i] for i in hora_max_temp_indices]
print("Hora en que cada reactor alcanzó su temperatura máxima:", hora_max_temp_reactor)

# 8. Crear una matriz booleana indicando si cada medición está dentro del rango óptimo
dentro_rango_optimo = np.zeros_like(temperaturas, dtype=bool)

for i, reactor in enumerate(reactores):
    rango_bajo, rango_alto = rangos_optimos[reactor]
    dentro_rango_optimo[:, i] = (temperaturas[:, i] >= rango_bajo) & (temperaturas[:, i] <= rango_alto)

print("Matriz booleana de mediciones dentro del rango óptimo:\n", dentro_rango_optimo)

# 9. Identificar todas las mediciones fuera de especificación (reactor, hora, temperatura)
fuera_rango_optimo = ~dentro_rango_optimo # Negate the boolean matrix to find values outside the range

# Get the indices of the values outside the range
horas_fuera, reactores_fuera = np.where(fuera_rango_optimo)

print("Mediciones fuera de especificación:")
for i in range(len(horas_fuera)):
    hora = horas[horas_fuera[i]]
    reactor = reactores[reactores_fuera[i]]
    temperatura = temperaturas[horas_fuera[i], reactores_fuera[i]]
    print(f"- Reactor: {reactor}, Hora: {hora}, Temperatura: {temperatura}")

# 10. Calcular cuántos grados se desvió cada medición problemática del límite más cercano
print("\nDesviación de las mediciones fuera de especificación:")
for i in range(len(horas_fuera)):
    hora_index = horas_fuera[i]
    reactor_index = reactores_fuera[i]
    reactor = reactores[reactor_index]
    temperatura = temperaturas[hora_index, reactor_index]
    rango_bajo, rango_alto = rangos_optimos[reactor]

    if temperatura < rango_bajo:
        desviacion = rango_bajo - temperatura
        print(f"- Reactor: {reactor}, Hora: {horas[hora_index]}, Temperatura: {temperatura}, Desviación: {desviacion:.2f} grados por debajo del límite inferior ({rango_bajo})")
    elif temperatura > rango_alto:
        desviacion = temperatura - rango_alto
        print(f"- Reactor: {reactor}, Hora: {horas[hora_index]}, Temperatura: {temperatura}, Desviación: {desviacion:.2f} grados por encima del límite superior ({rango_alto})")

# 11. Ordenar los reactores por nivel de criticidad (mayor tiempo fuera de especificación)
tiempo_fuera_especificacion = np.sum(fuera_rango_optimo, axis=0)
ranking_criticidad_indices = np.argsort(tiempo_fuera_especificacion)[::-1] # Sort in descending order
ranking_criticidad_reactores = [reactores[i] for i in ranking_criticidad_indices]

print("\nRanking de reactores por criticidad (mayor tiempo fuera de especificación):", ranking_criticidad_reactores)

# 12. Calcular la temperatura promedio por hora (todas los reactores) para detectar patrones temporales
temperatura_promedio_hora = np.mean(temperaturas, axis=1)
print("Temperatura promedio por hora (en todos los reactores):", temperatura_promedio_hora)

# 13. Crear DOS gráficos:
# - Gráfico 1: Gráfico de líneas mostrando la evolución de temperatura de los 4 reactores + bandas de rangos óptimos
plt.figure(figsize=(12, 6))

for i in range(len(reactores)):
    plt.plot(horas, temperaturas[:, i], marker='o', label=reactores[i])
    rango_bajo, rango_alto = rangos_optimos[reactores[i]]
    plt.fill_between(horas, rango_bajo, rango_alto, color=plt.gca().lines[-1].get_color(), alpha=0.1, label=f'{reactores[i]} Rango Óptimo')


plt.xlabel("Hora")
plt.ylabel("Temperatura (°C)")
plt.title("Evolución de la Temperatura por Reactor y Rangos Óptimos")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2: Gráfico de barras mostrando el porcentaje de conformidad de cada reactor
plt.figure(figsize=(10, 6))
plt.bar(reactores, porcentaje_conformidad, color='lightgreen')
plt.xlabel("Reactor")
plt.ylabel("Porcentaje de Conformidad (%)")
plt.title("Porcentaje de Conformidad por Reactor")
plt.ylim(0, 100) # Ensure y-axis goes up to 100%
plt.grid(axis='y', linestyle='--')
plt.show()

"""¿Qué reactor necesita intervención inmediata y por qué? Según el ranking de criticidad, el Reactor 3 y el Reactor 2 son los que estuvieron más tiempo fuera de especificación. El Reactor 3 tuvo 2 mediciones fuera de rango (una por encima y una por debajo), mientras que el Reactor 2 tuvo 2 mediciones por encima del límite superior. Ambos necesitarían revisión, pero el Reactor 3 podría requerir una intervención más inmediata al salirse por ambos límites.
¿La desviación estándar baja siempre indica un buen proceso? Expliquen. No, una desviación estándar baja no siempre indica un buen proceso por sí sola. Indica que las mediciones son consistentes y están cerca del promedio. Sin embargo, si el promedio está fuera del rango objetivo, una desviación estándar baja solo significa que consistentemente se está fuera de especificación. Un buen proceso requiere tanto una desviación estándar baja como un promedio dentro del rango deseado.
¿Observaron algún patrón temporal en las temperaturas? Al observar la temperatura promedio por hora (calculada en el punto 12), se puede ver una ligera tendencia al aumento desde las 08:00 hasta las 14:00, para luego disminuir a las 15:00. Esto podría sugerir un patrón temporal relacionado con la operación diaria o factores ambientales.
¿Qué métodos de indexing/masking de NumPy utilizaron? Utilizamos principalmente:
Indexing con enteros: Para acceder a elementos o filas/columnas específicas (ej. temperaturas[:, i]).
Slicing: Para seleccionar rangos de elementos (aunque no se usó explícitamente en este último análisis, sí en ejercicios anteriores).
Boolean Indexing (Masking): Para seleccionar elementos basándose en condiciones booleanas (ej. (temperaturas[:, i] >= rango_bajo) & (temperaturas[:, i] <= rango_alto) y el uso de fuera_rango_optimo).
np.where(): Para obtener los índices donde una condición booleana es True, lo que nos permitió identificar las mediciones fuera de rango.
"""


#Desafio 3
# Datos base
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
almacenes = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro', 'Costero']

inventario = np.array([
    [450, 320, 580, 290, 410],
    [380, 350, 520, 310, 390],
    [420, 310, 550, 280, 420],
    [390, 340, 510, 320, 380],
    [460, 330, 590, 300, 430],
    [410, 360, 540, 290, 400]
])

precios = np.array([45, 65, 38, 72, 55])
costos_almacenamiento = np.array([2.5, 3.8, 2.0, 4.2, 3.0])
demanda_mensual = np.array([2200, 1800, 3000, 1600, 2300])

# --- Nivel 1 ---
stock_total_producto = inventario.sum(axis=0)
stock_total_almacen = inventario.sum(axis=1)

almacen_mayor_volumen = almacenes[np.argmax(stock_total_almacen)]
producto_menor_stock = productos[np.argmin(stock_total_producto)]

# --- Nivel 2 ---
valor_inventario_almacen = inventario @ precios #producto matricial
valor_inventario_producto = stock_total_producto * precios
almacen_mayor_valor = almacenes[np.argmax(valor_inventario_almacen)]

valor_total = valor_inventario_producto.sum()
porcentaje_valor_producto = (valor_inventario_producto / valor_total) * 100

# --- Nivel 3 ---
meses_cobertura = stock_total_producto / demanda_mensual
riesgo_desabastecimiento = [productos[i] for i in range(len(productos)) if meses_cobertura[i] < 1]
exceso_inventario = [productos[i] for i in range(len(productos)) if meses_cobertura[i] > 1.5]


costo_mensual_producto = stock_total_producto * costos_almacenamiento
costo_mensual_almacen = inventario @ costos_almacenamiento

# --- Nivel 4 ---
ranking_almacenes = [almacenes[i] for i in np.argsort(-valor_inventario_almacen)]
distribucion_optima = (inventario / stock_total_producto) * 100  # % del stock de cada producto por almacén

# Resultados
print("Stock total por producto:", stock_total_producto)
print("Inventario total por almacén:", stock_total_almacen)
print("Almacén con mayor volumen:", almacen_mayor_volumen)
print("Producto con menor stock:", producto_menor_stock)
print("Valor inventario por almacén:", valor_inventario_almacen)
print("Valor inventario por producto:", valor_inventario_producto)
print("Almacén con mayor valor:", almacen_mayor_valor)
print("Porcentaje de valor por producto:", porcentaje_valor_producto)
print("Meses de cobertura:", meses_cobertura)
print("Productos con riesgo:", riesgo_desabastecimiento)
print("Productos con exceso:", exceso_inventario)
print("Costo mensual por producto:", costo_mensual_producto)
print("Ranking de almacenes:", ranking_almacenes)

"""El producto que requiere reabastecimiento más pronto es Producto E, y el que podría reducirse ligeramente es Producto A.
El almacén Centro tiene el inventario más eficiente porque combina el mayor valor total con un volumen medio, optimizando espacio y rentabilidad.
El broadcasting de NumPy se usa en los cálculos de valor total, multiplicando directamente matrices de inventario por vectores de precios o costos sin necesidad de bucles.
"""


#Desafio 4
# Datos base
productos = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta']
trimestres = ['Q1', 'Q2', 'Q3', 'Q4']

unidades = np.array([
    [1250, 1380, 1420, 1650],
    [980, 1050, 1020, 1150],
    [1560, 1680, 1590, 1820],
    [870, 920, 890, 1010],
    [1340, 1450, 1480, 1620],
    [760, 810, 780, 890]
])

ingresos = np.array([
    [56250, 62100, 63900, 74250],
    [58800, 63000, 61200, 69000],
    [54600, 58800, 55650, 63700],
    [60900, 64400, 62300, 70700],
    [60300, 65250, 66600, 72900],
    [49400, 52650, 50700, 57850]
])

# --- Nivel 1 ---
ventas_totales = unidades.sum(axis=1)
ingresos_totales = ingresos.sum(axis=1)

precio_promedio = ingresos / unidades
producto_mayor_ingreso = productos[np.argmax(ingresos_totales)]
ingresos_trimestre = ingresos.sum(axis=0)

# --- Nivel 2 ---
crecimiento_unidades = (unidades[:, 3] - unidades[:, 0]) / unidades[:, 0] * 100
crecimiento_ingresos = (ingresos[:, 3] - ingresos[:, 0]) / ingresos[:, 0] * 100

producto_mayor_crecimiento = productos[np.argmax(crecimiento_unidades)]
producto_crecimiento_negativo = [productos[i] for i in range(len(productos)) if crecimiento_unidades[i] < 0]

tasa_crecimiento_promedio = (crecimiento_unidades / 3)

# --- Nivel 3 ---
ingreso_promedio_unidad = ingresos_totales / ventas_totales
producto_premium = productos[np.argmax(ingreso_promedio_unidad)]

porcentaje_ingresos_totales = (ingresos_totales / ingresos_totales.sum()) * 100
mejor_trimestre = [trimestres[i] for i in np.argmax(ingresos, axis=1)]

# --- Nivel 4 ---
tendencia = np.polyfit([1, 2, 3, 4], ingresos.mean(axis=0), 1)
q1_2024 = np.polyval(tendencia, 5)

# Resultados
print("Ventas anuales por producto:", ventas_totales)
print("Ingresos anuales por producto:", ingresos_totales)
print("Producto con mayor ingreso:", producto_mayor_ingreso)
print("Ingresos por trimestre:", ingresos_trimestre)
print("Crecimiento unidades (%):", crecimiento_unidades)
print("Crecimiento ingresos (%):", crecimiento_ingresos)
print("Producto mayor crecimiento:", producto_mayor_crecimiento)
print("Productos con crecimiento negativo:", producto_crecimiento_negativo)
print("Tasa crecimiento promedio trimestral:", tasa_crecimiento_promedio)
print("Ingreso promedio por unidad:", ingreso_promedio_unidad)
print("Producto más premium:", producto_premium)
print("Porcentaje ingresos totales:", porcentaje_ingresos_totales)
print("Mejor trimestre por producto:", mejor_trimestre)
print("Proyección Q1 2024:", q1_2024)

"""Para 2024 conviene invertir en Alpha y Epsilon, ya que muestran crecimiento sostenido y gran aporte a los ingresos.
Gamma podría replantearse o rediseñarse por su bajo rendimiento relativo.
Las operaciones vectorizadas de NumPy, como sum(axis=1), mean(axis=1) y divisiones entre matrices, permiten obtener rápidamente métricas sin bucles.
La diferencia entre crecimiento en unidades e ingresos refleja cambios en precios o en mezcla de ventas: si los ingresos crecen más rápido que las unidades, el producto está ganando valor o posicionamiento en el mercado.
"""