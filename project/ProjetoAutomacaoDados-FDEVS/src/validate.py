import numpy as np
import pandas as pd

from src.rules import percentual_premiacao_crescimento, validar_multiplas_regras


def validar_volume(relatorio_campanha_detalhe, dados_brutos):
    validacao_volume_campanha_bruto = pd.merge(
        relatorio_campanha_detalhe,
        dados_brutos[[
            "CODIGOCLIENTE",
            "CODIGODOCUMENTO",
            "CODIGOPRODUTO",
            "VOLUME BRUTO",
        ]],
        how="inner",
        on=["CODIGOCLIENTE", "CODIGODOCUMENTO", "CODIGOPRODUTO"],
    )

    validacao_volume_campanha_bruto["Validação"] = np.where(
        validacao_volume_campanha_bruto["VOLUME"]
        != validacao_volume_campanha_bruto["VOLUME BRUTO"],
        "Divergente",
        "Correto",
    )

    return validacao_volume_campanha_bruto


def validar_premiacao(relatorio_campanha_premiacao, relatorio_campanha_detalhe):
    campanha_detalhe = (
        relatorio_campanha_detalhe.groupby(["CODIGOCLIENTE", "CODIGOPRODUTO"])
        ["VOLUME"].sum()
        .reset_index()
    )

    validacao_premiacao = pd.merge(
        relatorio_campanha_premiacao,
        campanha_detalhe,
        how="left",
        on=["CODIGOCLIENTE", "CODIGOPRODUTO"],
    )

    validacao_premiacao["% Crescimento Calculado"] = (
        (validacao_premiacao["VOLUMEREALIZADO"]
         / validacao_premiacao["METAVOLUMEVENDA"]) - 1
    ).round(4)

    validacao_premiacao["% Premiação Calculado"] = validacao_premiacao[
        "% Crescimento Calculado"
    ].apply(percentual_premiacao_crescimento)

    validacao_premiacao["Valor Premiacao Calculado"] = (
        validacao_premiacao["VALORVENDAPREMIACAO"]
        * validacao_premiacao["% Premiação Calculado"]
    )

    validacao_premiacao["Validação"] = validar_multiplas_regras(
        validacao_premiacao,
        regras=[
            (
                validacao_premiacao["% Premiação Calculado"]
                != validacao_premiacao["PERCENTUALPREMIACAO"],
                "Percentual Premiação divergente do Cálculo",
            ),
            (
                validacao_premiacao["VALORPREMIACAO"]
                != validacao_premiacao["Valor Premiacao Calculado"],
                "Valor Premiação divergente do Cálculo",
            ),
        ],
    )

    return validacao_premiacao
