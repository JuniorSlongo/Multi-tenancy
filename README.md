# Multi Tenancy com Flask e PostgreSQL

## Objetivo

O objetivo deste projeto é demonstrar uma implementação básica de Multi Tenancy usando o framework Flask em Python e o banco de dados PostgreSQL. A estratégia de Multi Tenancy escolhida para este projeto é a **Shared Database, Shared Schema**.

## Estratégia de Multi Tenancy

Na estratégia de **Shared Database, Shared Schema**, todos os clientes (tenants) compartilham o mesmo banco de dados e o mesmo esquema. Os dados dos clientes são diferenciados por uma coluna de identificação do inquilino em cada tabela. Isso permite que vários clientes usem a mesma instância da aplicação e do banco de dados, com seus dados devidamente isolados.

## Aplicação Desenvolvida

A aplicação desenvolvida neste projeto é uma aplicação web simples usando o framework Flask. A aplicação permite aos usuários:

- Visualizar uma lista de usuários cadastrados.
- Adicionar novos usuários.

Os dados dos usuários são armazenados em uma tabela chamada `usuarios` dentro do banco de dados PostgreSQL. Cada usuário possui uma coluna `tenant_id` para identificar a que cliente ele pertence.

## Configuração

Para executar a aplicação, siga estas etapas:

1. Instale o Python e o PostgreSQL, se ainda não estiverem instalados.
2. Crie um ambiente virtual Python e instale as dependências:

`pip install Flask psycopg2`

3. Execute o script SQL fornecido (`script.sql`) para criar o banco de dados e a tabela necessários.
4. Execute o arquivo Python (`app.py`) para iniciar o servidor Flask.
5. Acesse a aplicação em seu navegador web através do URL `http://localhost:5000`.

