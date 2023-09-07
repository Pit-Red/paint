import sqlite3

def create_database():
    conn = sqlite3.connect('paint.db')
    conn.close()

def create_table():
    conn = sqlite3.connect('paint.db')

    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS draw')
    query = """
    CREATE TABLE draw(
    id INTEGER AUTOINCREMENT,
    title TEXT UNIQUE NOT NULL,
    description TEXT,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (title,data_creazione)
    )
    """
    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

def insert_draw(title,descrizione=''):
    if not contain_title(title):
        conn =sqlite3.connect('paint.db')

        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO draw(title,description) VALUES (?,?)',(title,descrizione))

            conn.commit()
            cursor.close()
            conn.close()
        except sqlite3.Error as e:
            print(f'Errore durante l\'inserimento del nuovo disegno: {e}')

def contain_title(title):
    conn = sqlite3.connect('paint.db')
    risultato = ''

    try:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM draw WHERE title = ?',(title,))

        risultato = cursor.fetchone()
        cursor.close()
    except sqlite3.Error as e:
        print(f'Errore durante la ricerca del titolo: {e}')
    finally:
        conn.close()
        if risultato is not None:
            return True
        return False
    
def get_descriprion(title):
    conn = sqlite3.connect('paint.db')
    risultato = ''

    try:
        cursor = conn.cursor()

        cursor.execute('SELECT description FROM draw WHERE title = ?',(title,))

        risultato = cursor.fetchone()
        cursor.close()
    except sqlite3.Error as e:
        print(f'Errore durante la ricerca della descrizione: {e}')
    finally:
        conn.close()
        if risultato is not None:
            return risultato[0]
        
def get_creation_date(title):
    conn = sqlite3.connect('paint.db')
    risultato = ()
    try:
        cursor = conn.cursor()

        cursor.execute('SELECT creation_date FROM draw WHERE title = ?'(title,))

        risultato = cursor.fetchone()
        cursor.close()
    except sqlite3.Error as e:
        print(f'Errore durante la ricerca della data di creazione: {e}')
    finally:
        conn.close()
        if risultato is not None:
            return risultato[0]