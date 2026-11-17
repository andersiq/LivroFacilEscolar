# 📚 LivroFácil Escolar

Sistema web desenvolvido para auxiliar na organização e no gerenciamento de bibliotecas escolares, facilitando o cadastro de livros, controle de exemplares, empréstimos e devoluções.

## 🎯 Objetivo do projeto

O LivroFácil Escolar surgiu da necessidade de substituir controles manuais realizados em papel por uma solução digital simples e prática, facilitando o trabalho do agente escolar responsável pela biblioteca.

O projeto foi desenvolvido como parte de uma atividade acadêmica do curso de Análise e Desenvolvimento de Sistemas (ADS).

## 🚀 Funcionalidades

- Cadastro de livros e autores.
- Cadastro de exemplares com número de TOMBO individual.
- Consulta de livros cadastrados.
- Visualização da disponibilidade dos exemplares.
- Registro de empréstimos para alunos.
- Registro de devoluções.
- Controle de status dos exemplares.

## 🛠️ Tecnologias utilizadas

- **Python 3.12** — linguagem de programação.
- **Flask** — framework para desenvolvimento web.
- **SQLite** — banco de dados.
- **HTML5** — estrutura das páginas.
- **CSS3** — estilização da interface.

## 📂 Estrutura do projeto

```text
LivroFacilEscolar/
│
├── app.py
├── banco.db
├── templates/
│   ├── index.html
│   ├── cadastrar_livro.html
│   ├── livros.html
│   ├── emprestimo.html
│   └── devolucao.html
│
├── .gitignore
└── README.md
```

## ⚙️ Como executar o projeto

**1. Clone o repositório:**

```bash
git clone https://github.com/andersiq/LivroFacilEscolar.git
```

**2. Entre na pasta:**

```bash
cd LivroFacilEscolar
```

**3. Crie um ambiente virtual:**

```bash
python -m venv .venv
```

**4. Ative o ambiente virtual no Windows:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**5. Instale o Flask:**

```bash
pip install Flask
```

**6. Execute o sistema:**

```bash
python app.py
```

**7. Acesse pelo navegador:**

http://127.0.0.1:5000

## 🏗️ Arquitetura

O projeto utiliza uma estrutura monolítica em camadas, com organização baseada no padrão MVC (Model-View-Controller).

## 📌 Status do projeto

MVP desenvolvido para fins acadêmicos, com

## Documentação do projeto

O projeto possui documentos complementares:

- [Roteiro de testes](docs/roteiro-testes.md)
- [Estrutura e arquitetura do projeto](docs/estrutura-projeto.md)

Esses documentos apresentam os procedimentos de validação do sistema e explicam a organização dos arquivos e a arquitetura utilizada.