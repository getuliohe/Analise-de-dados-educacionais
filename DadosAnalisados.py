class DadosAnalisados:
    def __init__(self, tamanhoDaLista, media, mediana, min, max, qd1, qd2, qd3, soma):
        self.tamanhoDaLista = tamanhoDaLista
        self. media = media
        self.mediana = mediana
        self.min = min
        self.max = max
        self.qd1 = qd1
        self.qd2 = qd2
        self.qd3 = qd3
        self.soma = soma
#+=
    def printAnalise(self, nomeDado):
                        return f"{nomeDado}\n\n" + f"n = {self.tamanhoDaLista}\n" + f"media = {self.media}\n" + f"mediana = {self.mediana}\n\n" + f"min = {self.min}\n" + f"qd1 = {self.qd1}\n" + f"qd2 = {self.qd2}\n" + f"qd3 = {self.qd3}\n" + f"max = {self.max}\n" +f"soma = {self.soma}\n"
              