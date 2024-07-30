import matplotlib.pyplot as plt
import numpy as np
from DadosAnalisados import DadosAnalisados
from docx import Document
from docx.shared import Inches


class Analise:
    @staticmethod
    def analise(tabela1,tabela2,anoSemestre,nomeProcura):

        media1 = Analise.__analise__(tabela1.media)

        media2 = Analise.__analise__(tabela2.media)
        
        medias = [media1.media,media2.media]
        Analise.gerarGraficoBloxPLot(tabela2.media, anoSemestre)
        Analise.gerarGraficosBarra(medias, anoSemestre)

        Analise.gerarDocumento(media1.printAnalise("media"),anoSemestre,anoSemestre)
        print(media1.printAnalise("Media"))
        print(tabela2.media)

    @staticmethod
    def __analise__(lista):
        listaAnalisada = DadosAnalisados(
                                    len(lista),
                                    Analise.calculaMedia(lista),
                                    Analise.calcularMediana(lista),
                                    min(Analise.filtrarNulos(lista)),
                                    max(Analise.filtrarNulos(lista)),
                                    Analise.calcularQuadrantes(lista)[0],
                                    Analise.calcularQuadrantes(lista)[1],
                                    Analise.calcularQuadrantes(lista)[2],
                                    Analise.calcularTotal(lista)
                                )
        
        return listaAnalisada


    @staticmethod
    def calculaMedia(lista):
        media = 0
        listaFiltrada = Analise.filtrarNulos(lista)
        totalLinhas = len(listaFiltrada)

        for linha in listaFiltrada:
                media += linha

        media /= totalLinhas
        return media
    
    @staticmethod
    def calcularQuadrantes(lista):

        listaEmRol = sorted(filter(None, lista))
        
        n = len(listaEmRol)
        q1 = listaEmRol[n // 4]
        q2 = listaEmRol[n // 2]
        q3 = listaEmRol[3 * n // 4]
        
        return q1, q2, q3
    
    @staticmethod
    def calcularMediana(lista):
        listaEmRol = sorted(Analise.filtrarNulos(lista))
        n = len(listaEmRol)

        if n % 2 != 0:
            return listaEmRol[(n // 2)]
        else:
            return (listaEmRol[(n // 2) - 1] + listaEmRol[(n // 2)])/2
    
    @staticmethod
    def filtrarNulos(lista):
        listaSemNulos = []

        for item in lista:
            if item != None or item == 0:
                listaSemNulos.append(item)

        return listaSemNulos
    
    @staticmethod
    def calcularTotal(lista):
        total = 0

        for item in lista:
            if item:
                total += item

        return total
    
    def gerarGraficoBloxPLot(lista,anoSemestre):#, nome#):

        plt.figure(figsize=(8,6))
        plt.boxplot(Analise.filtrarNulos(lista), patch_artist=True, showmeans=True, showfliers=True)
        plt.title("Bloxplox da media")
        plt.ylabel('Valores')
        plt.grid(True)
        plt.yticks(range(11))

        plot_path = "plot.png"
        plt.savefig(plot_path)
        plt.close() 

    def gerarGraficosBarra(valores, anoSemestre):
        plt.bar(anoSemestre, valores)

        plt.xlabel('Ano/Semestre')
        plt.ylabel('Média')
        plt.title('Gráfico de Barras')

        plt.grid(True)
        plt.yticks(range(11))
        plt.show()
    
    def gerarDocumento(texto, anos, nomeProcura,pathsGraficos):
        doc = Document()

        doc.add_heading(f"Analise de {nomeProcura} {anos[0]} X {nomeProcura} {anos[1]}")

        doc.add_paragraph(texto)

        for path in pathsGraficos:
            doc.add_heading("Plot Example", level=1)
            doc.add_paragraph("Below is an example of a plot generated using matplotlib:")
            doc.add_picture(path, width=Inches(6))

