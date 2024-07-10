# ex_2: Créez une fonction qui compte le nombre d'occurrences de chaque lettre dans une
# chaîne de caractères.
# test: print(compter_lettres("hello")) # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def count_letter(string):
    # creation d'un objet
    word = {}
    for letter in string:
        # initaliser le nombre de lettre à 0
        number = 0
        # trouver le nombre de lettres dans le mot
        if letter in word:
            number = word[letter] + 1 
        else:
            number = 1
        # fonction update insert des items dans le dictionnaire
        word.update({letter: number})
    return word
print(count_letter('hello'))