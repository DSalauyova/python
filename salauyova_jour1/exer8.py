# ex_8 : Écrire une fonction qui prend deux listes et renvoie une nouvelle liste contenant
# uniquement les éléments communs aux deux listes.
# test : print(elements_communs([1, 2, 3, 4], [2, 4, 6, 8])) # Affiche [2, 4]

def get_commun_list():
    first_list = [1, 2, 3, 4]
    second_list = [2, 4, 6, 8]
    # comparer les elements de chaque tableau
    match = []
    for el in first_list:
        if el in second_list:
            match.append(el)
    print(match)
get_commun_list()