from typing import Literal
import pytest
from conversores_temp import converter_temperatura


@pytest.mark.happy_path
@pytest.mark.parametrize(
    "valor, de_escala, para_escala, situacao_esperada ",
    [
        (32,"KELVIN","CELSIUS", -241.15),
        (32,"KELVIN","FAHRENHEIT", -402.07),
        (32, "KELVIN","KELVIN", 32),

        (32,"CELSIUS","KELVIN", 305.15),
        (32,"CELSIUS","FAHRENHEIT", 89,6),
        (32, "CELSIUS","CELSIUS", 32),

        (32,"FAHRENHEIT","KELVIN", 273.15),
        (32,"FAHRENHEIT","CELSIUS", 0),
        (32, "FAHRENHEIT","FAHRENHEIT", 32),
        
    ]
)
def test_converter_temperatura_happy_path(valor: float, de_escala:str, para_escala: str, situacao_esperada: float | Literal[0]):
    resultado = converter_temperatura(valor,de_escala,para_escala)

    assert resultado == pytest.approx(situacao_esperada, 0.5)

# @pytest.mark.error_path
# @pytest.mark.parametrize(
#     "valor,de_escala,para_escala,situacao_esperada",
#     [
#         ()
#     ]
# )