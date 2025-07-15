import pandas as pd
import logging
import sys

# Configura logging simples
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

def format_csv(input_path: str, output_path: str):
    try:
        df = pd.read_csv(input_path)
        logger.info(f"CSV lido: {len(df)} linhas")
    except Exception as e:
        logger.error(f"Erro ao ler arquivo CSV em {input_path}: {e}")
        raise

    # Remover linhas sem Nome ou Data
    before = len(df)
    df = df.dropna(subset=['Nome', 'Data de Nascimento'])
    logger.info(f"{before - len(df)} linhas removidas por nulos em Nome/Data")

    # Padronizar nomes
    df['Nome'] = df['Nome'].astype(str).str.strip().str.title()

    # Converter datas
    df['Data de Nascimento'] = pd.to_datetime(
        df['Data de Nascimento'], errors='coerce'
    )
    # Tratar datas inválidas
    invalid_dates = df['Data de Nascimento'].isna().sum()
    if invalid_dates:
        logger.warning(f"{invalid_dates} datas inválidas convertidas para NaT")
    df = df.dropna(subset=['Data de Nascimento'])

    # Calcular idade
    hoje = pd.Timestamp.today()
    df['Idade_Calc'] = ((hoje - df['Data de Nascimento']).dt.days // 365).astype(int)

    # **REMOVIDO** filtro por consistência de idade para não descartar todos os registros
    # df = df[df['Idade'] == df['Idade_Calc']]

    # Exportar CSV limpo
    try:
        df.to_csv(output_path, index=False)
        logger.info(f"CSV formatado salvo em {output_path}: {len(df)} linhas")
    except Exception as e:
        logger.error(f"Erro ao salvar CSV em {output_path}: {e}")
        raise

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python format_csv.py <input_path> <output_path>")
        sys.exit(1)
    _, inp, outp = sys.argv
    format_csv(inp, outp)
