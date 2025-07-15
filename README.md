📊 Pipeline Airflow + Solr + Docker
Este projeto implementa um pipeline de dados que formata um CSV de alunos e insere os dados no Apache Solr, com orquestração via Apache Airflow. Tudo é executado em containers Docker.

🚀 Tecnologias utilizadas
Python (pandas, pysolr)

Apache Airflow

Apache Solr

Docker e Docker Compose

PostgreSQL e Redis para backend do Airflow

📁 Estrutura do projeto
school-solr-airflow/
├── airflow/
│ ├── dags/ → arquivo da DAG solr_pipeline_dag.py
│ ├── logs/
│ ├── plugins/
├── data/ → alunos.csv e alunos_clean.csv
├── docker/ → docker-compose-airflow.yml, docker-compose-solr.yml e requirements.txt 
├── scripts/ → scripts Python de formatação e carregamento
└── README.md

📦 Pré-requisitos
Docker instalado

docker-compose instalado

🛠️ Como executar o pipeline
Clone o repositório:

git clone https://github.com/seu-usuario/school-solr-airflow.git
cd school-solr-airflow

Coloque o arquivo alunos.csv na pasta data/

Inicie os containers:

docker-compose up --build -d

Acesse:

Airflow: http://localhost:8080 (usuário: admin / senha: admin)

Solr: http://localhost:8983/solr

No Airflow:

Ative a DAG solr_pipeline

Clique em Trigger DAG

Verifique os dados no Solr acessando a collection alunos_collection e rodando a query:

q=:&indent=true

Você verá os documentos inseridos.

🧪 Scripts
format_csv.py → faz limpeza e normalização dos dados, usando pandas

load_to_solr.py → carrega os dados para o Solr, usando pysolr

📝 Observações
As tarefas são orquestradas com Airflow usando CeleryExecutor

O pipeline trata erros simples (valores nulos, campos mal formatados)

Requisitos estão em requirements.txt

✅ Autor
Este projeto foi desenvolvido para fins de avaliação técnica.

👤 Bruno Maia
📧 brunomaia2304@gmail.com