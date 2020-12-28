from cryptography.fernet import Fernet

key = Fernet.generate_key()

crypter = Fernet(key)
pw= crypter.encrypt(b'mypassword')
decrypter = crypter.decrypt(pw)

print(str(pw,'utf8'))
print(str(decrypter,'utf8'))

