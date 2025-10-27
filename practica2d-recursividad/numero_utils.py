class NumeroUtils:
    def sumar_digitos(self, n):
        # Caso base: si el número tiene un solo dígito
        if n < 10:
            return n
        else:
            # Último dígito + suma de los demás dígitos
            return (n % 10) + self.sumar_digitos(n // 10)

    def invertir_numero(self, n):
        # Caso base: si es un solo dígito
        if n < 10:
            return n
        else:
            # Calcular el número de dígitos del resto
            resto = n // 10
            digitos_resto = self.contar_digitos(resto)
            # Último dígito multiplicado por 10^(número de dígitos del resto) + invertir el resto
            return (n % 10) * (10 ** digitos_resto) + self.invertir_numero(resto)

    # Método auxiliar para contar dígitos
    def contar_digitos(self, n):
        if n < 10:
            return 1
        else:
            return 1 + self.contar_digitos(n // 10)


num_utils = NumeroUtils()
print(num_utils.sumar_digitos(1234))  # 10
print(num_utils.sumar_digitos(505))   # 10

print(num_utils.invertir_numero(1234))  # 4321
print(num_utils.invertir_numero(100))   # 1