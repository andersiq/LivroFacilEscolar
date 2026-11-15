
from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Criar o banco de dados
def criar_banco():
    conexao = sqlite3.connect("banco.db")

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            quantidade_total INTEGER NOT NULL,
            quantidade_disponivel INTEGER NOT NULL
        )
    """)

    
    # Criar tabela de exemplares
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS exemplares (
            id_exemplar INTEGER PRIMARY KEY AUTOINCREMENT,
            id_livro INTEGER NOT NULL,
            tombo TEXT NOT NULL UNIQUE,
            status TEXT NOT NULL DEFAULT 'Disponível',
            FOREIGN KEY (id_livro) REFERENCES livros(id_livro),
            CHECK (
                length(tombo) = 4
                AND tombo NOT GLOB '*[^0-9]*'
            )
        )
    """)

    # Criar tabela de empréstimos
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS emprestimos (
            id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
            id_exemplar INTEGER NOT NULL,
            nome_aluno TEXT NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao TEXT,
            status TEXT NOT NULL DEFAULT 'Emprestado',
            FOREIGN KEY (id_exemplar) REFERENCES exemplares(id_exemplar)
        )
    """)

    conexao.commit()
    conexao.close()


# Página inicial
@app.route("/")
def inicio():
    return render_template("index.html")


# Cadastro de livros

@app.route("/livros/cadastrar", methods=["GET", "POST"])
def cadastrar_livro():

    mensagem = ""

    if request.method == "POST":

        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()

        try:
            quantidade = int(request.form["quantidade"])
        except ValueError:
            quantidade = 0

        tombos = [
            item.strip()
            for item in request.form["tombos"].split(",")
        ]

        if (
            not titulo
            or not autor
            or quantidade <= 0
            or len(tombos) != quantidade
            or any(
                len(tombo) != 4 or not tombo.isdigit()
                for tombo in tombos
            )
            or len(set(tombos)) != len(tombos)
        ):
            mensagem = "Confira os dados e informe um TOMBO de 4 números para cada exemplar."

        else:
            conexao = sqlite3.connect("banco.db")

            try:
                cursor = conexao.execute("""
                    INSERT INTO livros
                    (titulo, autor, quantidade_total, quantidade_disponivel)
                    VALUES (?, ?, ?, ?)
                """, (titulo, autor, quantidade, quantidade))

                id_livro = cursor.lastrowid

                for tombo in tombos:
                    conexao.execute("""
                        INSERT INTO exemplares
                        (id_livro, tombo)
                        VALUES (?, ?)
                    """, (id_livro, tombo))

                conexao.commit()
                mensagem = "Livro e exemplares cadastrados com sucesso!"
                

            except sqlite3.IntegrityError:
                conexao.rollback()
                mensagem = "Um ou mais números TOMBO já estão cadastrados."

            finally:
                conexao.close()

    return render_template(
        "cadastrar_livro.html",
        mensagem=mensagem
    )

# Consultar livros cadastrados
@app.route("/livros")
def consultar_livros():
    conexao = sqlite3.connect("banco.db")
    conexao.row_factory = sqlite3.Row

    exemplares = conexao.execute("""
        SELECT
            livros.id_livro,
            livros.titulo,
            livros.autor,
            exemplares.id_exemplar,
            exemplares.tombo,
            exemplares.status,
            (
                SELECT COUNT(*)
                FROM exemplares AS e
                WHERE e.id_livro = livros.id_livro
                AND e.status = 'Disponível'
            ) AS quantidade_disponivel
        FROM exemplares
        INNER JOIN livros
            ON livros.id_livro = exemplares.id_livro
        ORDER BY livros.titulo, exemplares.tombo
    """).fetchall()

    conexao.close()

    return render_template(
        "livros.html",
        exemplares=exemplares
    )


# Registrar empréstimo
@app.route("/emprestimo", methods=["GET", "POST"])
def registrar_emprestimo():

    mensagem = ""

    if request.method == "POST":

        nome_aluno = request.form["nome_aluno"].strip()
        tombo = request.form["tombo"].strip()

        conexao = sqlite3.connect("banco.db")

        try:
            exemplar = conexao.execute("""
                SELECT id_exemplar, status
                FROM exemplares
                WHERE tombo = ?
            """, (tombo,)).fetchone()

            if not nome_aluno or not tombo:
                mensagem = "Preencha todos os campos."

            elif exemplar is None:
                mensagem = "TOMBO não encontrado."

            elif exemplar[1] != "Disponível":
                mensagem = "Este exemplar já está emprestado."

            else:
                data_emprestimo = datetime.now().strftime("%d/%m/%Y")

                conexao.execute("""
                    INSERT INTO emprestimos
                    (id_exemplar, nome_aluno, data_emprestimo)
                    VALUES (?, ?, ?)
                """, (exemplar[0], nome_aluno, data_emprestimo))

                conexao.execute("""
                    UPDATE exemplares
                    SET status = 'Emprestado'
                    WHERE id_exemplar = ?
                """, (exemplar[0],))

                conexao.commit()

                mensagem = "Empréstimo registrado com sucesso!"

        except sqlite3.Error:
            conexao.rollback()
            mensagem = "Erro ao registrar o empréstimo."

        finally:
            conexao.close()

    return render_template(
        "emprestimo.html",
        mensagem=mensagem
    )


# Registrar devolução
@app.route("/devolucao", methods=["GET", "POST"])
def registrar_devolucao():

    mensagem = ""

    if request.method == "POST":

        tombo = request.form["tombo"].strip()

        conexao = sqlite3.connect("banco.db")

        try:
            exemplar = conexao.execute("""
                SELECT id_exemplar, status
                FROM exemplares
                WHERE tombo = ?
            """, (tombo,)).fetchone()

            if exemplar is None:
                mensagem = "TOMBO não encontrado."

            elif exemplar[1] == "Disponível":
                mensagem = "Este exemplar já está disponível."

            else:
                data_devolucao = datetime.now().strftime("%d/%m/%Y")

                conexao.execute("""
                    UPDATE emprestimos
                    SET data_devolucao = ?, status = 'Devolvido'
                    WHERE id_exemplar = ?
                    AND status = 'Emprestado'
                """, (data_devolucao, exemplar[0]))

                conexao.execute("""
                    UPDATE exemplares
                    SET status = 'Disponível'
                    WHERE id_exemplar = ?
                """, (exemplar[0],))

                conexao.commit()

                mensagem = "Devolução registrada com sucesso!"

        except sqlite3.Error:
            conexao.rollback()
            mensagem = "Erro ao registrar a devolução."

        finally:
            conexao.close()

    return render_template(
        "devolucao.html",
        mensagem=mensagem
    )


# Excluir livro e seus exemplares
@app.route("/livros/excluir/<int:id_livro>", methods=["POST"])
def excluir_livro(id_livro):

    conexao = sqlite3.connect("banco.db")

    try:
        # Excluir primeiro os exemplares
        conexao.execute(
            "DELETE FROM exemplares WHERE id_livro = ?",
            (id_livro,)
        )

        # Depois excluir o livro
        conexao.execute(
            "DELETE FROM livros WHERE id_livro = ?",
            (id_livro,)
        )

        conexao.commit()

    except sqlite3.Error:
        conexao.rollback()
        return "Erro ao excluir o livro.", 500

    finally:
        conexao.close()

    return redirect("/livros")


if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)