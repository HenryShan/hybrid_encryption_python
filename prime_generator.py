import numpy as np
import random as rd

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

# print(modular_exponentiation(3292213, 41, 100))

# generate random prime number p and q in range [0, 100]
# def isPrime(i):
#     if i > 1:
#         for x in range(2, i):
#             if (i % x) == 0:
#                 return 0
#         return 1
#     else:
#         return 1
#
# all_primes = []
# for i in range(10000, 100001):
#     if isPrime(i):
#         all_primes.insert(0, i)
#
# p = rd.choice(all_primes)
# all_primes.remove(p)
# q = rd.choice(all_primes)
# print('p = ', p, ' q = ', q)
# prime_pair = str(p)+','+str(q)
# prime = open("prime.txt", 'w')
# prime.write(prime_pair)
# prime.close()


# a = 'MIIEpQIBAAKCAQEAtXimGO3OIgLgiipm0YqJVvAopYpohv/dN4QEKVDZY/sd/Buw' \
#     'Q5Hi4NnIbkBfNv4Z0GyLLYQkk7sPWxgF53Pz6Zopd28G/sXi0mQZWqlX+x859m11' \
#     'kZp48vT+JZNiHYkWBs79dJcw6Hws+l4T4Wkhjrn4XYkiwY45J1WmzLfqnnLbrE/5' \
#     'iXzaXIRXjy0E/pRVyBT6ZvJ327FyoVOxkDeVovdksKX1GOvQi9WGpTvVlUNJKxas' \
#     'I71P/ZyUguzJMuk/Vc1XZz/EV5OXqGGbyK0FKHuzr0F9KbHAbzTBj5fF9Lb/fOtW' \
#     'KkSGLgmGsGPT1XYWDRXfWDaV9+G0FKUjXriWKQIDAQABAoIBAQCKfmlE3ThT/J4g' \
#     '0/tkL7ZhAygCLn9XiC3sEHSck3dVNnDL1tXOu6fKsmqkubvw3DwXNL+DHTZNCJXP' \
#     'j6Xx3ixoO58p5zIPfjZ9Gqe+6T6cCFjUGPWBCcMEqLTNOI3IvLZyu8XzFO/efeZV' \
#     'rTa+8N0LcCJ8QAyma0RzIIsL8dC82uDJWkogPj7/d14YZz8kiFrQQTenHz9hlQr6' \
#     'r+aE2tenl9d/U4XPjmwyyXT4qYZRi6HwWzkhxwyKWRPCHRDIiRYB3gR76VG0egNi' \
#     'Pcn2MMcVCjsZfYfW6Zv3Gstn2aCb6KeXy6gdj0pfF6ozAvupqLVmMjpm307QYjm/' \
#     'MacufMYBAoGBAO8Ue3k8bdXyF2PeVFyGVPleK1YMfSPdAMztCmpqRFi6kZRyUl5R' \
#     'LMXUEJKSzOAE6GQlfjvLYIXSuBXxGxnA/dhUuGjhauZxZCEreBxt/RPpHLS9iJM6' \
#     '33pXKdQ5gZo7vdYVJ9TVHS544PpusX2qGTPKg9UU4SH9U+BmkYrK9LB9AoGBAMJQ' \
#     'caM3O2hWfil/Bw2hUd9RXWY8NEVp3cnSHy2nqbcUtG+na/eQHmNSHDZlJ2OnhWEx' \
#     'gUvV/JK34onlQ7+hnPSf2m1TUHTsL4EnPsSyqwrusu+xZDqTVq5sRtxJ8MivQy0B' \
#     'oCCmmaAxIpqdg5T/xeBh0JqYXytXK6qP4ZuwPngdAoGBAJmLhAlG4BupkZAYOAH8' \
#     'XBKTgi2Pc8dWpq72Bdx2R1Lc76ZxDal5ZNHg8ovQMDgnrsCyu7HXWjRYMtYUtR0D' \
#     'L4SCVLU3IJrDdFVBP7CyivkAm+kQWOiFxQUjeb/M9wmBGNinWZ99B3LTO1pbQS69' \
#     '0dXLWIO/Fx/nPLk/5nVHB4NZAoGBAJUax2hX7IUuwZaz+8SQwlNbixD1J6MQDnlc' \
#     'fEI7QrbS83YuAWIxO7A5BJ8U1bnZhTbElxOLO0mWQwZPX8I/kEICG8kCQl3GEtnH' \
#     'NJoZA7ja24GkHGX6Q2yKd4F4V4SXQDPb6HTFgmLy8Tu1nI+MCNoaFMlcHMMUG9TA' \
#     'nX0rK3RdAoGAO1MNBjFuVpIDec9mv5+xSrANnV1oOU7h7JGpTo5zitQDlARZGQPA' \
#     'zeDN/2ACuEI1PqQc9sR8jsQTKCXpyrW/gkYJZYlhn0UhTvaesK/3aAurD3zgYySl' \
#     'w+rLD+l1sXVt8pjCFeZK4GWb0lGmr7bmxoGr2AJCbUNuAF+nHK2L8ZM='
#
# b = 'AAAAB3NzaC1yc2EAAAADAQABAAABAQC1eKYY7c4iAuCKKmbRiolW8CilimiG/903hAQpUNlj+x38G7BDkeL' \
#     'g2chuQF82/hnQbIsthCSTuw9bGAXnc/' \
#     'Ppmil3bwb+xeLSZBlaqVf7Hzn2bXWRmnjy9P4lk2IdiRYGzv10lzDofCz6XhPhaSGOufhdiSLBjjknVabMt' \
#     '+qectusT/mJfNpchFePLQT+lFXIFPpm8nfbsXKhU7GQN5Wi92SwpfUY69CL1YalO9WVQ0krFqwjvU/' \
#     '9nJSC7Mky6T9VzVdnP8RXk5eoYZvIrQUoe7OvQX0pscBvNMGPl8X0tv9861YqRIYuCYawY9PVdhYNFd9YNp' \
#     'X34bQUpSNeuJYp'
#
# a2 = 'AAAAB3NzaC1yc2EAAAADAQABAAABAQDWQorkCbWOR5T/WZ2zmAdB05/iwF6JD76yl3ppAsR17hEl/' \
#      'NMuSRbgy+I9HM+vYUWITYtPmuDZ2AvjBuZHE5AaZCSF5T42NofavVf8KgK29gU4FGHT8IfhWX2qEswTSrbI' \
#      'jq0vYnv5M6Cbz3stXzNZk4kuzoeD9wcbNfj4GY6WBL9zeC94pfF/a/' \
#      'IwwVuhcwSP5qdZ12KlSQpdANq5dzz+esuYZQxU8CECVWq4hxn1pdxvcpA0+Lg/' \
#      'NSa+DsDJoybemsFAzzRtGe16UtlDQTlIrpqFLfOzwS9CLuXfsHaPuPlJ708Q3VvQUM+D/' \
#      '+gDpLJtpoQlLGOMUBTOtSK35jqR'
#
# # c = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxzYuc22QSst/dS7geYYK5l5kLxU0tayNdixkEQ17ix+CUcUbKIsnyftZxaCYT46rQtXgCaYRdJcbB3hmyrOavkhTpX79xJZnQmfuamMbZBqitvscxW9zRR9tBUL6vdi/0rpoUwPMEh8+Bw7CgYR0FK0DhWYBNDfe9HKcyZEv3max8Cdq18htxjEsdYO0iwzhtKRXomBWTdhD5ykd/fACVTr4+KEY+IeLvubHVmLUhbE5NgWXxrRpGasDqzKhCTmsa2Ysf712rl57SlH0Wz/Mr3F7aM9YpErzeYLrl0GhQr9BVJxOvXcVd4kmY+XkiCcrkyS1cnghnllh+LCwQu1sYwIDAQAB'
# print(len(c))