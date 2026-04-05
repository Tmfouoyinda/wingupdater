import os

while True:
    print("1) Mettre son système à jour")
    print("2) Mettre ces logiciel à jour")
    print("3) Quitter")
    try:
        choix = int(input("Choix : "))
    except ValueError:
        print("Erreur : veuillez entrer un nombre valide.")
        continue
    except KeyboardInterrupt:
        print("\nInterruption détectée. Au revoir !")
        break



    if choix == 3:
        print("Au revoir !")
        break
    elif choix == 1:
        try:
            print("Mise à jour du système...")
            os.system("winget upgrade --id Microsoft.Windows --accept-source-agreements")
        except KeyboardInterrupt:
            print("\nMise à jour interrompue.")
    elif choix == 2:
        try:
            print("Mise à jour des logiciels...")
            os.system("winget upgrade --all --accept-source-agreements")
        except KeyboardInterrupt:
            print("\nMise à jour interrompue.")
    else:
        print("choix invalide, réssayez.")
