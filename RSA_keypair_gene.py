from Cryptodome.PublicKey import RSA

keys = RSA.generate(2048) # seems to be private key
f = open('keys.pem', 'wb')
f.write(keys.exportKey('PEM'))
f.close()

# print(keys.exportKey(format='PEM'))
# print(pk.exportKey(format='PEM'))
#
# with open ("private.pem", "w") as prv_file:
#     print("{}".format(keys.exportKey()), file=prv_file)
#
# with open ("public.pem", "w") as pub_file:
#     print("{}".format(pk.exportKey()), file=pub_file)
# print(pk)
# print(f'pk: (n={hex(pk.n)}, e={hex(pk.e)})')
# pkPem = pk.exportKey()
# print(pkPem.decode('ascii'))

# print(f"Private key: (n={hex(pk.n)}, d={hex(keys.d)})")
# skPEM = keys.exportKey()
# print(skPEM.decode('ascii'))

# pk_n = open('pk_n', 'wb')
# pk_n.write(pk.n)
# pk_n.close()
#
# pk_e = open('pk_e', 'wb')
# pk_e.write(pk.e)
# pk_e.close()
#
# pk_d = open('pk_d', 'wb')
# pk_d.write(pk.d)
# pk_d.close()