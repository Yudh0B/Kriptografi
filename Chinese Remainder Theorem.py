def Xterkecil(a, b, k):
    p = 1
    for i in range(0, k):
        p = p * a[i]
    hasil = 0

    for i in range(0, k):
        pp = p // a[i]
        hasil = hasil + b[i] * invers(pp, a[i]) * pp

    return hasil % p

def invers(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if (m == 1):
        return 0

    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if (x1 < 0):
        x1 = x1 + m0
    return x1

# x = 3 mod 2
# x = 4 mod 3
# x = 5 mod 1
#format matrix
a = [3, 4, 5, 7, 11]
b = [2, 3, 1, 2, 2]
k = len(a) #fleksibel mengikuti jumlah operasi yang dibutuhkan
print("x adalah ", Xterkecil(a, b, k))