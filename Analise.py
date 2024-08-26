import matplotlib.pyplot as plt
import numpy as np
from DadosAnalisados import DadosAnalisados
from docx import Document
from docx.shared import Inches
import math


class Analise:
    @staticmethod
    def analise(tabela1,tabela2,anoSemestre,nomeProcura):

        media1 = Analise.__analise__(tabela1.media)

        media2 = Analise.__analise__(tabela2.media)
        
        medias = [media1.media,media2.media]

        listaPathGrafico = []
        listaPathGrafico.append(Analise.gerarGraficoBoxPLot(tabela2.media, anoSemestre[0], "media", nomeProcura))
        listaPathGrafico.append(Analise.gerarGraficosBarra(medias, anoSemestre, "media", nomeProcura))

        Analise.gerarDocumento(media1.printAnalise("media"), anoSemestre, nomeProcura, listaPathGrafico)

    @staticmethod
    def __analise__(lista):
        listaAnalisada = DadosAnalisados(
                                    len(lista),
                                    Analise.calculaMedia(lista),
                                    Analise.calcularMediana(lista),
                                    Analise.calcularVariancia(lista),
                                    Analise.calcularDesvioPadrao(lista),
                                    Analise.calcularDesvioMedioAbsoluto(lista),
                                    Analise.calcularAmplitude(lista),
                                    Analise.calcularCoeficienteDeVaricao(lista),
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
        # Filtrar None e ordenar a lista
        listaEmRol = sorted(filter(None, lista))
        
        def calcularQ1(lista):
            n = len(lista)
            if n % 2 == 0:
                return (lista[n//4 - 1] + lista[n//4]) / 2
            else:
                return lista[n//4]

        def calcularQ2(lista):
            n = len(lista)
            if n % 2 == 0:
                return (lista[n//2 - 1] + lista[n//2]) / 2
            else:
                return lista[n//2]

        def calcularQ3(lista):
            n = len(lista)
            if n % 2 == 0:
                return (lista[(3*n)//4 - 1] + lista[(3*n)//4]) / 2
            else:
                return lista[(3*n)//4]
            
        return calcularQ1(lista), calcularQ2(lista), calcularQ3(lista)

    
    @staticmethod
    def calcularMediana(lista):
        listaEmRol = sorted(Analise.filtrarNulos(lista))
        n = len(listaEmRol)

        if n % 2 != 0:
            return listaEmRol[(n // 2)]
        else:
            return (listaEmRol[(n // 2) - 1] + listaEmRol[(n // 2)])/2
    
    @staticmethod
    def calcularVariancia(lista):
        listaFiltrada = Analise.filtrarNulos(lista)
        media = Analise.calculaMedia(lista)
        total = 0

        for item in listaFiltrada:
            total += (item - media)**2
        
        return total/(len(listaFiltrada)- 1)
    
    @staticmethod
    def calcularDesvioPadrao(lista):
        return math.sqrt(Analise.calcularVariancia(lista))
    
    @staticmethod
    def calcularDesvioMedioAbsoluto(lista):
        listaFiltrada = Analise.filtrarNulos(lista)
        media = Analise.calculaMedia(lista)
        total = [abs(x - media) for x in listaFiltrada]
        
        return sum(total)/len(listaFiltrada)
    
    @staticmethod
    def calcularAmplitude(lista):
        return (max(Analise.filtrarNulos(lista)) - min(Analise.filtrarNulos(lista)))
    
    @staticmethod
    def calcularCoeficienteDeVaricao(lista):
        media = Analise.calculaMedia(lista)

        return (Analise.calcularDesvioPadrao(lista)/ media) * 100
    
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
    
    def gerarGraficoBoxPLot(lista,anoSemestre, dadoanalisado, listaAnalisada):#, nome#):

        plt.figure(figsize=(8,6))
        plt.boxplot(Analise.filtrarNulos(lista), patch_artist=True, showmeans=True, showfliers=True)
        plt.title("Bloxplox da media")
        plt.ylabel('Valores')
        plt.grid(True)
        plt.yticks(range(11))

        plot_path = f"{listaAnalisada + dadoanalisado + anoSemestre}.png"
        plt.savefig(plot_path)
        plt.close()

        return plot_path

    def gerarGraficosBarra(valores, anoSemestre, dadoanalisado, listaAnalisada):
        plt.bar(anoSemestre, valores)

        plt.xlabel('Ano/Semestre')
        plt.ylabel('Média')
        plt.title('Gráfico de Barras')

        plt.grid(True)
        plt.yticks(range(11))

        plot_path = f"{listaAnalisada + dadoanalisado + anoSemestre[0] + anoSemestre[1] }.png"
        plt.savefig(plot_path)
        plt.close()

        return plot_path
    
    def gerarDocumento(texto, anos, nomeProcura,pathsGraficos):
        doc = Document()

        doc.add_heading(f"Analise de {nomeProcura} {anos[0]} X {nomeProcura} {anos[1]}")

        doc.add_paragraph(texto)

        for path in pathsGraficos:
            doc.add_heading(path, level=1)
            doc.add_picture(path, width=Inches(6))
        
        doc.save(f"{nomeProcura + anos[0] + anos[1]}.docx")


