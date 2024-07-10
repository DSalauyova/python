# Créer un serveur TCP qui renvoie au client exactement ce qu'il a reçu. Le client
# envoie plusieurs messages au serveur et affiche les réponses.
import socket
# creer socket
server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ADDRESS = 'localhost'
PORT = 8888
# lier socket à l'adresse et port
server_tcp.bind((ADDRESS, PORT))
# activer
server_tcp.listen(1)

print(f"Server is actif at {ADDRESS} : {PORT}")

while True:
    client_socket, client_address = server_tcp.accept()
    print(f"Connexion {client_socket} is accepted {client_address}")
    # reçoit les donnees de la taille max 1024
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Message reçu: {message}")
    response = f"Message renvoyé: {message}"
    client_socket.send(response.encode('utf-8'))
    client_socket.close()
    print(f"Connexion fermée avec {client_address}")

    if __name__ == "__main__":
        server_tcp
