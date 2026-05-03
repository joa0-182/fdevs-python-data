import pandas as pd


def carregar_dados(pasta_input):
    arquivo_campanha = pasta_input / "Campanha Incentivo - Distribuição Vinho.xlsx"
    arquivo_configuracao = pasta_input / "Configuracao da Campanha.xlsx"
    arquivo_bruto = pasta_input / "Dados_Brutos.csv"

    relatorio_campanha_premiacao = pd.read_excel(
        arquivo_campanha,
        sheet_name="Premiação Distribuidores",
    )

    relatorio_campanha_detalhe = pd.read_excel(
        arquivo_campanha,
        sheet_name="Detalhamento Mês Apurado",
    )

    configuracao_campanha_cliente = pd.read_excel(
        arquivo_configuracao,
        sheet_name="Cliente",
    )

    configuracao_campanha_produto = pd.read_excel(
        arquivo_configuracao,
        sheet_name="Produto",
    )

    relatorio_bruto = pd.read_csv(
        arquivo_bruto,
        sep=";",
        encoding="utf-8",
        dtype={"NUMERODOCUMENTO": "str"},
    )

    return {
        "relatorio_campanha_premiacao": relatorio_campanha_premiacao,
        "relatorio_campanha_detalhe": relatorio_campanha_detalhe,
        "configuracao_campanha_cliente": configuracao_campanha_cliente,
        "configuracao_campanha_produto": configuracao_campanha_produto,
        "relatorio_bruto": relatorio_bruto,
    }
