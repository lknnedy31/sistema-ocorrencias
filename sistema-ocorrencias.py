import sqlite3


def criar_banco():
    conexao = sqlite3.connect("ocorrencias.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ocorrencias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_ocorrencia TEXT NOT NULL,
            descricao TEXT,
            data_ocorrencia TEXT NOT NULL,
            local TEXT,
            status TEXT DEFAULT 'aberta',
            prioridade TEXT DEFAULT 'media'
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_ocorrencia():
    tipo = input("Tipo de ocorrência: ")
    descricao = input("Descrição: ")
    data = input("Data da ocorrência (AAAA-MM-DD): ")
    local = input("Local: ")
    prioridade = input("Prioridade (baixa/media/alta/urgente): ")

    conexao = sqlite3.connect("ocorrencias.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO ocorrencias (tipo_ocorrencia, descricao, data_ocorrencia, local, prioridade)
        VALUES (?, ?, ?, ?, ?)
    """, (tipo, descricao, data, local, prioridade))

    conexao.commit()
    conexao.close()
    print("Ocorrência cadastrada com sucesso!\n")


criar_banco()
cadastrar_ocorrencia()
