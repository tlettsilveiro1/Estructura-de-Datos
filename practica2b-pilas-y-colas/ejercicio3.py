# Ejercicio 3: Evaluador de expresiones RPN (usando deque)
from collections import deque  # Importamos deque para usarlo como pila eficiente

def evaluar_rpn(expresion):
    pila = deque()  # Usamos deque en lugar de lista para mejorar el manejo de la pila

    # Separar la expresión en partes (tokens)
    tokens = expresion.split()

    for token in tokens:
        # Verificar si el token es un número
        if token.replace('.', '', 1).isdigit():
            # Convertir a float para aceptar decimales
            pila.append(float(token))  # append() apila el número en la cima
        else:
            # Si es operador, desapilar los dos últimos números
            if len(pila) < 2:
                print("Error: no hay suficientes operandos.")
                return None

            # pop() en deque elimina el elemento del final (igual que en la lista)
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


# Ejemplos de uso
print(evaluar_rpn("3 4 + 2 *"))         # (3 + 4) * 2 = 14
print(evaluar_rpn("5 1 2 + 4 * + 3 -")) # (1 + 2) * 4 + 5 - 3 = 14
print(evaluar_rpn("10 2 / 3 +"))        # (10 / 2) + 3 = 8
print(evaluar_rpn("7 2 - 3 *"))         # (7 - 2) * 3 = 15