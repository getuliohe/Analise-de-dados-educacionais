from apps.conexaoBD.ConexaoBD import ConexaoBD

class Selecoes:
    def __init__(self, anoSemestre, campus , curso = None, disciplina = None):
        self.campus = campus
        self.curso = curso
        self.disciplina = disciplina
        self.anoSemestre = anoSemestre
        self.__escolherTipo__()

    def __escolherTipo__(self):
        if(self.disciplina):
            ConexaoBD.procuraBDdisciplina(self)
        elif(self.curso):
            ConexaoBD.procuraBDcurso(self)
        elif(self.campus):
            ConexaoBD.procuraBdCampus(self)
        else:
            print("erro __escolherTipo__")
