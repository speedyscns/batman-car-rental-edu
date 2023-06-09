import os
import sys
import platform
from datetime import *

# Ottenere il percorso completo di dove si trova questo file .py
percorsoQuestoFilePY = os.path.abspath(__file__)
#print(os.path.abspath(__file__))

# Ottenere il percorso completo della directory genitore di questo file .py
percorsoCartellaFilePY = os.path.dirname(percorsoQuestoFilePY)
    #print(os.path.dirname(percorsoQuestoFilePY))

# path dei CSV    
pathUtenti = os.path.join(percorsoCartellaFilePY, "utenti.csv")
pathAuto = os.path.join(percorsoCartellaFilePY, "auto.csv")
batmobile = False

#funzioni
def restituisciAuto(): # secondo l'ordine del CSV 
    auto = []  # dichiarazione della variabile auto
    print("""
        ----------------------
        LISTA AUTO NOLEGGIATE
        ----------------------
        ID - MODELLO
        ----------------------
        """)
          
    file = letturaCSV(Path=pathAuto) 
    
    # mostra solo auto con disponibilità False (id e nome)
        
    for riga in file:
        rigaSplit = riga.strip().split(":") # riga divisa in due elementi
        auto.append(rigaSplit[0].strip())  # IMPORTANTE! Aggiungi l'indice dell'auto alla lista auto
        
        if rigaSplit[3].strip() == "False":  # Visualizza auto SOLO se è tra quelle da restituire

            #if mostraAncheBatmobile(rigaSplit) and batmobile: # condizione mostra auto / mostra auto + batmobile se batmobile = True
            if mostraAncheBatmobile(rigaSplit) and batmobile: # condizione mostra auto / mostra auto + batmobile se batmobile = True
                print("        ", rigaSplit[0], rigaSplit[1]) # mostra solo ID e NOME
            
            #elif nascondiBatmobile(rigaSplit): # condizione mostra auto / mostra auto + batmobile
            elif nascondiBatmobile(rigaSplit): # condizione mostra auto / mostra auto + batmobile
                print("        ", rigaSplit[0], rigaSplit[1]) # Mostra solo ID e NOME
                
            # MOSTRA SE LE RIGHE SPLITTATE SONO < 1 DI UNO (QUINDI NON CI SONO DELLE AUTO NEL CSV)        
            elif len(rigaSplit) < 1:
                print("""
        ----------------------------
        Non ci sono auto disponibili
        ----------------------------
                    """)
            
    IDrestituzione = input("""
        -------------------------------------------------            
        Inserisci l'indice dell'auto che stai restituendo
        -------------------------------------------------
        
        >>> """)
    
    # logica per riportare a True l'auto con l'indice da input restituzione
    # LETTURA TUTTA LE LINEE e verifica se selezioneNoleggio è presente tra gli indici delle auto
    if IDrestituzione in auto and len(auto) > 0:
        file = open(pathAuto, "r")
        linee = file.readlines()
        file.close()

        file = open(pathAuto, "w")
        # variabili vuote create prima del ciclo for riempite solo in caso di else ovvero 
        idAutoDaRestituire = ""
        nomeAutoDaRestituire = ""
        prezzoAutoDaRestituire = ""
        disponibilitaRestituita = "True"

        for riga in linee:
            rigaSplit = riga.strip().split(":")

            # IMPORTANTE: IF DENTRO CICLO FOR PER OGNI RIGA!
            if rigaSplit[0] != IDrestituzione:  # esclude la riga contenente l'indice cercato
                file.write(f"{riga}")  # scrive file temp senza la riga dell'indice cercato (niente \n o incasina con il salta riga)
                
            else: # ovvero la corrispondenza con l'indice inserito da input
                if len(rigaSplit) > 1:
                    idAutoDaRestituire = rigaSplit[0]
                    nomeAutoDaRestituire = rigaSplit[1]
                    prezzoAutoDaRestituire = rigaSplit[2]
                    disponibilitaRestituita = "True"
                    file.write(f"{idAutoDaRestituire}:{nomeAutoDaRestituire}:{prezzoAutoDaRestituire}:{disponibilitaRestituita}\n")
                    
        if nomeAutoDaRestituire is not None:
            print(f"""
        ----------------------------------
        Procedura restituzione per auto:
        {nomeAutoDaRestituire} completata
        ----------------------------------
            """)

        
    else:
        print("""
        ---------------------------
        Indice inserito non valido
        ---------------------------
            """)
    file.close()

