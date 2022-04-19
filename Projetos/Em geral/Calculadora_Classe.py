class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b
calculadora = Calculadora(10, 2)
print('O valor de b é:')
print(calculadora.valor_b)
print('O resultado da soma é:')
print(calculadora.soma())
print('O resultado da subtração é:')
print(calculadora.subtracao())
print('O resultado da multiplicação é:')
print(calculadora.multiplicacao())
print('O resultado da divisão é:')
print(calculadora.divisao())