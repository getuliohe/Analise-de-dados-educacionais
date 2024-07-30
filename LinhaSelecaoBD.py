class LinhaSelecaoBD:

    def __init__(self, totalFaltas = None, porcentagemFrequencia = None , situacao = None, nota1 = None, falta1 = None, media = None, notaFinal = None, mediaFinal = None):
        #     self.totalFaltas = totalFaltas
        #     self.porcentagemFrequencia = porcentagemFrequencia
        #     self.situacao = situacao
        #     self.nota1 = nota1
        #     self.falta1 = falta1
        #     self.media = media
        #     self.notaFinal = notaFinal
        #     self.mediaFinal = mediaFinal
        self.totalFaltas = [] if totalFaltas is None else [totalFaltas]
        self.porcentagemFrequencia = [] if porcentagemFrequencia is None else [porcentagemFrequencia]
        self.situacao = [] if situacao is None else [situacao]
        self.nota1 = [] if nota1 is None else [nota1]
        self.falta1 = [] if falta1 is None else [falta1]
        self.media = [] if media is None else [media]
        self.notaFinal = [] if notaFinal is None else [notaFinal]
        self.mediaFinal = [] if mediaFinal is None else [mediaFinal]

    def adicionarLinha(self, totalFaltas, porcentagemFrequencia, situacao, nota1, falta1, media, notaFinal, mediaFinal):
        self.totalFaltas.append(totalFaltas)
        self.porcentagemFrequencia.append(porcentagemFrequencia)
        self.situacao.append(situacao)
        self.nota1.append(nota1)
        self.falta1.append(falta1)
        self.media.append(media)
        self.notaFinal.append(notaFinal)
        self.mediaFinal.append(mediaFinal)