def noleggiaAuto():    
    auto = []  # dichiarazione della variabile auto
    
    file = letturaCSV(Path=pathAuto)
    
    for riga in file:
        rigaSplit = riga.strip().split(":") # riga divisa in due elementi
        
        # ho eliminato la stamp perché la lista sarebbe ridondante
        if mostraAncheBatmobile(rigaSplit) and batmobile: # condizione mostra auto / mostra auto + batmobile se batmobile = True
            auto.append(rigaSplit[0].strip())
        
        elif nascondiBatmobile(rigaSplit): # condizione mostra auto / mostra auto + batmobile
            auto.append(rigaSplit[0].strip()) 
          
    # MOSTRA SE LE RIGHE SPLITTATE SONO < 1 DI UNO (QUINDI NON CI SONO DELLE AUTO NEL CSV)        
    if len(auto) < 1:
        print("""
        ----------------------------
        Non ci sono auto disponibili
        ----------------------------
        """)
        
    selezioneID_Noleggio = input("""
        --------------------------------------
        Inserisci l'ID dell'auto da noleggiare
        --------------------------------------
                
        >>> """)

    # ALTRI COMMENTI SU FUNZIONE restituisciAuto()
    # LETTURA TUTTA LE LINEE e verifica se selezioneNoleggio è presente tra gli indici delle auto
    if selezioneID_Noleggio in auto and len(auto) > 0:
        file = open(pathAuto, "r")
        linee = file.readlines()
        file.close()

        file = open(pathAuto, "w")
        # variabili vuote create prima del ciclo for riempite solo in caso di else ovvero 
        idAutoDaNoleggiare = ""
        nomeAutoDaNoleggiare = ""
        prezzoAutoDaNoleggiare = ""
        disponibilitaNoleggiare = "False"

        for riga in linee:
            rigaSplit = riga.strip().split(":")

            # IMPORTANTE: IF DENTRO CICLO FOR PER OGNI RIGA!
            if rigaSplit[0] != selezioneID_Noleggio:  # esclude la riga contenente l'indice cercato
                file.write(f"{riga}")  # scrive file temp senza la riga dell'indice cercato (niente \n o incasina con il salta riga)
                
            else: # ovvero la corrispondenza con l'indice inserito da input
                if len(rigaSplit) > 1:
                    idAutoDaNoleggiare = rigaSplit[0]
                    nomeAutoDaNoleggiare = rigaSplit[1]
                    prezzoAutoDaNoleggiare = rigaSplit[2]
                    disponibilitaNoleggiare = "False"
                    file.write(f"{idAutoDaNoleggiare}:{nomeAutoDaNoleggiare}:{prezzoAutoDaNoleggiare}:{disponibilitaNoleggiare}\n")
                    
        if nomeAutoDaNoleggiare is not None:
            print(f"""
        ----------------------------------
        Procedura noleggio per auto:
        {nomeAutoDaNoleggiare} completata
        ----------------------------------
            """)

        file.close()
    else:
        print("""
        ---------------------------
        Indice inserito non valido
        ---------------------------
            """)
    file.close() 

def letturaCSV(Path):
    try:
        file = open(Path, "r")  # Lettura CSV
        return file
    except FileNotFoundError:
        print("""
        --------------------
        Il file non trovato!
        --------------------
              """)

