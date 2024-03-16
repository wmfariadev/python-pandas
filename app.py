import pandas as pd
import psycopg2

def import_xls(xls_file, table_name, db_params):
  df = pd.read_excel(xls_file)

  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()

  print('Iniciando importação')

  for _, row in df.iterrows():
    insert_row = (row['nome'], row['endereco'], row['numero'], row['email'], row['telefone'])
    insert_query = f"INSERT INTO {table_name} (nome, endereco, numero, email, telefone) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(insert_query, insert_row)
    print(insert_row)

  conn.commit()
  cursor.close()
  conn.close()

  print('Script finalizado')

def export_xls(table_name, db_params):
  conn = psycopg2.connect(**db_params)
  cursor = conn.cursor()

  print('Iniciando exportação')

  select_query = f"SELECT * FROM {table_name}"
  cursor.execute(select_query)

  print('Executando a query')

  data = cursor.fetchall()

  df = pd.DataFrame(data, columns=[col[0] for col in cursor.description])

  cursor.close()
  conn.close()

  print('Exportar')
  df.to_excel('nova-planilha.xlsx', index=False)

  print('Fim do script')

xls_file = 'clientes-002.xlsx'
table_name = 'cliente'
db_params = {
  'host': 'localhost',
  'database': 'importacao',
  'user': 'postgres',
  'password': 'postgres'
}

# import_xls(xls_file, table_name, db_params)
export_xls(table_name, db_params)