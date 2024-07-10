# Écrivez une fonction qui vérifie si une chaîne est un palindrome (se lit de la même façon dans les deux sens).
# test: print(est_palindrome("radar")) # Output: True
# print(est_palindrome("python")) # Output: False
def is_it_palindrome(string):
    # le mot initial est egale au mot inversé
    return string == string[::-1]
    
print("radar is palindrome:",is_it_palindrome("kayak"))
print("hello is palindrome:",is_it_palindrome("hello"))