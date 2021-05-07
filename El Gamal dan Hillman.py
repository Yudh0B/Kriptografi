#no. 1
print("1.")
g=4
n=7
x=3
y=4
A=((g**x) % n)
B=((g**y) % n)
K=((B**x) % n)
Ka=((A**y) % n)
print("Hasil perhitungan no. 1 : ")
print("A = " + str(A))
print("B = " + str(B))
print("K = " + str(K))
print("K' = " + str(Ka))
if K == Ka :
    print("Enkripsi dan Dekripsi Berhasil")
else :
    print("Enkripsi dan Dekripsi Gagal")
print("")
#no. 2
print("2.")
g=653
n=5471
x=9
y=11
A=((g**x) % n)
B=((g**y) % n)
K=((B**x) % n)
Ka=((A**y) % n)
print("Hasil perhitungan no. 2 : ")
print("A = " + str(A))
print("B = " + str(B))
print("K = " + str(K))
print("K' = " + str(Ka))
if K == Ka :
    print("Enkripsi dan Dekripsi Berhasil")
else :
    print("Enkripsi dan Dekripsi Gagal")
print("")
#no. 3
print("3.")
#enkripsi
p=11
g=2
x=8
me=5
k=9
a=((g**k) % p)
y=((g**x) % p)
b=(((y**k)*me) % p)
#dekripsi
c=[a,b]
m=((c[1]*(c[0]**(p-1-x))) % p)
#hasil perhitungan
print("Hasil perhitungan no. 3 : ")
print("a = " + str(a))
print("b = " + str(b))
print("y = " + str(y))
print("c = " + str(c))
print("m = " + str(m))
if m == me :
    print("Enkripsi dan Dekripsi Berhasil")
else :
    print("Enkripsi dan Dekripsi Gagal")
print("")
#no. 4
print("4.")
#enkripsi
p=397
g=1
x=140
me=181
k=45
a=((g**k) % p)
y=((g**x) % p)
b=(((y**k)*me) % p)
#dekripsi
c=[a,b]
m=((c[1]*(c[0]**(p-1-x))) % p)
#hasil perhitungan
print("Hasil perhitungan no. 4 : ")
print("a = " + str(a))
print("b = " + str(b))
print("y = " + str(y))
print("c = " + str(c))
print("m = " + str(m))
if m == me :
    print("Enkripsi dan Dekripsi Berhasil")
else :
    print("Enkripsi dan Dekripsi Gagal")
print("")
#no. 4
print("5.")
#enkripsi
p=557
g=300
x=34
me=103
k=206
a=((g**k) % p)
y=((g**x) % p)
b=(((y**k)*me) % p)
#dekripsi
c=[a,b]
m=((c[1]*(c[0]**(p-1-x))) % p)
#hasil perhitungan
print("Hasil perhitungan no. 5 : ")
print("a = " + str(a))
print("b = " + str(b))
print("y = " + str(y))
print("c = " + str(c))
print("m = " + str(m))
if m == me :
    print("Enkripsi dan Dekripsi Berhasil")
else :
    print("Enkripsi dan Dekripsi Gagal")