# PSutil
# ex_3: Écrire un script qui affiche l'utilisation de la mémoire du système.
import psutil

def sys_memory():
    print(
        psutil.virtual_memory()
    )

sys_memory()
