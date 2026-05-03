CFOP_CAMPANHA = [
    5102, 5106, 5110, 6102, 6106, 6110, 5160, 6160, 6910, 5910
]


def filtrar_dados_brutos(
    relatorio_bruto,
    configuracao_campanha_cliente,
    configuracao_campanha_produto,
):
    dados_brutos = relatorio_bruto[
        relatorio_bruto["CODIGOCLIENTE"].isin(
            configuracao_campanha_cliente["CODIGOCLIENTE"]
        )
    ]

    dados_brutos = dados_brutos[
        dados_brutos["CODIGOPRODUTO"].isin(
            configuracao_campanha_produto["CODIGOPRODUTO"]
        )
    ]

    dados_brutos = dados_brutos[dados_brutos["CFOP"].isin(CFOP_CAMPANHA)]

    dados_brutos = dados_brutos.rename(columns={
        "VOLUME": "VOLUME BRUTO"
    })

    return dados_brutos
