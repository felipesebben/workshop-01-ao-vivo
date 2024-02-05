import pytest
from datetime import datetime
from src.contrato import Vendas
from pydantic import ValidationError


def test_vendas_com_dados_validos():
    """
    Testa a criação de uma instância de Vendas com dados válidos.
    
    Este teste verifica se a classe Vendas aceita e armazena corretamente os dados válidos passados para o construtor.
    Dados válidos incluem:
    - email correto
    - data atual válida
    - valor positivo
    - produto não vazio
    - quantidade positiva
    - categoria válida
    O teste confirma se os valores armazenados na instância de Vendas são iguais aos valores passados para o construtor.	
    """
    dados_validos = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto X",
        "quantidade": 3,
        "categoria": "categoria inexistente",
    }

    
    # A sintaxe **dados_validos é uma forma de desempacotamento de dicionários em Python. 
    # O que isso faz é passar os pares chave-valor no dicionário dados_validos como argumentos nomeados para o construtor da classe Vendas.

    venda = Vendas(**dados_validos)

    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.valor == dados_validos["valor"]
    assert venda.produto == dados_validos["produto"]
    assert venda.quantidade == dados_validos["quantidade"]
    assert venda.categoria == dados_validos["categoria"]

# Testes com dados inválidos
def test_vendas_com_dados_invalidos():
    """
    Testa a criação de uma instância de Vendas com dados inválidos.

    Este teste verifica se a classe Vendas levanta uma exceção `ValidationError` quando dados inválidos são passados para o construtor. 
    Dados inválidos incluem:
    - email inválido
    - data inválida
    - valor negativo
    - produto vazio
    - quantidade negativa
    - categoria inválida
    Espera-se que a classe Vendas levante uma exceção `ValidationError` quando dados inválidos são passados para o construtor.
    """
    dados_invalidos = {
        "email": "comprador",
        "data": "não é uma data",
        "valor": -100,
        "produto": "",
        "quantidade": -1,
        "categoria": "categoria3"
    }

    with pytest.raises(ValidationError):
        Vendas(**dados_invalidos)

# Teste de validação de categoria
def test_validacao_categoria():
    """
    Testa a validação da categoria na criação de uma instância de Vendas.

    Este teste especificamente verifica se a classe Vendas valida a categoria passada para o construtor.
    Utiliza-se dados válidos para todos os campos exceto para a categoria, que é inválida e definida como "categoria inexistente".
    Espera-se que a classe Vendas levante uma exceção `ValidationError` quando a categoria é inválida.

    args:
        dados = {
            "email": comprador@example.com,
            "data": datetime.now(),
            "valor": 100.50,
            "produto": Produto Y,
            quantidade: 1,
            categoria: categoria inexistente
        }
    """
    dados = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto Y",
        "quantidade": 1,
        "categoria": "categoria inexistente",
    }

    with pytest.raises(ValidationError):
        Vendas(**dados)