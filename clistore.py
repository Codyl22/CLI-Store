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
}
BANNER =f"""
======================================================
               CLI-STORE v0.0.1-bêta
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

def main():
    # Écran au démarrage
    os.system("clear")

    # Étape 1 : On sécurise l'éccès en demandant le mot de passe root
    check_root()

    # Petite pause pour valider visuellement la connexion
    input(f"\n{LOCALES['press_enter']}")

    print(LOCALES["step1_ok"])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(LOCALES["forced_exit"])
