import database_manager

class GestionaleScolastico:
    def __init__(self, db_manager):
        self.db = db_manager

    def mostra_menu(self):
        print("""
<> Gestionale Scolastico <>
1. Inserisci studente
2. Visualizza studenti e medie
3. Modifica studente
4. Elimina studente
5. Esci
""")

    def avvia(self):
        while True:
            self.mostra_menu()
            scelta = input("Scelta: ")
            if scelta == "1":
                self.inserisci()
            elif scelta == "2":
                self.visualizza()
            elif scelta == "3":
                self.modifica()
            elif scelta == "4":
                self.elimina()
            elif scelta == "5":
                print("Uscita in corso...")
                self.db.chiudi_connessione()
                break
            else:
                print("Scelta non valida.")

# va messo controllo per verifica try/except nome=lettare e voti=numeri vuoto range 0-10
    def inserisci(self):
        nome = input("Nome studente: ")
        italiano = (input("Voto italiano: "))
        matematica = float(input("Voto matematica: "))
        self.db.inserisci_studente(nome, italiano, matematica)
        print("Studente inserito con successo!")
    

    def visualizza(self):
        studenti = self.db.visualizza_studenti()
        print("\nElenco studenti e medie:")

        for id_studente, nome, italiano, matematica in studenti:
# se fossero piu voti e materie si puo usare libreria per calcolare la media statistics?
            media = (italiano + matematica) / 2
            print(f"ID: {id_studente} | {nome} | italiano: {italiano} | matematica: {matematica} - Media: {media:.2f}")

    def modifica(self):
        self.visualizza()
        id_studente = input("ID dello studente da modificare: ")
        nuovo_nome = input("Nuovo nome: ")
        nuovo_italiano = float(input("Nuovo voto italiano: "))
        nuovo_matematica = float(input("Nuovo voto matematica: "))
        self.db.modifica_studente(id_studente, nuovo_nome, nuovo_italiano, nuovo_matematica)
        print("Studente modificato con successo!")

    def elimina(self):
        self.visualizza()
        id_studente = input("ID dello studente da eliminare: ")
        self.db.elimina_studente(id_studente)
        print("Studente eliminato con successo!")

    """def chiudi_connessione(self):
        self.db.chiudi_connessione()
        print("Connessione al database chiusa.")"""
