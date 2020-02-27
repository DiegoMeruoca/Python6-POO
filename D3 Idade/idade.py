from datetime import date


class Idade:  # Define o nome da classe
    # __init__() é o método inicializador da classe recebendo
    # um parâmetro: raio
    def __init__(self, ano, mes, dia):
        self.anoNasc = ano
        self.mesNasc = mes
        self.diaNasc = dia
        data = date.today()
        self.anoAtt = data.year
        self.mesAtt = data.month
        self.diaAtt = data.day
        self.totalAnos = 0

    def calcularAnos(self):
        if self.mesNasc < self.mesAtt:  # Se o mes de aniversario já passou
            self.totalAnos = self.anoAtt - self.anoNasc
        elif self.mesNasc == self.mesAtt:  # Se estamos no mes de aniversario
            if self.diaNasc <= self.diaAtt:  # Se o dia do aniversario ja passou
                self.totalAnos = self.anoAtt - self.anoNasc
            else:  # Se o dia do aniversario não passou
                self.totalAnos = self.anoAtt - self.anoNasc -1
        else:  # Se o mes de aniversario não passou
            self.totalAnos = self.anoAtt - self.anoNasc - 1