def rimozioneAuto(): # da eliminare doppione print
    
    print("""
        --------------------------------------------
              AUTO DISPONIBILI PER IL NOLEGGIO
        --------------------------------------------
        ID - MODELLO  - COSTO/Giorno -  DISPONIBILE?
        --------------------------------------------
        """)
    
    file = letturaCSV(Path=pathAuto)

    auto = []      
    for riga in file:
        rigaSplit = riga.strip().split(":") # riga divisa in due elementi
        auto.append(rigaSplit[0].strip()) 
        if mostraAncheBatmobile(rigaSplit) and batmobile: # condizione mostra auto / mostra auto + batmobile se batmobile = True
            print("        ", riga) 
        elif nascondiBatmobile(rigaSplit): # condizione mostra auto / mostra auto + batmobile
            print("        ", riga) 
        elif len(rigaSplit) < 1:  # MOSTRA SE LE RIGHE SPLITTATE SONO < 1 DI UNO (QUINDI NON CI SONO DELLE AUTO NEL CSV)        
            print("""
        ----------------------------
        Non ci sono auto disponibili
        ----------------------------
                """)          
                            
    selezioneRimozione = input("""
        -------------------------------------
        Inserisci l'ID dell'auto da rimuovere
        -------------------------------------
                
        >>> """)
    
    # LETTURA TUTTA LE LINEE e verifica se selezioneRimozione è presente tra gli indici delle auto                                     
    if selezioneRimozione in auto and len(auto) > 0:
        file = open(pathAuto, "r")
        linee = file.readlines()
        file.close()
        
        file = open(pathAuto, "w")
        nomeAutoDaRimuovere = ""
    
        for riga in linee:
            rigaSplit = riga.strip().split(":")

            # IMPORTANTE: IF DENTRO CICLO FOR PER OGNI RIGA!
            if rigaSplit[0] != selezioneRimozione: # (RI)SCRIVE TUTTE LE LINEE TRANNE QUELLE CHE HANNO INDICE[0] == selezioneRimozione
                file.write(riga)
    
            else:
                if len(rigaSplit) > 1: # CONTROLLO PER EVITARE CRASH CON INDICE NON PRESENTE
                    nomeAutoDaRimuovere = rigaSplit[1]
            
        if nomeAutoDaRimuovere:
            print(f"""
            Rimossa auto: {nomeAutoDaRimuovere}
            """)
            
        file.close()
                         
    else:
        print("""
        ---------------------------
        Indice inserito non valido
        ---------------------------
            """) 

def modificaPrezzoAuto():
    IDAutoPrezzoDaModificareo = input("""
        --------------------------------------------                       
            Procedura modifica prezzo/giorno auto...
        --------------------------------------------                           
        
        
        Inserisci l'ID dell'auto cui modificare il prezzo
        
        >>> """)
    
    os.system("cls")
    
    file = letturaCSV(Path=pathAuto)

    auto = []
    for riga in file:
        rigaSplit = riga.strip().split(":")
        auto.append(rigaSplit[0].strip())   
    file.close()
    
    
    
    # LETTURA TUTTA LE LINEE e verifica se l'ID auto da modificare è presente tra gli indici delle auto                                     
    if IDAutoPrezzoDaModificareo in auto and len(auto) > 0:
        file = open(pathAuto, "r")
        linee = file.readlines()
        file.close()
        
        file = open(pathAuto, "w")
        nomeAutoDaModificare = ""
        
        # input da inserire dentro la IF successiva accertato che ID auto da modificare è presente
        NuovoPrezzoAuto = input(""" 
                                
        -----------------------------------------------------------
        Ora, inserisci il nuovo prezzo/giorno dell'auto selezionata
        -----------------------------------------------------------
        
        >>> """)
    
        for riga in linee:
            rigaSplit = riga.strip().split(":")

            # IMPORTANTE: IF DENTRO CICLO FOR PER OGNI RIGA!
            if rigaSplit[0] != IDAutoPrezzoDaModificareo: # (RI)SCRIVE TUTTE LE LINEE TRANNE QUELLE CHE HANNO INDICE[0] == selezioneRimozione
                file.write(riga)
    
            else:
                if len(rigaSplit) > 1: # CONTROLLO PER EVITARE CRASH CON INDICE NON PRESENTE
                    IDAutoPrezzoDaModificareo = int(rigaSplit[0])
                    nomeAutoDaModificare = rigaSplit[1]
                    disponibilita = "True"
                    file.write(f"{IDAutoPrezzoDaModificareo}:{nomeAutoDaModificare}:{NuovoPrezzoAuto}:{disponibilita}")
    
            
        if nomeAutoDaModificare:
            print(f"""
        ------------------------------------------          
        {NuovoPrezzoAuto} è il nuovo prezzo/giorno
        per l'Auto: {nomeAutoDaModificare}
        -------------------------------------------
        
            """)
            
        file.close()
                         
    else:
        print("""
        ---------------------------
        Indice inserito non valido
        ---------------------------
            """)
    
