from database_manager import DatabaseManager
from gestionale import GestionaleScolastico

if __name__ == "__main__":
    db = DatabaseManager(
        host="localhost",
        user="root",
        password="",
        database_name="scuolaDB"
    )
    app = GestionaleScolastico(db)
    app.avvia()
