from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator


class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"


class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.

    Attributes:
        `email` (`str`): Email do cliente.
        `data` (`datetime`): Data da venda.
        `valor` (`float`): Valor da venda.
        `produto` (`str`): Nome do produto.
        `quantidade` (`int`): Quantidade de produtos.
        `categoria` (`str`): Categoria do produto.

    """

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    produto: str
    quantidade: PositiveInt
    categoria: CategoriaEnum

    @field_validator("categoria")
    def categoria_deve_estar_no_enum(cls, error):
        return error
