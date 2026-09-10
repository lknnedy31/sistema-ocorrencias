# Sistema de Gerenciamento de Ocorrências

Sistema de linha de comando (CLI) em Python para cadastro e controle de ocorrências, desenvolvido como projeto de estudo aplicando lógica de programação e banco de dados relacional com operações CRUD completas.

##  Demonstração

<!-- Adicione aqui um print da tela do sistema rodando no terminal, ou um GIF curto mostrando o cadastro e a listagem de uma ocorrência -->
<!-- Exemplo: ![demo](./assets/demo.gif) -->

##  Funcionalidades

- Cadastrar nova ocorrência (tipo, descrição, data, local e prioridade)
- Listar todas as ocorrências cadastradas
- Atualizar dados de uma ocorrência existente
- Excluir uma ocorrência pelo ID

##  Tecnologias utilizadas

- **Python 3** — lógica do sistema
- **SQLite** — banco de dados local, embutido no Python (módulo `sqlite3`)

> **Sobre o banco de dados:** o projeto utiliza SQLite por não exigir instalação nem configuração de servidor, facilitando testar e rodar em qualquer máquina. Todos os comandos SQL (`CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`) seguem a sintaxe padrão de SQL, com pequenas adaptações específicas do SQLite (como `AUTOINCREMENT` no lugar de `AUTO_INCREMENT`). A lógica das consultas é a mesma utilizada em bancos como MySQL ou PostgreSQL, exigindo apenas ajustes pontuais de sintaxe para migração.

##  Competências praticadas

- Manipulação de dados via linha de comando (CLI)
- Implementação de operações CRUD completas (Create, Read, Update, Delete)
- Integração entre Python e banco de dados relacional (SQLite)
- Uso de queries parametrizadas para prevenir SQL Injection
- Modelagem básica de tabela relacional
- Versionamento de código com Git e GitHub

##  Como rodar o projeto

Clone o repositório:
```
git clone git@github.com:lknnedy31/sistema-ocorrencias.git
```

Entre na pasta do projeto:
```
cd sistema-ocorrencias
```

Execute o arquivo principal:
```
python sistema-ocorrencias.py
```

Não é necessário instalar nenhuma dependência externa — o SQLite já vem incluso no Python.

##  Estrutura do banco de dados

Tabela `ocorrencias`:

| Campo             | Tipo    | Descrição                                    |
|-------------------|---------|-----------------------------------------------|
| id                | INTEGER | Identificador único (gerado automaticamente)  |
| tipo_ocorrencia   | TEXT    | Tipo da ocorrência (ex: furto, acidente)      |
| descricao         | TEXT    | Detalhamento da ocorrência                    |
| data_ocorrencia   | TEXT    | Data em que o fato ocorreu (AAAA-MM-DD)       |
| local             | TEXT    | Local onde ocorreu                            |
| status            | TEXT    | Situação atual (padrão: "aberta")             |
| prioridade        | TEXT    | Nível de urgência (padrão: "media")           |

##  Possíveis melhorias futuras

- Adicionar campos de responsável e data de registro
- Migrar para MySQL/PostgreSQL em ambiente de produção
- Criar interface web com Flask
- Gerar relatórios e estatísticas das ocorrências cadastradas

##  Autor

**Kauã Kennedy Carneiro Araujo**
Estudante de Análise e Desenvolvimento de Sistemas (ADS) — UCSAL
