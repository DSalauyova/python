# ex_10 : Écrire une fonction qui trouve la plus longue sous-liste croissante dans une liste
# test : print(plus_longue_croissante([1, 2, 2, 3, 2, 3, 4, 1])) # Affiche [2, 3, 4]
def longest_street(array):
    current_street = []
    max_street = []
    max_length = 0
    current_length = 0

    for el in array:
        if array[el] > array[el - 1]:
            current_street.append(array[el])
            current_length +=1
        else:
            if current_length > max_length:
                max_length = current_length
                max_street = current_street
            current_street = [array[el]]
            current_length = 1
    if current_length > max_length:
        max_street = current_street
    # return sorted(list_of_nu)
    return(max_street)

array = [1, 2, 2, 3, 2, 3, 4, 1]
print(longest_street(array))