# ex_1: Écrire un script Python qui affiche des informations de base sur le système,
# telles que le nom d'hôte, l'adresse IP, l'architecture du processeur et la version du
# système d'exploitation

import socket
import platform         
import sys
from osarch import detect_system_architecture

get_data_system = platform.system()
get_hostname = socket.gethostname()
get_ip_address = socket.gethostbyname('pythoniaformation.com')
get_local_server = socket.gethostbyname(get_hostname)
os_name, architecture = detect_system_architecture()
print(get_data_system)
print(get_hostname)
print(get_ip_address)
print(get_local_server)
print(f"OS: {os_name}, Architecture: {architecture}")