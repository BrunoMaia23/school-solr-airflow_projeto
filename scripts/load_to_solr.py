import pandas as pd
import pysolr

def load_to_solr(solr_url: str, csv_path: str):
    solr = pysolr.Solr(solr_url, always_commit=True, timeout=10)
    df = pd.read_csv(csv_path)

    docs = []
    for _, row in df.iterrows():
        try:
            doc = {
                'id': f"{row['Nome']}_{row['Data de Nascimento']}",
                'nome': row['Nome'],
                'idade': int(row['Idade']),
                'serie': str(row.get('Série', row.get('Serie', ''))),
                'nota_media': float(row['Nota Média']),
                'endereco': row['Endereço'],
                'nome_pai': row['Nome do Pai'],
                'nome_mae': row['Nome da Mãe'],
                'data_nascimento': row['Data de Nascimento']
            }
            docs.append(doc)
        except Exception as e:
            print(f"Erro ao processar linha: {e}")
    
    solr.add(docs)
    print(f"{len(docs)} documentos inseridos no Solr.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python load_to_solr.py <solr_url> <csv_path>")
        sys.exit(1)
    solr_url, csv_path = sys.argv[1], sys.argv[2]
    load_to_solr(solr_url, csv_path)
