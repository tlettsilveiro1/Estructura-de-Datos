def probar():
    a = (1, 2, [1, 2, 3])
    a[2].append(4)
    print(a)
probar()

#La línea a[2].append(4) modifica la lista dentro de la tupla, no la tupla en sí.