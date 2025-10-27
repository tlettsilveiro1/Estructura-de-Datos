def son_vectores_iguales(vectora, vectorb):
    # 1 Verificar que tengan la misma longitud
    if len(vectora) != len(vectorb):
        print("Los dos vectores NO son iguales")
        return
    
    # 2 Crear una nueva lista con los cuadrados de los elementos de vectora
    cuadrados = []
    for elemento in vectora:
        cuadrados.append(elemento ** 2)
    
    # 3 Ordenar ambos vectores (para ignorar el orden)
    cuadrados.sort()
    vectorb.sort()
    
    # 4 Comparar elemento a elemento
    iguales = True
    for i in range(len(cuadrados)):
        if cuadrados[i] != vectorb[i]:
            iguales = False
            break
    
    # 5 Mostrar el resultado
    if iguales:
        print("Los dos vectores son iguales")
    else:
        print("Los dos vectores NO son iguales")


vectora = [121, 144, 19, 161, 19, 144, 19, 11] 
vectorb = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

son_vectores_iguales(vectora, vectorb)

vectora = [121, 144, 19, 161, 19, 144, 9, 11] 
vectorb = [121, 14641, 20736, 361, 25, 361, 20736, 361]

son_vectores_iguales(vectora, vectorb)