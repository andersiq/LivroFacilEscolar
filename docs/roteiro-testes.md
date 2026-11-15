# Roteiro de Testes — LivroFácil Escolar

## 1. Objetivo
Verificar se as principais funcionalidades do sistema funcionam corretamente e facilitam o gerenciamento dos livros da biblioteca escolar.

## 2. Ambiente de teste
- Sistema: LivroFácil Escolar
- Linguagem: Python
- Framework: Flask
- Banco de dados: SQLite
- Navegador: Google Chrome
- Dados utilizados: fictícios.

## 3. Testes funcionais

### Teste 1 — Cadastro de livros
1. Acessar a tela inicial.
2. Selecionar a opção "Cadastrar livro".
3. Informar título, autor, quantidade de exemplares e números TOMBO.
4. Confirmar o cadastro.

**Resultado esperado:** o sistema deve cadastrar o livro e seus exemplares, exibindo uma mensagem de sucesso.

### Teste 2 — Consulta de livros
1. Acessar a opção "Consultar livros".
2. Verificar os livros cadastrados.
3. Conferir título, autor, número TOMBO e situação de cada exemplar.

**Resultado esperado:** o sistema deve apresentar os exemplares e indicar se estão disponíveis ou emprestados.

### Teste 3 — Registro de empréstimo
1. Acessar a opção "Registrar empréstimo".
2. Informar o nome do aluno e o número TOMBO de um exemplar disponível.
3. Confirmar o empréstimo.

**Resultado esperado:** o sistema deve registrar o empréstimo e alterar a situação do exemplar para "Emprestado".

### Teste 4 — Registro de devolução
1. Acessar a opção "Registrar devolução".
2. Informar o número TOMBO de um exemplar emprestado.
3. Confirmar a devolução.

**Resultado esperado:** o sistema deve registrar a devolução e alterar a situação do exemplar para "Disponível".

## 4. Critérios de aprovação
Os testes serão considerados aprovados quando cada funcionalidade executar corretamente, apresentar as mensagens esperadas e manter as informações atualizadas no banco de dados.

## 5. Observações
Os testes devem utilizar dados fictícios. Erros encontrados, dificuldades de navegação e sugestões de melhoria devem ser registrados para orientar futuras atualizações do sistema.