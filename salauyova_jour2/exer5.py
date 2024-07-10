# SHutil

# ex_5 : Écrire un script qui vérifie l'espace disque disponible et utilisé sur le disque
# principal.
import psutil
# en param chemin vers le disque
main_disk = psutil.disk_usage('/')
print(main_disk)