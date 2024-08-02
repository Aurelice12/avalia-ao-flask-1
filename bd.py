import sqlite3

def tabela():
    conn = sqlite3.connect("bd")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(200) NOT NULL,
            atr_conjuracao VARCHAR(200) NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS armaduras (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(200) NOT NULL,
            defesa VARCHAR(200) NOT NULL,
            tipo VARCHAR(200) NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS armas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(200) NOT NULL,
            tipo VARCHAR(200) NOT NULL,
            propriedade VARCHAR(200) NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magias (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(200) NOT NULL,
            nivel REAL NOT NULL,
            alcance VARCHAR(200) NOT NULL
        );
    """)

    conn.close()

###########################################


def nova_classe(nome, atr_conjuracao):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()


    cursor.execute(f"""
      INSERT INTO classes(nome, atr_conjuracao)
      VALUES('{nome}', '{atr_conjuracao}');
  """)

    conn.commit()
    conn.close()


def listar_classe():
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    values = cursor.execute("SELECT * FROM classes")
    resultado = []
    for item in values.fetchall():
        resultado.append({
            'id': item[0],
            'nome': item[1],
            'atr_conjuracao': item[2],
        })
    print(resultado)
    conn.close()
    return resultado


def atualizar_classe(id, nome, atr_conjuracao):

    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    cursor.execute(f"""
      UPDATE classes
      SET nome='{nome}',
      atr_conjuracao = '{atr_conjuracao}',
      WHERE id={id}
  """)
    conn.commit()
    conn.close()


def remove_classe(id):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    cursor.execute(f"""
      DELETE FROM classe
      WHERE id={id}
  """)
    conn.commit()
    conn.close()


def detalha_classe(id):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    value = cursor.execute(f"""
            SELECT *
            FROM classes
            WHERE id={id}
        """)
    item = value.fetchone()
    conn.close()
    return {
        'id': item[0],
        'nome': item[1],
        'atr_conjuracao': item[2]}

#########################################


def nova_armadura(nome, defesa, tipo):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()

    cursor.execute(f"""
      INSERT INTO armaduras(nome, defesa, tipo)
      VALUES('{nome}', '{defesa}', '{tipo}');
  """)
    conn.commit()
    conn.close()


def listar_armadura():
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    values = cursor.execute("SELECT * FROM armaduras")
    resultado = []
    for item in values.fetchall():
        resultado.append({
            'id': item[0],
            'nome': item[1],
            'defesa': item[2],
            'tipo': item[3]
        })
    print(resultado)
    conn.close()
    return resultado


def atualizar_armadura(id, nome, defesa, tipo):


    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    cursor.execute(f"""
      UPDATE armaduras
      SET nome='{nome}',
      defesa = '{defesa}',
      tipo = '{tipo}'
      WHERE id={id}
  """)
    conn.commit()
    conn.close()


def remove_armadura(id):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    cursor.execute(f"""
      DELETE FROM armaduras
      WHERE id={id}
  """)
    conn.commit()
    conn.close()


def detalha_armadura(id):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    value = cursor.execute(f"""
            SELECT *
            FROM armaduras
            WHERE id={id}
        """)
    item = value.fetchone()
    conn.close()
    return {
        'id': item[0],
        'nome': item[1],
        'defesa': item[2],
        'tipo': item[3]}


######################################


def nova_arma(nome, propriedade, tipo):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()


    cursor.execute(f"""
      INSERT INTO armas(nome, propriedade, tipo)
      VALUES('{nome}', '{propriedade}', '{tipo}');
  """)
    conn.commit()
    conn.close()


def listar_arma():
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    values = cursor.execute("SELECT * FROM armas")
    resultado = []
    for item in values.fetchall():
        resultado.append({
            'id': item[0],
            'nome': item[1],
            'propriedade': item[2],
            'tipo': item[3]
        })
    print(resultado)
    conn.close()
    return resultado


def atualizar_arma(id, nome, propriedade, tipo):


    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    cursor.execute(f"""
      UPDATE armas
      SET nome='{nome}',
      propriedade = '{propriedade}',
      tipo = '{tipo}'
      WHERE id={id}
  """)
    conn.commit()
    conn.close()


def remove_arma(id):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    cursor.execute(f"""
      DELETE FROM armas
      WHERE id={id}
  """)
    conn.commit()
    conn.close()


def detalha_arma(id):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    value = cursor.execute(f"""
            SELECT *
            FROM armas
            WHERE id={id}
        """)
    item = value.fetchone()
    conn.close()
    return {
        'id': item[0],
        'nome': item[1],
        'propriedade': item[2],
        'tipo': item[3]}


##########################################


def nova_magia(nome, nivel, alcance):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()

    cursor.execute(f"""
      INSERT INTO magias(nome, nivel, alcance)
      VALUES('{nome}', '{nivel}', '{alcance}');
  """)
    conn.commit()
    conn.close()


def listar_magia():
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    values = cursor.execute("SELECT * FROM magias")
    resultado = []
    for item in values.fetchall():
        resultado.append({
            'id': item[0],
            'nome': item[1],
            'nivel': item[2],
            'alcance': item[3]
        })
    print(resultado)
    conn.close()
    return resultado


def atualizar_magia(id, nome, nivel, alcance):

    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    cursor.execute(f"""
      UPDATE magias
      SET nome='{nome}',
      nivel = '{nivel}',
      alcance = '{alcance}'
      WHERE id={id}
  """)
    conn.commit()
    conn.close()


def remove_magia(id):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    cursor.execute(f"""
      DELETE FROM magias
      WHERE id={id}
  """)
    conn.commit()
    conn.close()


def detalha_magia(id):
    conn = sqlite3.connect('bd')
    cursor = conn.cursor()
    value = cursor.execute(f"""
            SELECT *
            FROM magias
            WHERE id={id}
        """)
    item = value.fetchone()
    conn.close()
    return {
        'id': item[0],
        'nome': item[1],
        'nivel': item[2],
        'alcance': item[3]}


if __name__ == '__main__':
    tabela()
