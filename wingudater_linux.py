import os

def wingudater():
    while True:
        print("1) Mettre son système à jour (dépôts + paquets)")
        print("2) Mettre ses logiciels à jour (paquets uniquement)")
        print("3) Quitter")

        try:
            choice = int(input("Votre choix : "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")
            continue
        except KeyboardInterrupt:
            print("\nInterruption détectée. Au revoir.")
            break

        if choice == 1:
            print("Mise à jour du système...")
            os.system("sudo apt update && sudo apt upgrade -y")
        elif choice == 2:
            print("Mise à jour des logiciels...")
            os.system("sudo apt upgrade -y")
        elif choice == 3:
            print("Au revoir.")
            break
        else:
            print("Choix invalide, réessayez.")

wingudater()