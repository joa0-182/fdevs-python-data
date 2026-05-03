import pandas as pd


def salvar_indicadores(caminho_saida, validacao_volume, validacao_premiacao):
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(caminho_saida, engine="xlsxwriter") as writer:
        validacao_volume.to_excel(
            writer,
            sheet_name="Dados Apuração x Bruto",
            index=False,
        )

        validacao_premiacao.to_excel(
            writer,
            sheet_name="Premiação",
            index=False,
        )
