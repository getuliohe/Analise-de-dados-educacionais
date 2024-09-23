from ..Analise.Analise import Analise
from ..Analise.LinhaSelecaoBD import LinhaSelecaoBD
import mysql.connector

class ConexaoBD:

    @staticmethod
    def retorna_conexao():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="bussola"
        )
    
    
    @staticmethod
    def procuraBDdisciplina(procura):
        conn = ConexaoBD.retorna_conexao()

        nomeTabela = []

        cursor = conn.cursor()
        queryNomeTabela = [f"select nomeTabela from (SELECT nomeCampus, nomeTabela, idCurso, nomeDisciplina, anoSemestre FROM (SELECT nomeCampus,idDisciplina,nomeTabela, anoSemestre FROM `lista de tabelas` as y INNER JOIN campus on y.idCampus = campus.idCampus) as a inner join `disciplinas` on  a.idDisciplina = `disciplinas`.idDisciplina) as b inner join `cursos` on b.idCurso = `cursos`.idCurso WHERE nomeCurso = \"{procura.curso}\" and nomeCampus = \"{procura.campus}\" and nomeDisciplina = \"{procura.disciplina}\" and anoSemestre = {procura.anoSemestre[0]};", f"select nomeTabela from (SELECT nomeCampus, nomeTabela, idCurso, nomeDisciplina, anoSemestre FROM (SELECT nomeCampus ,idDisciplina,nomeTabela, anoSemestre FROM `lista de tabelas` as y INNER JOIN campus on y.idCampus = campus.idCampus) as a inner join `disciplinas` on  a.idDisciplina = `disciplinas`.idDisciplina) as b inner join `cursos` on b.idCurso = `cursos`.idCurso WHERE curso = \"{procura.curso}\" and nomeCampus = \"{procura.campus}\" and nomeDisciplina = \"{procura.disciplina}\" and anoSemestre = {procura.anoSemestre[1]};"]
        
        cursor.execute(queryNomeTabela[0])
        nomeTabela.append( cursor.fetchall()[0][0])

        cursor.execute(queryNomeTabela[1])
        nomeTabela.append(cursor.fetchall()[0][0])

        query = [f"SELECT * FROM `{nomeTabela[0]}`",
                 f"SELECT * FROM `{nomeTabela[1]}`"]

        cursor.execute(query[0])

        resultados1 = cursor.fetchall()

        cursor.execute(query[1])
        resultados2 = cursor.fetchall()

        cursor.close()
        conn.close()
        
        tabela1 = LinhaSelecaoBD()
        tabela2 = LinhaSelecaoBD()

        for resultado in resultados1:
            tabela1.adicionarLinha(resultado[0], 
                                    resultado[1], 
                                    resultado[2], 
                                    resultado[3],
                                    resultado[4], 
                                    resultado[5], 
                                    resultado[6], 
                                    resultado[7])

        for resultado in resultados2:
            tabela2.adicionarLinha(resultado[0], 
                                    resultado[1], 
                                    resultado[2], 
                                    resultado[3],
                                    resultado[4], 
                                    resultado[5], 
                                    resultado[6], 
                                    resultado[7])
        
        Analise.analise(tabela1,tabela2,procura.anoSemestre, procura.disciplina)
            

    @staticmethod
    def procuraBDcurso(procura):
        listaProcura1 = []
        listaProcura2 = []
        resultados1 = []
        resultados2 = []
        tabela1 = LinhaSelecaoBD()
        tabela2 = LinhaSelecaoBD()
        
        conn = ConexaoBD.retorna_conexao()

        cursor = conn.cursor()
        
        query = [f"SELECT nomeTabela FROM (SELECT nomeCurso, y.idCampus ,nomeTabela, anoSemestre FROM `cursos` INNER JOIN `lista de tabelas`as y on `cursos`.idCurso = y.idCurso) AS A INNER JOIN campus ON A.idCampus = campus.idCampus WHERE A.nomeCurso = \"{procura.curso}\" AND A.anoSemestre = \"{procura.anoSemestre[0]}\" and nomeCampus = \"{procura.campus}\";", 
                 f"SELECT nomeTabela FROM (SELECT nomeCurso, y.idCampus ,nomeTabela, anoSemestre FROM `cursos` INNER JOIN `lista de tabelas`as y on `cursos`.idCurso = y.idCurso) AS A INNER JOIN campus ON A.idCampus = campus.idCampus WHERE A.nomeCurso = \"{procura.curso}\" AND A.anoSemestre = \"{procura.anoSemestre[1]}\" and nomeCampus = \"{procura.campus}\";"]

        cursor.execute(query[0])

        listaProcura1 = cursor.fetchall()

        cursor.execute(query[1])
        listaProcura2 = cursor.fetchall()

        for pesquisa in listaProcura1:
            query = f"SELECT * FROM `{pesquisa[0]}`"
            cursor.execute(query)
            resultados1.append(cursor.fetchall())

        for pesquisa in listaProcura2:
            query = f"SELECT * FROM `{pesquisa[0]}`"
            cursor.execute(query)
            resultados2.append(cursor.fetchall())
        
        for resultados in resultados1:
            for resultado in resultados:
                tabela1.adicionarLinha(resultado[0], 
                                            resultado[1],
                                            resultado[2],
                                            resultado[3],
                                            resultado[4], 
                                            resultado[5], 
                                            resultado[6], 
                                            resultado[7])
                
        for resultados in resultados2:
            for resultado in resultados:
                tabela2.adicionarLinha(resultado[0], 
                                            resultado[1],
                                            resultado[2],
                                            resultado[3],
                                            resultado[4], 
                                            resultado[5], 
                                            resultado[6], 
                                            resultado[7])

        cursor.close()
        conn.close()

        Analise.analise(tabela1,tabela2,procura.anoSemestre,procura.curso)


    @staticmethod
    def procuraBdCampus(procura):
        listaProcura1 = []
        listaProcura2 = []
        resultados1 = []
        resultados2 = []
        tabela1 = LinhaSelecaoBD()
        tabela2 = LinhaSelecaoBD()
        
        conn = ConexaoBD.retorna_conexao()

        cursor = conn.cursor()
        
        query = [f"select nomeTabela from  `lista de tabelas` AS A INNER JOIN `campus` AS B ON A.idCampus = B.idCampus WHERE B.nomeCampus = \"{procura.campus}\" AND A.anoSemestre = \"{procura.anoSemestre[0]}\";", 
                 f"select nomeTabela from  `lista de tabelas` AS A INNER JOIN `campus` AS B ON A.idCampus = B.idCampus WHERE B.nomeCampus = \"{procura.campus}\" AND A.anoSemestre = \"{procura.anoSemestre[1]}\";"]

        cursor.execute(query[0])

        listaProcura1 = cursor.fetchall()

        cursor.execute(query[1])
        listaProcura2 = cursor.fetchall()

        for pesquisa in listaProcura1:
            query = f"SELECT * FROM `{pesquisa[0]}`"
            cursor.execute(query)
            resultados1.append(cursor.fetchall())

        for pesquisa in listaProcura2:
            query = f"SELECT * FROM `{pesquisa[0]}`"
            cursor.execute(query)
            resultados2.append(cursor.fetchall())
        
        for resultados in resultados1:
            for resultado in resultados:
                tabela1.adicionarLinha(resultado[0], 
                                            resultado[1],
                                            resultado[2],
                                            resultado[3],
                                            resultado[4], 
                                            resultado[5], 
                                            resultado[6], 
                                            resultado[7])
                
        for resultados in resultados2:
            for resultado in resultados:
                tabela2.adicionarLinha(resultado[0], 
                                            resultado[1],
                                            resultado[2],
                                            resultado[3],
                                            resultado[4], 
                                            resultado[5], 
                                            resultado[6], 
                                            resultado[7])

        cursor.close()
        conn.close()
        
        Analise.analise(tabela1,tabela2,procura.anoSemestre, procura.campus)