# Diseñen una calculadora que tenga las funciones básicas (suma, resta,
# multiplicación y división) que operan siempre con dos operandos.
# El usuario introduce los dos operandos y el operador ('+', '-', '\*', '/').
# El programa termina cuando el usuario introduce una cadena vacía como operando.
# Maneja correctamente los posibles casos de error.

def calculadora():
    print("Calculadora básica. Ingresa números y un operador (+, -, *, /).")
    print("Deja el primer operando vacío para salir.")

    while True:
        # Pedimos el primer operando
        op1 = input("Ingresa el primer número: ")
        if op1 == "":
            print("Saliendo de la calculadora...")
            break

        try:
            op1 = float(op1)
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            continue   #salta a la siguiente iteración, pero el bucle sigue funcionando.

        # Pedimos el segundo operando
        op2 = input("Ingresa el segundo número: ")
        try:
            op2 = float(op2)
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            continue

        # Pedimos el operador
        operador = input("Ingresa el operador (+, -, *, /): ")
        
        try:
            if operador == "+":
                resultado = op1 + op2
            elif operador == "-":
                resultado = op1 - op2
            elif operador == "*":
                resultado = op1 * op2
            elif operador == "/":
                resultado = op1 / op2
            else:
                raise ValueError("Operador no válido")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
            continue
        except ValueError as e:
            print("Error:", e)
            continue

        print("Resultado:", resultado)
        print("-" * 30)

# Ejecutar la calculadora
calculadora()