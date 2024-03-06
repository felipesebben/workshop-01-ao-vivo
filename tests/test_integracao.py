import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env")

# Ler as variáveis de ambiente
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Criar a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def test_ler_dados_e_checar_schema():
    """
    Executa leitura do banco de dados. Verifica:
    - Se o DataFrame não está vazio.
    - Se o schema (coluna e tipos de dados) está correto.
    """
    df = pd.read_sql("SELECT * FROM vendas", con=DATABASE_URL)

    # Verificar se o DataFrame não está vazio
    assert not df.empty, "O DataFrame está vazio."

    # Verificar se o schema está correto
    expected_dtype = {
        "email": "object",  # `object` em Pandas equivale a `string` em SQL
        "data": "datetime64[ns]",
        "valor": "float64",
        "quantidade": "int64",
        "produto": "object",
        "categoria": "object",
    }
    print(df.dtypes.to_dict())
    assert (
        df.dtypes.to_dict() == expected_dtype
    ), "O schema do DataFrame não corresponde ao esperado."
