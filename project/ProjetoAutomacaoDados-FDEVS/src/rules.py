import numpy as np


def validar_multiplas_regras(dataframe, regras, separador=" | "):
    """
    Aplica multiplas regras vetorizadas e retorna uma unica coluna:
    - "Correto" se nenhuma regra falhar
    - texto com os motivos se houver divergencias
    """
    mensagens = np.full(len(dataframe), "", dtype=object)

    for mascara, texto in regras:
        mensagens = np.where(
            mascara,
            np.where(
                mensagens == "",
                texto,
                mensagens + separador + texto,
            ),
            mensagens,
        )

    return np.where(mensagens == "", "Correto", mensagens)


def percentual_premiacao_crescimento(crescimento):
    # Ordem do maior para o menor
    if crescimento >= 0.20:
        return 0.10
    if crescimento >= 0.15:
        return 0.08
    if crescimento >= 0.10:
        return 0.06
    if crescimento >= 0.05:
        return 0.03

    return 0.0
