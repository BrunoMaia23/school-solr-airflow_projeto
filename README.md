# Pipeline Airflow + Solr + Docker

Este projeto implementa um **pipeline de dados** que formata um CSV de alunos e insere os registros no **Apache Solr**, orquestrado pelo **Apache Airflow**. Toda a infraestrutura roda em containers Docker para facilitar o deploy e garantir portabilidade.

---

## 🚀 Tecnologias Utilizadas

- **Python**: pandas, pysolr
- **Apache Airflow** (CeleryExecutor)
- **Apache Solr**
- **Docker & Docker Compose**
- **PostgreSQL** (metastore do Airflow)
- **Redis** (broker Celery)

---

## 📁 Estrutura do Projeto

```
school-solr-airflow/
├── airflow/
│   ├── dags/                # Definição da DAG (solr_pipeline_dag.py)
│   ├── logs/                # Logs gerados pelo Airflow
│   └── plugins/             # Plugins do Airflow (vazio por padrão)
├── data/                    # Dados de entrada e saída
│   ├── alunos.csv           # CSV original com dados dos alunos
│   └── alunos_clean.csv     # CSV gerado pela task de formatação
├── docker/                  # Arquivos Docker Compose e requirements
│   ├── docker-compose-airflow.yml
│   ├── docker-compose-solr.yml
│   └── requirements.txt     # pandas, pysolr
├── scripts/                 # Scripts Python das tasks
│   ├── format_csv.py        # Formatação e limpeza do CSV
│   └── load_to_solr.py      # Inserção dos dados no Solr
└── README.md                # Este arquivo
```

---

## 📦 Pré-requisitos

Antes de iniciar, instale:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠️ Como Executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/BrunoMaia23/school-solr-airflow_projeto.git
   cd school-solr-airflow_projeto
   ```

2. **Copie o CSV de alunos**
   - Coloque o arquivo `alunos.csv` na pasta `data/`

3. **Suba os containers**
   ```bash
   cd docker
   docker-compose -f docker-compose-solr.yml up -d   # Solr
   docker-compose -f docker-compose-airflow.yml up --build -d  # Airflow + Celery
   ```

4. **Acesse as interfaces**
   - **Airflow UI**: http://localhost:8080  
     Usuário: `admin` / Senha: `admin`
   - **Solr Admin**: http://localhost:8983/solr

5. **Execute o pipeline**
   - Na Airflow UI, ative a DAG `solr_pipeline` (toggle On)
   - Clique em **Trigger DAG**

6. **Verifique no Solr**
   - No Solr Admin, selecione a **collection** `alunos_collection`  
   - Clique em **Query** e execute sem filtros (`q=*:*`)  
   - Você verá os documentos inseridos pelo pipeline

---

## 🧪 Descrição dos Scripts

- **scripts/format_csv.py**  
  - Lê `alunos.csv` com pandas
  - Remove linhas com campos obrigatórios vazios
  - Padroniza nomes e converte datas
  - Calcula idade a partir de `Data de Nascimento`
  - Salva o CSV limpo em `alunos_clean.csv`

- **scripts/load_to_solr.py**  
  - Lê `alunos_clean.csv`
  - Constrói documentos no formato esperado pelo Solr
  - Conecta ao Solr via pysolr e insere os documentos

---

## 📝 Observações

- **Executor**: utiliza CeleryExecutor para escalabilidade das tasks
- **Tratamento de erros**: validações no Python para dados faltantes e logging de falhas
- **Dependências**: listadas em `docker/requirements.txt`

---

## ✅ Autor

**Bruno Maia**  
📧 brunomaia2304@gmail.com

Este projeto foi desenvolvido para atender ao desafio técnico de **Importação de Dados para o Solr com Orquestração via Airflow**.
