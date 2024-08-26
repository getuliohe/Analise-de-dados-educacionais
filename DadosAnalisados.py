class DadosAnalisados:
    def __init__(self, tamanhoDaLista, media, mediana,variancia,desvioPadrao,desvioMedioAbsoluto,amplitude,coeficienteDeVariacao, min, max, qd1, qd2, qd3, soma):
        self.tamanhoDaLista = tamanhoDaLista
        self. media = media
        self.mediana = mediana
        self.variancia =variancia
        self.desvioPadrao = desvioPadrao
        self.desvioMedioAbsoluto = desvioMedioAbsoluto
        self.amplitude = amplitude
        self.coeficienteDeVariacao = coeficienteDeVariacao
        self.minimo = min
        self.maximo = max
        self.quartil1 = qd1
        self.quartil2 = qd2
        self.quartil3 = qd3
        self.total = soma
#+=
    def printAnalise(self, nomeDado):
                        return f"\tDado analisado:{nomeDado}\n\nn = {self.tamanhoDaLista}\nmédia = {self.media}\nmediana = {self.mediana}\nmínimo = {self.minimo}\nquartil 1 = {self.quartil1}\nquartil 2 = {self.quartil2}\nquartil 3 = {self.quartil3}\nmáximo = {self.maximo}\nvariancia = {self.variancia}\ndesvio padrão = {self.desvioPadrao}\n desvio médio absoluto = {self.desvioMedioAbsoluto}\namplitude = {self.amplitude}\ntotal = {self.total}"
              