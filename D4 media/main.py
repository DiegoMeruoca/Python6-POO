# Arquivo principal do programa.
from aluno import Aluno
print("Bem vindo ao programa de calculo da média!")
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
meualuno = Aluno(nome, nota1, nota2)
media = meualuno.calc_media()
situacao = meualuno.verifica_situacao()
print("A média do(a) {} foi {:.2f}!\nPortanto ele(a) está {}!!!" .format(nome, media, situacao))



