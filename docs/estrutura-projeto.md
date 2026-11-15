# Estrutura do Projeto — LivroFácil Escolar

## 1. Organização dos arquivos

O projeto LivroFácil Escolar está organizado da seguinte forma:

```text
LivroFacil-Escolar/
│
├── app.py
├── banco.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── cadastrar_livro.html
│   ├── livros.html
│   ├── emprestimo.html
│   └── devolucao.html
│
└── docs/
    ├── roteiro-testes.md
    └── estrutura-projeto.md
```

## 2. Descrição dos principais arquivos

- **app.py:** arquivo principal da aplicação, responsável pelas rotas, regras de funcionamento e comunicação com o banco de dados.
- **banco.db:** banco de dados SQLite utilizado para armazenar livros, exemplares e empréstimos.
- **requirements.txt:** informa as dependências necessárias para executar o projeto.
- **templates/:** pasta que contém as páginas HTML apresentadas ao usuário.
- **docs/:** pasta destinada à documentação do projeto.

## 3. Arquitetura utilizada

O projeto utiliza uma arquitetura monolítica em camadas, seguindo conceitos do padrão MVC (Model-View-Controller).

- **Model:** representa os dados e as operações realizadas no banco de dados SQLite.
- **View:** corresponde às páginas HTML da pasta templates, responsáveis pela apresentação das informações.
- **Controller:** corresponde às rotas e ao processamento das solicitações no arquivo app.py.

## 4. Funcionamento geral

O usuário acessa o sistema pelo navegador e escolhe uma funcionalidade. O Flask recebe a solicitação, executa as operações necessárias no banco de dados e apresenta o resultado na página correspondente.

Essa organização facilita a compreensão do código e permite futuras melhorias no sistema.