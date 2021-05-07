import math
import random

E = []
p = 29
q = 31
n = p * q
l = (p - 1) * (q - 1)
for e in range(0, 100):
    boolTestA = math.gcd(e, p - 1)
    boolTestB = math.gcd(e, q - 1)
    boolTestC = math.gcd(e, l)
    print("e = " + str(e))
    print("gcd e dan p-1= " + str(boolTestA))
    print("gcd e dan q-1= " + str(boolTestB))
    print("gcd e dan l  = " + str(boolTestC))
    if (boolTestA == 1 and boolTestB == 1) and boolTestC == 1:
        E.append(e)
print(E)
# random item from list
e = (random.choice(E))
print("nilai e= " + str(e))
k = 0
for k in range(1, 200):
    d = (1 + (k * l)) / e
    print(d)
    if d % 2 == 1.0:
        break

print(d)
m = "SURYA"
M = []
C = []
ME = []
for character in m:
    M.append(ord(character))
print(M)
for m in M:
    c = ((m**e) % n)
    C.append(c)
print("hasil enkripsi= ")
print(C)
#for c in C:
#    mE = ((c**d) % n)
#    ME.append(mE)
#print("hasil dekripsi= ")
#print(ME)