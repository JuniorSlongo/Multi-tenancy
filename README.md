# Sistema Multi-Tenancy

Este é um exemplo simples de um sistema multi-tenant usando Node.js e MongoDB.

## Estratégia de Multi-Tenancy

A estratégia de multi-tenancy usada é a "Banco de Dados Separado". Cada inquilino tem seu próprio banco de dados MongoDB. O nome do inquilino é passado através do cabeçalho HTTP `x-tenant-name`. Com base nesse cabeçalho, uma conexão com o banco de dados correspondente é estabelecida e o modelo `Task` é criado para esse inquilino.

## Como usar

1. Clone este repositório para sua máquina local.
2. Instale as dependências com `npm install`.
3. Inicie o servidor com `node server.js`.
4. Abra o arquivo `index.html` em seu navegador.
5. Insira o nome do inquilino e clique em "Carregar Tarefas" para ver as tarefas para esse inquilino.

## API REST

O servidor fornece uma API REST simples que retorna tarefas para um inquilino específico. A rota é `GET /tasks` e o nome do inquilino deve ser passado no cabeçalho `x-tenant-name`.

