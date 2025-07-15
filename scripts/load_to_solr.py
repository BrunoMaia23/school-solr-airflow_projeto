import pandas as pd
import pysolr

def load_to_solr(solr_url: str, csv_path: str):
    # Conecta ao Solr
    solr = pysolr.Solr(solr_url, always_commit=True, timeout=10)
    # Lê CSV pré-formatado
    df = pd.read_csv(csv_path)
    docs = []
    for _, row in df.iterrows():
        docs.append({
            'id': f"{row['Nome']}_{row['Data de Nascimento']}",
            'nome': row['Nome'],
            'idade': int(row['Idade']),
            # Usa get para colunas com ou sem acento
            'serie': str(row.get('Série', row.get('Serie', ''))),
            'nota_media': float(row['Nota Média']),
            'endereco': row['Endereço'],
            'nome_pai': row['Nome do Pai'],
            'nome_mae': row['Nome da Mãe'],
            'data_nascimento': row['Data de Nascimento']
        })
    # Insere documentos no Solr
    solr.add(docs)
    print(f"{len(docs)} documentos inseridos no Solr.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print('Uso: python load_to_solr.py <solr_url> <csv_path>')
        sys.exit(1)
    url, path = sys.argv[1], sys.argv[2]
    load_to_solr(url, path)