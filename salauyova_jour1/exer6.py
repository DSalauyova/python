# Écrivez une fonction qui détecte toutes les dates au format JJ/MM/AAAA dans une
# chaîne de caractères et les retourne dans une liste.
# test : print(detecter_dates("Les dates importantes sont 12/05/2022 et 23/11/2023."))
import re

def detecter_dates(string):

    regex_date = r'\b\d{2}/\d{2}/\d{4}\b'
  

    dates = re.findall(regex_date, string)

    return dates

string = "Les dates importantes sont 12/05/2022 et 23/11/2023"
print(detecter_dates(string))
