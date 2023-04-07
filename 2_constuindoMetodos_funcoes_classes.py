class Calculadora:
  
    def soma(self):
        return selfvalor_a + selfvalor_b

    def subtracao(self):
        return valor_a - valor_b

    def multiplicacao(self):
        return valor_a * valor_b

    def divisao(self):
        return valor_a / valor_b


calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.divisao(100, 2))
print(calculadora.multiplicacao(10, 5))