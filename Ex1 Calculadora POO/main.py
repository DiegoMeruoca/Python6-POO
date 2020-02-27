# Arquivo principal do programa.
from calculadora import Calculadora
# Do arquivo calculadora importe a classe Calculadora.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
myCalc = Calculadora(numero1, numero2)  # Na variavel myClac
# cria um novo objeto do tipo Cauculadora, passando numero1
# e numero2 como parâmetros
op = input("Digite a operação matemática desejada( + - * / ): ")
if op == "+":
    myCalc.somar()  # Executa o método somar do obj myCalc
elif op == "-":
    myCalc.subtrair()  # Executa o método subtrair do obj myCalc
elif op == "*":
    myCalc.multiplicar()  # Executa o método multiplicar do obj myCalc
elif op == "/":
    myCalc.dividir()  # Executa o método dividir do obj myCalc
else:
    print("Opção inválida!!! ")
# Se foi utilizado um operador válido
if op == "+" or op == "-" or op == "*" or op == "/":
    print("O Resultado é ", myCalc.resultado)  # imprime a propriedade
    # resultado do objeto calc
