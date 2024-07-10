# ex_2: Créer un script qui liste tous les fichiers d'un répertoire spécifié, en incluant
# leur taille. La fonction doit prendre en paramètre le dossier

# OS
import os
# lister les fichiers du dossier courrant
current_folder = os.listdir()
desktop_path = "/Users/admin/Desktop"
target_folder = os.chdir(desktop_path)

print(current_folder)