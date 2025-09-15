# Descrição do Problema: 
# Você deve criar os testes para a função
# converter_temperatura(valor, de_escala, para_escala). A função recebe um
# float ou int para o valor e duas strings para as escalas.

# Regras da Função:
# 
# 1. Validação de Escalas: As strings de_escala e para_escala devem ser,
# insensíveis a maiúsculas/minúsculas, uma das seguintes: &quot;CELSIUS&quot;,
# &quot;FAHRENHEIT&quot;, &quot;KELVIN&quot;. Se qualquer uma for inválida, a função deve
# levantar ValueError com a mensagem &quot;Escala de temperatura inválida&quot;.
# 
# 2. Validação de Valor: O valor para a escala KELVIN não pode ser abaixo do
# zero absoluto (-273.15 °C). Se a de_escala for &quot;KELVIN&quot; e o valor for
# negativo, a função deve levantar ValueError com a mensagem &quot;Temperatura
# em KELVIN não pode ser negativa&quot;.
# 
# 3. Lógica de Conversão: A função deve realizar a conversão corretamente entre as
# escalas.
# 4. Resultado: A função deve retornar o valor da temperatura convertida como um
# float. Se as escalas de origem e destino forem as mesmas, deve retornar o valor
# original.

def converter_temperatura(valor:float, de_escala:str,para_escala:str):
    # 1 Validação de Escalas:
    if (de_escala != "CELSIUS" and de_escala != "FAHRENHEIT" and de_escala != "KELVIN"):
        raise ValueError("Escala de temperatura inválida")
    
    if (para_escala != "CELSIUS" and para_escala != "FAHRENHEIT" and para_escala != "KELVIN"):
        raise ValueError("Escala de temperatura inválida")
    
    # 2 Validação de Valor:
    
    if (de_escala == "KELVIN" and valor < 0 ):
        raise ValueError("Temperatura em KELVIN não pode ser negativa")
    
    # 3 Lógica de Conversão:
    