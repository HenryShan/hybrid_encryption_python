from Cryptodome.Cipher import AES
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import binascii
import numpy as np

# def modular_exponentiation(g, e, N):
#     if g == 0:
#         return 0
#     elif g == 1:
#         return 1
#     elif N <= 0:
#         print('invalid modulas')
#         return 0
#     elif e < 0:
#         print('invalid exponent')
#         return 0
#     rest = e
#     bits = np.array([])
#     while rest > 0:
#         i = 0
#         while 2**i < rest:
#             i += 1
#         i -= 1
#         rest -= 2**i
#         bits = np.append(bits, i)
#         if rest == 1:
#             bits = np.append(bits, 0)
#             break
#         elif rest == 0:
#             break
#     base = g % N
#     lexp = bits[0] #the largest exponent
#     material = np.array([])
#     for i in range(0, int(lexp) + 1):
#         exp = (int(base**(2**i))) % N
#         material = np.append(material, exp)
#
#     result = 1
#     for exps in bits:
#         result = int((result * material[int(exps)]) % N)
#     return result


# 'file' : the file need to encrypt
file = 'siesta.jpg'
with open(file, 'rb') as f:
    data = f.read()
# data = binascii.hexlify(content)

print("Please input your 16-bytes numerical AES-Key1:")
AESkey1_row = input()
if len(AESkey1_row) != 16:
    print("Your input is not valid!")
    exit(1)
# try:
#     AESkey1 = int(AESkey1_row)
# except ValueError:
#     print("AES key1 must be a numerical value!")
#     exit(1)
AESkey1 = AESkey1_row.encode('utf-8')

print("Please input your 16-bytes AES-Key2:")
AESkey2_row = input()
if len(AESkey2_row) != 16:
    print("Your input is not valid!")
    exit(1)
AESkey2 = AESkey2_row.encode('utf-8')

print("reading RAS public key")
f = open('keys.pem', 'r')
keys = RSA.import_key(f.read())
pk = keys.publickey()
N = pk.n
e = pk.e

# print("Please input your RSA public key in format 'N,e':")
# RSAkey_row = input()
# key_seg = RSAkey_row.split(',')
# try:
#     N = int(key_seg[0])
#     e = int(key_seg[1])
# except ValueError:
#     print("Your input is not a valid key!")
#     exit(1)

# first, calculate RA_key
encryptor = PKCS1_OAEP.new(pk)
RA_key = encryptor.encrypt(AESkey1)
print('RA key is : ',type(RA_key))
# RA_key = modular_exponentiation(AESkey1, e, N)

# then, calculate Secondary mixing key
cipher_2 = AES.new(AESkey2, AES.MODE_EAX)
ra_nonce = cipher_2.nonce
ra_nonce_f = open('ra_nonce','wb')
ra_nonce_f.write(ra_nonce)
ra_nonce_f.close()

# not sure if padding is needed --seems not
# need to padding RA_key if it is not a multiple of 16, or exit if RA_key is longer than 16 bytes
# RA_key = str(RA_key)
# len_diff = 16 - (len(RA_key) % 16)
# if len_diff > 0:
#     for i in range(0, len_diff):
#         RA_key = '0' + RA_key
# print(RA_key)
# RA_key = RA_key.encode('utf-8')
mix_key, ra_tag = cipher_2.encrypt_and_digest(RA_key)
mix_f = open('mix_f', 'wb')
mix_f.write(mix_key)
mix_f.close()
ra_tag_f = open('ra_tag_f', 'wb')
ra_tag_f.write(ra_tag)
ra_tag_f.close()

# now, encrypt file
cipher = AES.new(AESkey1, AES.MODE_EAX)
file_nonce = cipher.nonce
file_nonce_f = open("file_nonce", "wb")
file_nonce_f.write(file_nonce)

ciphertext, tag = cipher.encrypt_and_digest(data)
file_ciphered = open("file_encoded", 'wb')
file_ciphered.write(ciphertext)
file_ciphered.close()
file_tag_f = open("file_tag", 'wb')
file_tag_f.write(tag)
file_tag_f.close()

# send AES key2 together with other data
AES_2 = open('AES2', 'wb')
AES_2.write(AESkey2)
AES_2.close()