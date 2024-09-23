from apps.RecebimentoCSV.conversorJson import convert_to_json
import json

jsonRecebido = convert_to_json('arquivosTeste/Diario_Topicos Avançados_2S2022 - Dados Gerais.csv')

for coluna in jsonRecebido:
    print(f"freq: {coluna['%Freq']}\n")
