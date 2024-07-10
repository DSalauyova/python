# ex_4 : Créez une fonction qui remplace tous les espaces d'une chaîne par des tirets``
def replace_space_by_dash(space, dash):
    # fonction replace remplace 1er param par le second
    return space.replace(" ",dash)
print(replace_space_by_dash("Bonjour tout le monde","-"))
