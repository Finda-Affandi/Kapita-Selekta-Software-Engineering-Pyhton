def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            return False
    return True

def primeList(x, y):
    primeNum = []
    for i in range(x, y + 1):
        if prime(i):
            primeNum.append(i)
    return primeNum

print("Soal 1")
print(primeList(2, 9))




