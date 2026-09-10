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


def listar_ocorrencias ():
    conexao = sqlite3.connect("ocorrencias.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM ocorrencias")
    resultados = cursor.fetchall()

    conexao.close()

    if not resultados:
        print("Nenhuma ocorrência cadastrada ainda.\n")
        return

    for linha in resultados:
        print(f"ID: {linha[0]}")
        print(f"Tipo: {linha[1]}")
        print(f"Descrição: {linha[2]}")
        print(f"Data: {linha[3]}")
        print(f"Local: {linha[4]}")
        print(f"Status: {linha[5]}")
        print(f"Prioridade: {linha[6]}")
        print("-" * 30)


def atualizar_ocorrencia(): 
    listar_ocorrencias()
    id_ocorrencia = input("Digite o ID da ocorrência que deseja atualizar: ")

    novo_status = input("Novo status (aberta/em andamento/encerrada): ")
    nova_prioridade = input("Nova prioridade (baixa/media/alta/urgente): ")

    conexao = sqlite3.connect("ocorrencias.db")
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE ocorrencias
        SET status = ?, prioridade = ?
        WHERE id = ?
    """,    (novo_status, nova_prioridade, id_ocorrencia))

    conexao.commit()

    if cursor.rowcount == 0:
        print("Nenhuma ocorrência encontrada com esse ID.\n")
    else:
        print("Ocorrência atualizada com sucesso!\n")

    conexao.close()

criar_banco()
atualizar_ocorrencia()
 