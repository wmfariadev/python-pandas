# Importação e Exportação de Dados com Python e Pandas

Este repositório contém o código-fonte relacionado ao tutorial "Importação e Exportação de Dados com Python e Pandas", onde você aprenderá a importar dados de um arquivo xlsx para um banco de dados PostgreSQL e exportá-los de volta para um arquivo xlsx.

## Instalação

Para executar o projeto, você precisará ter o Python instalado em seu ambiente. Em seguida, instale as dependências executando o seguinte comando:

```bash
pip3 install pandas
```

## Configuração do Banco de Dados e Tabela
Antes de executar o projeto, é necessário configurar o banco de dados e a tabela dentro do arquivo app.py. Adicione as seguintes informações de conexão ao PostgreSQL:
```json
db_params = {
  'host': 'localhost',
  'database': 'importacao',
  'user': 'postgres',
  'password': 'postgres'
}
```
Certifique-se de ter criado a tabela no banco de dados PostgreSQL com os seguintes campos:

- nome
- endereco
- numero
- telefone
- email

Aqui está um exemplo de script SQL para criar essa tabela:
```sql
CREATE TABLE clientes (
    nome VARCHAR(255),
    endereco VARCHAR(255),
    numero VARCHAR(10),
    telefone VARCHAR(15),
    email VARCHAR(100)
);
```

## Como Executar
Após instalar as dependências, você pode rodar o projeto executando o arquivo app.py. Certifique-se de ter configurado corretamente seu ambiente PostgreSQL antes de executar o projeto.

```bash
python app.py
```

Isso iniciará o processo de importação dos dados do arquivo xlsx para o PostgreSQL e, em seguida, exportará os dados do PostgreSQL de volta para um arquivo xlsx.

**Desenvolvido por [William Faria](https://github.com/wmfariadev)**
