from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import binascii

keys = RSA.generate(2048)

pk = keys.publickey()
print(f'pk: (n={hex(pk.n)}, e={hex(pk.e)})')
pkPem = pk.exportKey()
print(pkPem.decode('ascii'))

print(f"Private key: (n={hex(pk.n)}, d={hex(keys.d)})")
skPEM = keys.exportKey()
print(skPEM.decode('ascii'))

msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pk)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keys)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)