def inserimentoAuto():
    os.system("cls")
    inserimentoNomeAuto = input("""
                                        
            Procedura di inserimento nuova auto...                            
                                        
        Inserisci il nome della nuova auto noleggiabile
        
        >>> """)
    
            
    file = letturaCSV(Path=pathAuto)

    auto = []
    for riga in file:
        rigaSplit = riga.strip().split(":")
        auto.append(rigaSplit[0].strip())   
    file.close()
    
    if inserimentoNomeAuto in auto:
        print(f"""
        ----------------------------------------------------
        {inserimentoNomeAuto} è già presente per il noleggio
        ----------------------------------------------------
            """)
    else: # INSERIMENTO (semi-automatico) INDICE USANDO COME RIFERIMENTO ULTIMO INDICE
        
        
        
        if len(auto) > 0: # Se la lunghezza stringhe > 0
            ultimaRiga = auto[-1].split(":") # LEGGE L'indice dell'ultima riga
            ultimoNumeroIndice = int(ultimaRiga[0]) #Convertire stringa con intero
            inserimentoPrezzoAuto = input(f"""
        -----------------------------------------------------------------
        Inserisci il prezzo/giorno a noleggio della {inserimentoNomeAuto}
        -----------------------------------------------------------------
        
        >>> """)

        else:
            ultimoNumeroIndice = 1
        
        nuovoIndice = ultimoNumeroIndice + 1
        
        # Aggiungi il nuovo utente al file CSV
        file = open(pathAuto, "a")
        file.write(f"{nuovoIndice}:{inserimentoNomeAuto}:{inserimentoPrezzoAuto}:True\n")
        print(f"""
        -------------------------------
        {inserimentoNomeAuto} inserita!
        -------------------------------
                """)
        
def adminON(login):
    while True:           
        scelta = input(f"""
        --------------------------------------------------               
        {login}, puoi eseguiure le seguenti operazioni:
        -------------------------------------------------- 
        1. Inserire una nuova auto disponibile al noleggio
        2. Modificare il prezzo del noleggio
        3. Eliminare un'auto
        0. Torna indietro
        
        >>> """)
        if scelta == "1":
            inserimentoAuto()
        elif scelta == "2":
            modificaPrezzoAuto()
                 
        elif scelta == "3":
            rimozioneAuto()
        
        elif scelta == "0":
            break
            
        else:
            print("""
        --------------------
        Selezione non valida
        --------------------
            """)
 
def menuUtente():
    while True:
        selezione = input("""
        --------------------------------
        OPERAZIONI Noleggio disponibili:
        --------------------------------
        
        1. Noleggia un auto
        2. Restituisci un'auto
        0. Torna indietro
        
        >>> """)
        
        if selezione == "1":
            noleggiaAuto()
        elif selezione == "2":
            restituisciAuto()
        elif selezione == "0":
            break
        
        else:
            print("""
        --------------------
        Selezione non valida
        --------------------
        """) 
                 
def menuAccount(login):
    

    if login == "admin":
        adminON(login)
        
    elif login == "Bruce Wayne":
        menuUtente()
        
    else:
        menuUtente()
                   
def nascondiBatmobile(rigaSplit):
    return len(rigaSplit) > 1 and rigaSplit[1] != "Batmobile" # se è ci sono righe nel CSV e la riga modello corrisponde a "Batmobile
    # MOSTRA SE LE RIGHE SPLITTATE SONO > 1 DI UNO (QUINDI CI SONO DELLE AUTO NEL CSV)
    # E L'ELEMENTO CON INDICE 1 DELLA TUPLA E' DIVERSO DA "Batmobile"
    # SE L'ELEMENTO è == ALLORA MOSTRERA' SOLO LA Batmobile

