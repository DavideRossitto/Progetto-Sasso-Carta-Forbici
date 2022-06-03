#Importo le librerie necessarie per far funzionare il programma

import random
import time

#Funzione che gestisce l'intera partita

mosse_valide = ['sasso','carta','forbici']

def Partita(mossaComputer):
    verifica=True
    while (verifica):
        mossaGiocatore = input("Scegli tra Sasso, Carta, Forbici: ")
        time.sleep(1)

        #Ricerca di tutti i casi possibili

        if (mossaGiocatore.lower()!=mosse_valide[0]) and (mossaGiocatore.lower()!=mosse_valide[1]) and (mossaGiocatore.lower()!=mosse_valide[2]):
            print("Inserisci un oggetto tra quelli elencati")
        else:
            print("Hai scelto: " + mossaGiocatore.lower()+"\n")
            time.sleep(1)
            print("Sas-so!")
            time.sleep(1)
            print("Car-ta!")
            time.sleep(1)
            print("For-bi-ci!\n")
            time.sleep(1)

            #Se si verifica un pareggio viene richiamata la funzione MossaComputer() in modo tale da far ripartire la mano cambiando oggetto

            if mossaComputer.__eq__(mossaGiocatore.lower().capitalize()):
                print("Computer: " + mossaComputer + " vs Tu: " + mossaGiocatore.lower().capitalize())
                print("Pareggio!")
                print("ATTENZIONE! IL COMPUTER HA CAMBIATO OGGETTO!")
                Partita(MossaComputer())
                break
            elif (mossaComputer == "Forbici" and mossaGiocatore.lower().capitalize() == "Sasso") or (mossaComputer == "Carta" and mossaGiocatore.lower().capitalize() == "Forbici") or (mossaComputer == "Sasso" and mossaGiocatore.lower().capitalize() == "Carta"):
                print("Computer: " + mossaComputer + " vs Tu: " + mossaGiocatore.lower().capitalize())
                print("Hai vinto!")
                break
            else:
                print("Computer: " + mossaComputer + " vs Tu: " + mossaGiocatore.lower().capitalize())
                print("Hai perso...")
                break

#Funzione che assegna gli oggetti al computer

def MossaComputer():
    mossacomputer = ""
    rnd = random.randrange(1,3)
    if rnd == 1:
        mossacomputer = "Sasso"
    elif rnd == 2:
        mossacomputer = "Carta"
    elif rnd == 3:
        mossacomputer = "Forbici"
    return mossacomputer

#Funzione richiamata soltato se il giocatore desidera rigiocare

def RigiocaPartita() :
    v2 = True
    while (v2) :
        rigioca = input("Vuoi rigiocare?: ")
        if rigioca.lower().capitalize() == "Si" :
            time.sleep(1)
            print("\nOk...Sto avviando una nuova partita...\n")
            time.sleep(3)
            Partita(MossaComputer())
        elif rigioca.lower().capitalize() == "No" :
            time.sleep(2)
            print("\nOk, ritorna quando vorrai rigiocare!")
            v2 = False
        elif rigioca.lower().capitalize() != "Si" or rigioca.lower().capitalize() != "No" :
            print("Digita una risposta adeguata!")
            time.sleep(2)

#Main

mossaComputer=MossaComputer()
Partita(mossaComputer)
RigiocaPartita()