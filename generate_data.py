from faker import Faker
import pandas as pd
import os

# Configuração
fake = Faker()
output_dir = 'data/landing'
num_records = 10000

# Função para gerar uma tabela de dados
def generate_table(table_name):
    data = []
    for _ in range(num_records):
        data.append({
            'id': fake.uuid4(),
            'name': fake.name(),
            'email': fake.email(),
            'date': fake.date_between(start_date='-3y', end_date='today'),
            'amount': fake.random_int(min=100, max=10000),
        })
    df = pd.DataFrame(data)
    file_path = os.path.join(output_dir, f"{table_name}.csv")
    df.to_csv(file_path, index=False)
    print(f"Tabela {table_name} gerada em {file_path}")

# Tabelas a serem criadas
tables = ['customers', 'orders', 'products', 'payments', 'suppliers', 'shippings']

# Gerar os arquivos CSV
os.makedirs(output_dir, exist_ok=True)
for table in tables:
    generate_table(table)
