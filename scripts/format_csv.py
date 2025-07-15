import pandas as pd

def format_csv(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    df = df.dropna(subset=['Nome', 'Data de Nascimento'])
    df['Nome'] = df['Nome'].str.strip().str.title()
    df['Data de Nascimento'] = pd.to_datetime(df['Data de Nascimento'], errors='coerce')
    hoje = pd.Timestamp('today')
    df['Idade_Calc'] = ((hoje - df['Data de Nascimento']).dt.days // 365)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    import sys
    _, inp, outp = sys.argv
    format_csv(inp, outp)

