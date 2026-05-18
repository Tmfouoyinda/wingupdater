import subprocess

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
            result = subprocess.run(["sudo", "apt", "update"])
            if result.returncode == 0:
                result = subprocess.run(["sudo", "apt", "upgrade", "-y"])
                if result.returncode == 0:
                    print("Système mis à jour avec succès.")
                else:
                    print(f"Erreur lors de apt upgrade (code {result.returncode}).")
            else:
                print(f"Erreur lors de apt update (code {result.returncode}).")

        elif choice == 2:
            print("Mise à jour des logiciels...")
            result = subprocess.run(["sudo", "apt", "upgrade", "-y"])
            if result.returncode == 0:
                print("Logiciels mis à jour avec succès.")
            else:
                print(f"Erreur lors de la mise à jour des logiciels (code {result.returncode}).")

        elif choice == 3:
            print("Au revoir.")
            break
        else:
            print("Choix invalide, réessayez.")

wingudater()
