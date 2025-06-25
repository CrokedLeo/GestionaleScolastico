import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database_name):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()
        self.database_name = database_name
        self.init_database()

    def init_database(self):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database_name}")
        self.conn.database = self.database_name
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS studenti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                italiano FLOAT,
                matematica FLOAT
            )
        """)
# ma mettere anche media che si calcola con i voti inseriti, media iniziale a 0
    def inserisci_studente(self, nome, italiano, matematica):
        self.cursor.execute("""
            INSERT INTO studenti (nome, italiano, matematica)
            VALUES (%s, %s, %s)
        """, (nome, italiano, matematica))
        self.conn.commit()

    def visualizza_studenti(self):
        self.cursor.execute("SELECT id, nome, italiano, matematica FROM studenti")
        return self.cursor.fetchall()

    def modifica_studente(self, id_studente, nuovo_nome, nuovo_italiano, nuovo_matematica):
        self.cursor.execute("""
            UPDATE studenti
            SET nome = %s, italiano = %s, matematica = %s
            WHERE id = %s
        """, (nuovo_nome, nuovo_italiano, nuovo_matematica, id_studente))
        self.conn.commit()

    def elimina_studente(self, id_studente):
        self.cursor.execute("DELETE FROM studenti WHERE id = %s", (id_studente,))
        self.conn.commit()

    def chiudi_connessione(self):
        self.cursor.close()
        self.conn.close()

