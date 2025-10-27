# Ejercicio 3: Evaluador de expresiones RPN
def evaluar_rpn(expresion):
    pila = []  # Usamos una lista como pila

    # Separar la expresión en partes (tokens)
    tokens = expresion.split()

    for token in tokens:
        # Verificar si el token es un número
        if token.replace('.', '', 1).isdigit():
            # Convertir a float para aceptar decimales
            pila.append(float(token))
        else:
            # Si es operador, desapilar los dos últimos números
            if len(pila) < 2:
                print("Error: no hay suficientes operandos.")
                return None

            b = pila.pop()  # segundo operando
            a = pila.pop()  # primer operando

            # Aplicar la operación correspondiente
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                if b == 0:
                    print("Error: división por cero.")
                    return None
                resultado = a / b
            else:
                print("Operador desconocido:", token)
                return None

            # Apilar el resultado
            pila.append(resultado)

    # Al finalizar, la pila debería tener un único resultado
    if len(pila) == 1:
        return pila.pop()
    else:
        print("Error: la expresión no está bien formada.")
        return None



print(evaluar_rpn("3 4 + 2 *"))         # (3 + 4) * 2 = 14
print(evaluar_rpn("5 1 2 + 4 * + 3 -")) # (1 + 2) * 4 + 5 - 3 = 14
print(evaluar_rpn("10 2 / 3 +"))        # (10 / 2) + 3 = 8
print(evaluar_rpn("7 2 - 3 *"))         # (7 - 2) * 3 = 15