def mostraAncheBatmobile(rigaSplit):
    return len(rigaSplit) > 1 
    # MOSTRA SE LE RIGHE SPLITTATE SONO > 1 DI UNO (QUINDI CI SONO DELLE AUTO NEL CSV)

def ordinamentoAutoPerNome(auto):
        autoOrdinata = sorted(auto, key=lambda singolaAuto: singolaAuto[1])
        return autoOrdinata

def ordinamentoAutoperPrezzoCrescente(auto):
    autoOrdinata = sorted(auto, key=lambda singolaAuto: int(singolaAuto[2]))
    return autoOrdinata

def ordinamentoAutoperPrezzoDecrescente(auto):
    autoOrdinata = sorted(auto, key=lambda singolaAuto: int(singolaAuto[2]), reverse=True) #oppure ) * -1
    return autoOrdinata

def ordinamentoAuto(tipoOrdinamento):
    os.system("cls")

    auto = []
    print("""
        ---------------------------------------
            AUTO DISPONIBILI PER IL NOLEGGIO
        ---------------------------------------
        ID - MODELLO  -  COSTO  -  DISPONIBILE?
        ---------------------------------------
        """)

    file = letturaCSV(Path=pathAuto)
        
    for riga in file:
        rigaSplit = riga.strip().split(":")
        
        if mostraAncheBatmobile(rigaSplit) and batmobile:
            auto.append(rigaSplit)  # Aggiunge riga alla lista con ciclo for
        elif nascondiBatmobile(rigaSplit):
            auto.append(rigaSplit)  # Aggiunge riga alla lista con ciclo for

    auto = tipoOrdinamento(auto)
    
    for riga in auto: 
        print("        ", ":".join(riga)) # eliminazione spazi
    
    if len(auto) < 1:
        print("""
        ----------------------------
        Non ci sono auto disponibili
        ----------------------------
                """)       

    file.close()
    
def sempliceAperturaCSV():
    auto = []  # dichiarazione della variabile auto

    print("""
        --------------------------------------------
            AUTO DISPONIBILI PER IL NOLEGGIO
        --------------------------------------------
        ID - MODELLO  - COSTO/Giorno -  DISPONIBILE?
        --------------------------------------------
        """)

    file = letturaCSV(pathAuto)

    # TUTTI I COMMENTI SU FUNZIONE restituisciAuto()
    for riga in file:
        rigaSplit = riga.strip().split(":")
        
        if mostraAncheBatmobile(rigaSplit) and batmobile:
            auto.append(rigaSplit)  # Aggiunge riga alla lista con ciclo for
        elif nascondiBatmobile(rigaSplit):
            auto.append(rigaSplit)  # Aggiunge riga alla lista con ciclo for

    for riga in auto:
        print("        ", ":".join(riga)) # eliminazione spazi
    
    if len(auto) < 1:
        print("""
        ----------------------------
        Non ci sono auto disponibili
        ----------------------------
                """)       

    file.close()
    
def sceltaOrdinamentoAuto(login):

    while True:
        selezione = input("""
        -----------------------------------------------------
        In qual ordine vuoi visualizzare le auto disponibili?
        1. In ordine alfabetico
        2. In ordine di prezzo/giorno crescente
        3. In ordine di prezzo/giorno decrescente
        4. Apertura ordine CSV

        Premi 0 per tornare al menù precedente

        >>> """)

        if selezione == "1":
            ordinamentoAuto(tipoOrdinamento = ordinamentoAutoPerNome)
            menuAccount(login)
        elif selezione == "2":
            ordinamentoAuto(tipoOrdinamento = ordinamentoAutoperPrezzoCrescente)
            menuAccount(login)
        elif selezione == "3":
            ordinamentoAuto(tipoOrdinamento = ordinamentoAutoperPrezzoDecrescente)
            menuAccount(login)
        elif selezione == "4":
            sempliceAperturaCSV()
            menuAccount(login)    
        elif selezione == "0":
            break
        else:
            print("""
        -------------------------
        Selezione non disponibile
        -------------------------
            """)
                     
