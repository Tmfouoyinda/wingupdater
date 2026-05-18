import subprocess


def ouvrir_windows_update():
    subprocess.run(["cmd", "/c", "start", "", "ms-settings:windowsupdate"])


def mettre_a_jour_logiciels():
    subprocess.run(["winget", "upgrade", "--all", "--accept-source-agreements", "--accept-package-agreements"])


def winget_updater():
    while True:
        print("\n1) Mettre son système à jour")
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
            print("Ouverture des paramètres Windows Update...")
            ouvrir_windows_update()
        elif choix == 2:
            print("Lancement de la mise à jour des logiciels...")
            mettre_a_jour_logiciels()
        elif choix == 3:
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")


winget_updater()
