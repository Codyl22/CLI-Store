#!/usr/bin/env python3
import subprocess
import os
import sys

# ==============================================================================
# GESTION DE LA LANGUE (FRANÇAIS / ANGLAIS)
# ==============================================================================

# On détecte la langue du système Linux
SYSTEM_LANG = os.environ.get("LANG", "en")
IS_FR = SYSTEM_LANG.startswith("fr")

LOCALES = {
        "banner": " --- UNIVERSAL LINUX PACKAGES SEARCH ---" if not IS_FR else " --- RECHERCHE UNIVERSELLE DE PAQUETS LINUX ---",
        "sec_title": "[SECURITY] This tool requires root privileges to install packages." if not IS_FR else "[SÉCURITÉ] Cet outil nécessite les privilèges root pour installer des paquets.",
        "sec_auth": "Please authenticate." if not IS_FR else "Veuillez vous authentifier.",
         "sec_ok": "[OK] Authentication successful. Root access granted." if not IS_FR else "[OK] Authentification réussie. Accès root accordé.",
        "sec_fail": "[ERROR] Authentication failed or acess denied. Exiting." if not IS_FR else "[ERREUR] Échec de l'authentification ou accès refusé. Fermeture.",
        "press_enter": "Press Enter to open the search bar..." if not IS_FR else "Appuyez sur Entrée pour ouvrir la barre de recherche...",
        "forced_exit": "\n\nForced closure of CLI-Store." if not IS_FR else "\n\nFermeture forcé du Cli-Store.",
        "step1_ok": "\n[OK] Step 1 validated. Ready for the next block." if not IS_FR else "\n[OK] Étape 1 validée. Prêt pour la suite.",
        "search_prompt": "[CLI-Store] Enter your search (or 'Q' to quit) :" if not IS_FR else "[CLI-Store] Entrez votre recherche (ou 'Q' pour quitter) :",
        "search_exit": "Leaving CLI-Store. See you!" if not IS_FR else "Sortie de CLI-Store. À la prochaine !",
        "no_pm": "[ERROR] No compatible package manager found (APT, DNF, PACMAN).Exiting." if not IS_FR else "[ERREUR] Aucun gestionnaire de paquetscompatible trové (APT, DNF, PACMAN). Fermeture.",
        "searching": "Searching for packages..." if not IS_FR else "Recherche des paquets en cours..."
}
BANNER =f"""
======================================================
               CLI-STORE v0.1-bêta
{LOCALES['banner']}
======================================================
"""

# ==============================================================================
# SÉCURITÉ & ACCÈS ROOT
# ==============================================================================

def check_root():
    """Vérifier ou demande les privilèges root via sudo dès le départ"""
    print(BANNER)
    print (LOCALES["sec_title"])
    print (LOCALES["sec_auth"] + "\n")

    try:
        # On rafraîchît le token sudo en arrière-plan
        subprocess.run(["sudo", "-v"], check=True)
        print(f"\n{LOCALES['sec_ok']}")
    except subprocess.CalledProcessError:
        print(f"\n{LOCALES['sec_fail']}")
        sys.exit(1)
# ==============================================================================
# BOUCLE PRINCIPALE
# ==============================================================================

def detect_package_manager():
    """Détecte le gestionnaire de paquets disponible sur le système"""
    if os.path.exists("/usr/bin/dnf"):
        return "dnf"
    elif os.path.exists("/usr/bin/apt") or os.path.exists("usr/bin/apt-get"):
        return "apt"
    elif os.path.exists("usr/bin/pacman"):
        return "pacman"
    return None

def main():
    # Écran au démarrage
    os.system("clear")

    # On sécurise l'accès en demandant le mot de passe root
    check_root()

    # Petite pause pour valider visuellement la connexion
    input(f"\n{LOCALES['press_enter']}")

    # Boucle de la barre de recherche
    while True:
        os.system ("clear")
        print(BANNER)

        # On demande la saisie
        query = input(LOCALES["search_prompt"]).strip()

        # Si l'utilisateur veut quitter
        if query.upper() == "Q":
            print (f"\n{LOCALES['search_exit']}\n")
            break # On sort de la boucle et on quitte le script

        # Si l'utilisateur a appuyé sur Entrée sans rien écrire
        if not query:
            continue

        # --- BLOC TEST ---
        print(f"\n[TEST] Tu as recherché le mot : {query}")
        input ("\nAppuie sur Entrée pour refaire un recherche...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(LOCALES["forced_exit"])
