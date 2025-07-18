#l'Utente puó aggiungere spesa, vedere  tutte le spese, calcolare il totale, cancellare una spesa, modificare una spesa, ssalvare e caricare le espese dal file .csv

#si puo aggiungere uninterfaccia grafica (gui) con Tkinter o streamlit.

tutte_le_spese = []

def aggiungi_spesa():
    print("\n--- Aggiungi una nuova spesa ---")
    prodotto = input("Prodotto o servizio: ")
    descrizione = input("Descrizione: ")
    importo = float(input("Importo (€): "))
    data = input("Data (es. 13-07-2025): ")
    addebito = input("Prenotare addebito bancario (si/no): ")
    pagato = input("Pagato? (si/no): ")

    spesa = {
        "prodotto": prodotto,
        "descrizione": descrizione,
        "importo": importo,
        "data": data,
        "addebito": addebito,
        "pagato": pagato
    }
    tutte_le_spese.append(spesa)
    print("✅ Spesa aggiunta con successo!")
    salva_spese_su_csv()

#Funzione per mostrare tutte le spese; controllare e stampare in modo ordinato.
def mostra_spese():
    print("\n--- Elenco delle spese ---")
    if not tutte_le_spese:
        print("Nessuna spesa trovate.")
        return

    for i, spesa in enumerate(tutte_le_spese, start=1):
        print(f"\nSpesa #{i}")
        print(f" Prodotto: {spesa['prodotto']}")
        print(f" Descrizione: {spesa['descrizione']}")
        print(f" Importo: € {spesa['importo']}")
        print(f" Data: {spesa['data']}")
        print(f" Addebito: {spesa['addebito']}")
        print(f" Pagato: {spesa['pagato']}")

def mostra_menu():
    print("\n=== GESTORE SPESE ===")
    print("1. Aggiungi una spesa")
    print("2. Mostra tutte le spese")
    print("3. Calcola totale spese")
    print("4. Cancella una spesa")
    print("5. Modifica una spesa")
    print("6. Esci")

def calcola_totale():
    print("\n--- Totale delle spese ---")
    if not tutte_le_spese:
        print("Nessuna spesa trovata.")
        return
    totale = 0
    for spesa in tutte_le_spese:
        try:
            importo = float(spesa["importo"])
            totale += importo
        except ValueError:
            print(f"⚠️ Importo non Valido nella Spesa: {spesa['prodotto']}")

    print(f"💰 Totale speso: € {totale:.2f}")

def cancella_spesa():
    print("\n--- Cancella una Spesa ---")

    if not tutte_le_spese:
        print("Nessuna spesa da cancellare.")
        return

    mostra_spese()  #utilizando la funzione esistente

    try:
        numero = int(input("\nInserisci il numero della spesa da cancellare: "))
        if 1 <= numero <= len(tutte_le_spese):
            spesa = tutte_le_spese[numero - 1]
            conferma = input(f"Confirmi di voler cancellare '{spesa['prodotto']}'? (si/no): ")
            if conferma.lower() in ["sì" , "si"]:
                del tutte_le_spese[numero - 1]
                print("Spesa cancellata.")
                salva_spese_su_csv()
            else:
                print("Annullato.")
        else:
            print("⚠️Numero non valido.")
    except ValueError:
        print("⚠️Inserisci un numero valido.")

def modifica_spesa():
    print("\n---Modifica una Spesa ---")

    if not tutte_le_spese:
        print("Nessuna spesa da modificare.")
        return

    mostra_spese()

    try:
        numero = int(input("\nInserisci il numero della spesa da modificare: "))
        if 1 <= numero <= len(tutte_le_spese):
            spesa = tutte_le_spese[numero - 1]

            print("Lascia vuoto il campo per non cambiarlo.")
            nuovo_prodotto = input(f"Prodotto ({spesa['prodotto']}): ") or spesa["prodotto"]
            nuova_descrizione = input(f"Descrizione ({spesa['descrizione']}): ") or spesa["descrizione"]
            nuovo_importo = input(f"Importo (€) ({spesa['importo']}): ")
            nuova_data = input(f"Data ({spesa['data']}): ") or spesa["data"]
            nuovo_addebito = input(f"Addebito ({spesa['addebito']}): ") or spesa["addebito"]
            nuovo_pagato = input(f"Pagato? ({spesa['pagato']}): ") or spesa["pagato"]

            spesa["prodotto"] = nuovo_prodotto
            spesa["descrizione"] = nuova_descrizione
            spesa["importo"] = float(nuovo_importo) if nuovo_importo else spesa["importo"]
            spesa["data"] = nuova_data
            spesa["addebito"] = nuovo_addebito
            spesa["pagato"] = nuovo_pagato

            print("✏️ Spesa modificata con successo!")
            salva_spese_su_csv()

        else:
            print("⚠️ Numero non valido.")
    except ValueError:
        print("⚠️ Inserisci un numero valido.")

import csv
def salva_spese_su_csv(nome_file="spese.csv"):
    intestazioni = ["prodotto", "descrizione", "importo", "data", "addebito", "pagato"]

    with open(nome_file, mode="w", newline= "", encoding="utf-8") as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=intestazioni)
        writer.writeheader()
        for spesa in tutte_le_spese:
            writer.writerow(spesa)
    print("Spese salvate su file CSV.")


def carica_spese_da_csv(nome_file="spese.csv"):
    try:
        with open(nome_file, mode="r", newline="", encoding="utf-8") as file_csv:
            reader = csv.DictReader(file_csv)
            for riga in reader:
                spesa = {
                    "prodotto": riga["prodotto"],
                    "descrizione": riga["descrizione"],
                    "importo": float(riga["importo"]),
                    "data": riga["data"],
                    "addebito": riga["addebito"],
                    "pagato": riga["pagato"]
                }
                tutte_le_spese.append(spesa)
        print("📂 Spese caricate dal file CSV.")
    except FileNotFoundError:
        print("⚠️ Nessun file CSV trovato. Iniziamo da zero.")

carica_spese_da_csv()

while True:
    mostra_menu()
    scelta = input("Scegli un'opizione: ")

    if scelta == "1":
        aggiungi_spesa()
    elif scelta == "2":
        mostra_spese()
    elif scelta == "3":
        calcola_totale()
    elif scelta == "4":
        cancella_spesa()
    elif scelta == "5":
        modifica_spesa()
    elif scelta == "6":
        print("Arrivederci!")
        break
    else:
        print("Scelta non valida.")