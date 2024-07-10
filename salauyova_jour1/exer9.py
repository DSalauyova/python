# ex_9 : Écrire une fonction qui compte combien de fois un élément apparaît dans une liste.
# test : print(compter_occurrences([1, 4, 2, 7, 4, 4, 3], 4)) # Affiche 3

def count_elements(array, element):
    return array.count(element)

list_of_numbers = [1, 4, 2, 7, 4, 4, 3]
element = 4
func_count = str(count_elements(list_of_numbers, element))
print("Le nombre 4 est", func_count + " fois dans la liste")