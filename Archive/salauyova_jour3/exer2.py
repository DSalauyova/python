# Écrivez un programme Python qui définit une fonction pour générer
# des mots de passe aléatoires d'une longueur spécifiée. La fonction
# prend un paramètre optionnel longueur, qui est défini par défaut à 8.
# Si aucune longueur n'est spécifiée par l'utilisateur, le mot de passe
# aura 8 caractères.

import secrets
import string

def password_generate(pass_length):
    pass_length = 8
    letters = string.ascii_letters
    chiffres = string.digits
    special_chars = string.punctuation

    alphabet = letters + str(chiffres) + special_chars
    password = ""
    password = "".join(secrets.choice(alphabet) 
    for el in range(pass_length)) 
    return password

print(password_generate(8))