def registrazione():
    os.system("cls")
    print("""
        -----------------------------  
        PROCEDURA DI REGISTRAZIONE... 
        -----------------------------
        """)
    login = input("""
        Login: """)
    password = input("""
        Password: """)
    
    try:
        file = open(pathUtenti, "r")
    except FileNotFoundError:
        print("""
        --------------------
        Il file non trovato!
        --------------------
              """)

    utenti = []
    for riga in file:
        rigaSplit = riga.strip().split(":")
        utenti.append(rigaSplit[0].strip())

    file.close()

    if login in utenti:
        print("""
        ------------------------
        Questo login è già in uso
        ------------------------
        """)
    else:
        # Aggiungi il nuovo utente al file CSV (meglio append)
        file = open(pathUtenti, "a")
        file.write(f"{login}:{password}\n")
        print("""
        ----------------------
        Registrazione avvenuta
        ----------------------
        """)
              
def schermataBatman(login):
        os.system("cls")
        simboloBatman = """
                _,       _   _    ,_
              .o888P     Y8o8Y     Y888o.
             d88888      88888      88888b
            d888888b_  _d88888b_  _d888888b
            8888888888888888888888888888888
            8888888888888888888888888888888
            YJGS8P"Y888P"Y888P"Y888P"Y8888P
             Y888   '8'   Y8P   '8'   888Y
              '8o          V          o8'
                `                     `
        """
        print(f"""
        {simboloBatman}
        -----------------------------------------
        {login} aka Batman, Accesso garantito
        -----------------------------------------
                """)
        sceltaOrdinamentoAuto(login)    

def verificaLogin():
    os.system("cls")
    utenti = [] # inizializza dizionario per inserire username e password estratti dal CSV

    file = letturaCSV(pathUtenti)
    
    for riga in file:
        # va splitata la riga contenente utente:password
        
        rigaSplit = riga.strip().split(":")
        utenti.append({
            "username": rigaSplit[0].strip(),
            "password": rigaSplit[1].strip()
        })

    file.close() 
    
    login = input("Inserisci Login: ")     
    password = input("Inserisci la tua password: ")
    global batmobile
    
    for utente in utenti:
        if utente["username"] == login == "Bruce Wayne" and utente["password"] == password:
            # spostare qui?
            batmobile = True
            schermataBatman(login) # Schermata personalizzata per Bruce Wayne aka Batman       
            break
           
        elif utente["username"] == login and utente["password"] == password:
            batmobile = False
            print(f"""
        --------------------------------------
        {login}, Accesso garantito
        --------------------------------------
        
        
        Benvenuto {login}
        
                  """)
            sceltaOrdinamentoAuto(login)           
            break      
        
    else:
        print("""
        ---------------
        Password errata
        ---------------
              """)
        #os.system("cls")
                  
