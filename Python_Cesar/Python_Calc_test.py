import unittest


class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b


class TesteCalculadora(unittest.TestCase):

    def test_soma(self):
        self.calc = Calculadora()
        resultado = self.calc.soma(4, 10)
        esperado = 14
        self.assertEqual(resultado, esperado)

    def test_sub(self):
        self.calc = Calculadora()
        resultado = self.calc.sub(15, 5)
        esperado = 5
        self.assertEqual(resultado, esperado)

    def test_mult(self):
        self.calc = Calculadora()
        resultado = self.calc.mult(4, 6)
        esperado = 24
        self.assertEqual(resultado, esperado)

    def test_div(self):
        self.calc = Calculadora()
        resultado = self.calc.div(12, 2)
        esperado = 4
        self.assertEqual(resultado, esperado)

