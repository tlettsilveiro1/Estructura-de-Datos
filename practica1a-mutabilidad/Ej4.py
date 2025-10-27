def reemplazar(cadena, i, caracter):
    # Validamos que i esté dentro del rango
    if i < 0 or i >= len(cadena):
        raise ValueError("La posición i está fuera del rango de la cadena.")
    
    # Construimos la nueva cadena
    nueva_cadena = cadena[:i] + caracter + cadena[i+1:]
    return nueva_cadena


original = "casado"
print(original)
modificado = reemplazar(original, 2, "z")
print(modificado) # cazado