def main():
    #os.system("cls")
    if sys.platform.startswith('linux'):
        SO = "Linux"
    elif sys.platform.startswith('darwin'):
        SO = "Mac"
    else:
        SO = "Windows"
    orario = datetime.now()
    avanti = input (f"""
    {orario.date()}  Ore: {orario.hour}:{orario.minute}:{orario.second}
    --------------------------  
        
    Benvenuto utente loggato come: {os.getlogin()} 
    - Usi un computer con: {os.cpu_count()} processori fisici e logici;
    - Il Sistema Operativo in uso è: {SO};
    - Usi Python versione: {platform.python_version()};
    
    Il percorso del tuo VENV (ambiente virtuale) è questo:
    >>> {os.getcwd()}
    
    il percorso dell'eseguibile dell'interprete di Python è questo:
    >>> {sys.executable}
    
    La cartella di questo progetto è questa:
    >>> {os.path.dirname(percorsoQuestoFilePY)}
    
    Sono se non già presenti, sono stati generati automaticamente questi file (utenti.csv e auto.csv) 
    nella cartella di esecuzione di questo file .py ai seguenti percorsi:
    >>> {pathUtenti}
    >>> {pathAuto}
    
                        
    Iniziamo... premi un tasto """)
    os.system("cls")
    while True: # parte da qui per rendere visibile la parte di sopra solo al primo avvio                    
        
        
        scelta = input ("""            
                        
        ######################
        #                    #
        #   R-E-N-T @ B-A-T  #
        #                    #  
        ######################
        
        >>> Messaggio per *Bruce Wayne*: abbiamo un nuovo modello riservato solo per te!
        
        ____________________________            
        Premi 1 per il LOGIN;
        Premi 2 per la REGISTRAZIONE
        Premi 0 per Uscire
        
        >>> """)
        
        if scelta == "1":
            verificaLogin()
        elif scelta == "2":
            registrazione()
        elif scelta == "0":
            break
        else:
            print("""
        -----------------
        Scelta non valida
        -----------------
            """)

def generazioneCSVDefault():
    
    # Creare i due file CSV nella cartella di questo file .py
    File_CSV_Utenti = "utenti.csv"
    File_CSV_Auto = "auto.csv"
    percorsoFileUtenti = os.path.join(percorsoCartellaFilePY, File_CSV_Utenti)
    percorsoFileAuto = os.path.join(percorsoCartellaFilePY, File_CSV_Auto)

    # dati default utenti.csv
    datiDefaultUtenti = [
        ["admin", "admin"],
        ["Bruce Wayne", "0000"],
        ["Mario", "Rossi"]
    ]

    # dati default auto.csv
    datiDefaultAuto = [
        ["1", "Batmobile", "1000000", "True"],
        ["2", "Toyota Supra", "150", "True"],
        ["3", "Ford Fiesta", "80", "True"],
        ["4", "Nissan Celica", "100", "False"],
        ["5", "Fiat 500XL", "60", "True"],
        ["7", "Toyota Yaris", "55", "True"],
        ["10", "Fiat Panda", "35", "True"],
        ["11", "Ford KA", "40", "True"],
        ["12", "Ferrari Testarossa", "900", "True"],
        ["13", "Fiat Uno", "25", "True"],
        ["14", "Ford Mustang", "125", "False"],
        ["15", "Nissan Skyline", "200", "True"],
        ["16", "Corvette Camaro", "180", "False"],
        ["17", "Land Rover", "140", "True"],
        ["18", "Jeep Renegade", "75", "True"]
    ]

    if not os.path.exists(percorsoFileUtenti):
    # Apri il file in modalità scrittura con controllo se NON esiste già
        with open(percorsoFileUtenti, "w") as File_CSV_Utenti:
            for riga in datiDefaultUtenti:
                linea1 = ":".join(riga)  # Unisci i dati di ogni riga con una virgola
                File_CSV_Utenti.write(linea1 + "\n")
    
    if not os.path.exists(percorsoFileAuto):
    # Apri il file in modalità scrittura con controllo se NON esiste già    
        with open(percorsoFileAuto, "w") as File_CSV_Auto:
            for riga in datiDefaultAuto:
                linea2 = ":".join(riga)  # Unisci i dati di ogni riga con una virgola
                File_CSV_Auto.write(linea2 + "\n")
 
# INIZIO DA QUI SOTTO
generazioneCSVDefault()                       
main()


'''
# possibile soluzione definire cartella CSV

import os
import tkinter as tk
from tkinter import filedialog

def select_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(initialdir=os.getcwd(), title="Seleziona una cartella")
    return directory

# Utilizzo dell'interfaccia per selezionare la cartella
selected_directory = select_directory()

# Verifica se è stata selezionata una cartella
if selected_directory:
    # Utilizza la cartella selezionata come percorso di salvataggio per i file CSV
    percorsoCartellaFilePY = selected_directory
    print("Cartella selezionata:", percorsoCartellaFilePY)
else:
    print("Nessuna cartella selezionata")'''
