import random
einkaufs_liste = []
def menue_anzeigen():
    print("Willkommen zu deiner Einkaufsliste!")
    print("Was möchtest du machen?")

    print("1. Artikel hinzufügen")
    print("2. Artikel entfernen")
    print("3. Einkaufsliste anzeigen")  
    print("4. Beenden")

def artikel_hinzufügen(liste, artikel):
    liste.append(artikel)
    print(f"{artikel} wurde zur Einkaufsliste hinzugefügt.")

def artikel_entfernen(liste, input_choice): 
        if input_choice in liste: 
            liste.remove(input_choice)
            print(f"{input_choice} wurde von der Einkaufsliste entfernt. ")
        else: print("Element gibt es schon nicht mehr!")
        
        
def einkaufsliste_anzeigen(liste):
    if liste: 
        print("Deine Einkaufsliste:")
        for element in liste: 
            print(f"- {element}")
            
def random_choice(liste):
    if liste: 
        element = random.choice(liste)
        print(f"Das ist ein random Element aus dem Korb, {element}")
    else:  print("Es ist noch nichts enthalten")
def mischen(liste): 
    if liste: 
        random.shuffle(liste)
    else: print("Die Liste ist noch leer, wir können nichts mischen!!!")
menue_anzeigen()
while True:
    input_choice = input("Bitte wähle eine Option (1-4): ")

    if input_choice == "1":
            artikel = input("Gib den Artikel ein, den du hinzufügen möchtest: ")
            artikel_hinzufügen(einkaufs_liste, artikel)
    elif input_choice == "2":
        input_choice = input("Gib den Artikel ein, den du entfernen möchtest: ") 
        artikel_entfernen(einkaufs_liste, input_choice)
    elif input_choice == "3":  
        einkaufsliste_anzeigen(einkaufs_liste)
    elif input_choice == "4":
        print("Auf Wiedersehen!")
        break
    elif input_choice == "5":
       print("Du hast das Geheime Zahlenspiel entdeckt, Gib mir nacheinander 2 zahlen und du bekommste eine random zahl aus dem Bereich")
       start = int(input("Gib mir den Startpunkt des Zahlenbereichs !"))
       ende = int(input("Gib mir den Endpunkt des Zahlenbereichs !"))
       zahl = random.randint(start, ende)
       print(zahl)
    elif input_choice == "6":
        random_choice(einkaufs_liste)
    elif input_choice =="7":
        mischen(einkaufs_liste)

            
            