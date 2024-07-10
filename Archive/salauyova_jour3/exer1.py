import hashlib

string = "Python123"
hash_password = hashlib.sha256(string.encode())
print(hash_password.hexdigest())
