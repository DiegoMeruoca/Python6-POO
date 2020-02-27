class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0
        self.situacao = "Não avaliado"

    def calc_media(self):
        self.media = (self.nota1+self.nota2)/2
        return self.media

    def verifica_situacao(self):
        if self.media >= 7:
            self.situacao = "Aprovado"
        elif self.media < 5:
            self.situacao = "Reprovado"
        else:
            self.situacao = "de Recuperação"
        return self.situacao
