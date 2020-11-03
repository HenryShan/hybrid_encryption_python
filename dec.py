from Cryptodome.Cipher import AES
import numpy as np

def modular_exponentiation(g, e, N):
    if g == 0:
        return 0
    elif g == 1:
        return 1
    elif N <= 0:
        print('invalid modulas')
        return 0
    elif e < 0:
        print('invalid exponent')
        return 0
    rest = e
    bits = np.array([])
    while rest > 0:
        i = 0
        while 2**i < rest:
            i += 1
        i -= 1
        rest -= 2**i
        bits = np.append(bits, i)
        if rest == 1:
            bits = np.append(bits, 0)
            break
        elif rest == 0:
            break
    base = g % N
    lexp = bits[0] #the largest exponent
    material = np.array([])
    for i in range(0, int(lexp) + 1):
        exp = (int(base**(2**i))) % N
        material = np.append(material, exp)

    result = 1
    for exps in bits:
        result = int((result * material[int(exps)]) % N)
    return result

RSA_E = 0
print("Please input your E in RSA public key:")
RSA_E_row = input()
try:
    RSA_E = int(RSA_E_row)
except ValueError:
    print("Your E is invalid!")
    exit(1)

prime_pair = open("prime.txt",'r')
content = prime_pair.read()
primes = content.split(',')
p = primes[0]
q = primes[1]
phi_n = (int(p) - 1) * (int(q) - 1)
print(phi_n)
D = 0
while (RSA_E * D) % phi_n != 1:
    D += 1
print(D)
N = int(p) * int(q)


# first, calculate RA key
AES2 = open("AES2", 'rb')
AES_key2 = AES2.read()
AES2.close()
ra_nonce_f = open('ra_nonce', 'rb')
ra_nonce = ra_nonce_f.read()
ra_nonce_f.close()
cipher_1 = AES.new(AES_key2, AES.MODE_EAX, nonce=ra_nonce)
mix_f = open('mix_f', 'rb')
mix_key = mix_f.read()
mix_f.close()
ra_tag_f = open("ra_tag_f", 'rb')
ra_tag = ra_tag_f.read()
ra_tag_f.close()

RA_key = cipher_1.decrypt(mix_key)
try:
    cipher_1.verify(ra_tag)
except ValueError:
     print("Key incorrect or plaintext corrupted")

try:
    RA_key = int(RA_key)
    print('initial RA = ', RA_key)
except ValueError:
    print("Something is wrong, RA KEY is not an integer!")
    exit(1)

# then, calculate AES key1
AES_key1 = modular_exponentiation(RA_key, D, N)
print("AES key1 = ", AES_key1)
AES_key1 = str(AES_key1)
if len(AES_key1) != 16:
    print("something is wrong! AES key1 is not 16-bytes long!")
    exit(1)

AES_key1 = AES_key1.encode('utf-8')

# now, decrypt file!
with open("file_nonce", 'rb') as f:
    nonce = f.read()

with open("file_encoded", 'rb') as f2:
    ciphertext = f2.read()

with open("file_tag", 'rb') as f3:
    tag = f3.read()

cipher_2 = AES.new(AES_key1, AES.MODE_EAX, nonce=nonce)
plaintext = cipher_2.decrypt(ciphertext)

try:
    cipher_2.verify(tag)
    output = open("output.jpg", 'wb')
    output.write(plaintext)
    output.close()
except ValueError:
     print("Key incorrect or plaintext corrupted")