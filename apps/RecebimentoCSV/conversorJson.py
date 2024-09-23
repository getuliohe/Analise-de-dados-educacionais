import sys
import pandas as pd

def convert_to_json(input_file):
    try:
        # Verifica a extensão do arquivo e carrega o arquivo
        if input_file.endswith('.xlsx'):
            arquivo = pd.read_excel(input_file)  # Arquivo Excel
        elif input_file.endswith('.csv') or input_file.endswith('.txt'):
            arquivo = pd.read_csv(input_file)  # Arquivo CSV ou texto
        else:
            print(f"Formato de arquivo {input_file} não suportado.")
            return
        

        json_data = arquivo.to_dict(orient='records')
        return json_data
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_to_json(input_file, output_file)
    else:
        print("Por favor, forneça o arquivo de entrada e o nome do arquivo de saída.")
