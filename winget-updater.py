import os

def winget_updater():
    while True:
        print("1) Mettre son système à jour")
        print("2) Mettre ses logiciels à jour")
        print("3) Quitter")

        try:
            choix = int(input("Choix : "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")
            continue
        except KeyboardInterrupt:
            print("\nInterruption détectée. Au revoir !")
            break

        if choix == 1:
            print("Mise à jour du système...")
            os.system("start ms-settings:windowsupdate")
        elif choix == 2:
            print("Mise à jour des logiciels...")
            os.system("winget upgrade --all --accept-source-agreements")
        elif choix == 3:
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")

winget_updater()
