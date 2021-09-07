precipitacao_hoje = 120


def teste(variavel_meteorologica):
    if precipitacao_hoje > 60:
        return f"""Precipitação forte ({variavel_meteorologica} mm/h) : 
        ALERTA!!!! CONTATE URGENTE A DEFESA CIVIL 999"""

    elif precipitacao_hoje < 60 and precipitacao_hoje >= 5.1:
        return f'Precipitação moderada ({variavel_meteorologica} mm/h) : REQUER MONITORAMENTO'

    elif precipitacao_hoje < 5.1 and precipitacao_hoje >= 1.1:
        return f'Precipitação fraca ({variavel_meteorologica} mm/h) : TEMPO NORMAL'

    else:
        return f'Sem precipitação'


print(teste(precipitacao_hoje))
