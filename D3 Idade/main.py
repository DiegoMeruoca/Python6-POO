# Arquivo principal do programa.
from idade import Idade
print("Bem vindo aoprograma de calculo da idade!!!")
dia = int(input("Digite o dia do seu nascimento:"))
mes = int(input("Digite o mes do seu nascimento:"))
ano = int(input("Digite o ano do seu nascimento:"))
minhaIdade = Idade(ano, mes, dia)
minhaIdade.calcularAnos()
print("Você tem {} anos!" .format(minhaIdade.totalAnos))
