from pathlib import Path

from src.extract import carregar_dados
from src.transform import filtrar_dados_brutos
from src.validate import validar_premiacao, validar_volume
from src.load import salvar_indicadores


def main():
    pasta_projeto = Path(__file__).parent
    pasta_input = pasta_projeto / "data" / "input"
    pasta_output = pasta_projeto / "data" / "output"

    print("Carregando dados...")
    dados = carregar_dados(pasta_input)

    print("Aplicando filtros...")
    dados_brutos_filtrados = filtrar_dados_brutos(
        dados["relatorio_bruto"],
        dados["configuracao_campanha_cliente"],
        dados["configuracao_campanha_produto"],
    )

    print("Executando validacao de volume...")
    validacao_volume = validar_volume(
        dados["relatorio_campanha_detalhe"],
        dados_brutos_filtrados,
    )

    print("Executando validacao de premiacao...")
    validacao_premiacao = validar_premiacao(
        dados["relatorio_campanha_premiacao"],
        dados["relatorio_campanha_detalhe"],
    )

    print("Salvando arquivo...")
    caminho_saida = pasta_output / "Indicadores.xlsx"
    salvar_indicadores(caminho_saida, validacao_volume, validacao_premiacao)

    print(f"Processo finalizado: {caminho_saida}")


if __name__ == "__main__":
    main()
