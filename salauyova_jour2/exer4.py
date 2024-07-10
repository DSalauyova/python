# ex_4: Créer un script qui surveille et affiche l'utilisation du CPU en pourcentage
# toutes les 5 secondes.
import psutil
import time

while True:
    time.sleep(5)
    cpu = psutil.cpu_percent()
    print(cpu)