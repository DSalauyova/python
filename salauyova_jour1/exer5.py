# Écrivez une fonction qui prend une chaîne de caractères et retourne le mot le plus
# long de cette chaîne. print(trouver_le_plus_long_mot("Le python est un excellent langage de programmation"))
def get_longer_word(string):
    # f split divise la phrase en mots
    sentense = string.split(" ")
    # initialiser le plus grand mot
    longer_word = ""
    for word in sentense:
        # parcourir la phrase en cherchant le mot le plus long
        if len(word) > len(longer_word):
            longer_word = word
    return longer_word
print(get_longer_word("Le python est un excellent langage de programmation"))
