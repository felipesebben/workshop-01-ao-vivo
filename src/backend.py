import pandas as pd
from contrato import Vendas
from dotenv import load_dotenv
import os

class ExcelProcessor:
    """
    Classe para processar o arquivo Excel.
    """
    def __init__(self):
        # Carrega as variáveis de ambiente
        load_dotenv(".env")

        # Lê as variáveis de ambiente
        self.POSTGRES_USER = os.getenv('POSTGRES_USER')
        self.POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
        self.POSTGRES_HOST = os.getenv('POSTGRES_HOST')
        self.POSTGRES_PORT = os.getenv('POSTGRES_PORT')
        self.POSTGRES_DB = os.getenv('POSTGRES_DB')

        # Cria a URL de conexão com o banco de dados
        self.DATABASE_URL = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    def process_excel(self, uploaded_file):
        try:
            df = pd.read_excel(uploaded_file)

            # Verificar se há colunas extras no DataFrame
            extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
            if extra_cols:
                return False, f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}"

            # Validar cada linha com o schema escolhido
            for index, row in df.iterrows():
                try:
                    _ = Vendas(**row.to_dict())
                except Exception as e:
                    raise ValueError(f"Erro na linha {index + 2}: {e}")

            return df, True, None

        except ValueError as ve:
            return df, False, str(ve)
        except Exception as e:
            return df, False, f"Erro inesperado: {str(e)}"
        
    def save_dataframe_to_sql(self, df):
        # Salva o DataFrame no banco de dados
        df.to_sql('vendas', con=self.DATABASE_URL, if_exists='replace', index=False)