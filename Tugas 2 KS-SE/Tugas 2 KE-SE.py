# =====================Soal 1=====================
def prima(x):
    if x < 2:
        return False
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            return False
    return True

def primaList(x, y):
    primaNum = []
    for i in range(x, y + 1):
        if prima(i):
            primaNum.append(i)
    return primaNum

print("Soal 1")
print(primaList(2, 9))


# =====================Soal 2=====================

def ganjil(x) :
    if x%2 == 0 :
        return False
    return True

def ganjilList(x, y) :
    ganjilNum = []
    for i in range(x, y + 1) :
        if ganjil(i) :
            ganjilNum.append(i)
    return ganjilNum

print("\nSoal 2")
print(ganjilList(2,13))


# =====================Soal 3=====================


def primaGanjil(x, y):
    primaNum = []
    for i in range(x, y + 1):
        if prima(i):
            if i % 2 != 0 :
                primaNum.append(i)
    return primaNum

print("\nSoal 3")
print(primaGanjil(3, 17))


# =====================Soal 4=====================

def reverseStr(x) :
    y = []
    yRev = []
    for i in x :
        y.append(i)
    for j in y :
        yRev = [j] + yRev
    result = ''.join(str(i) for i in yRev)
    return result

print("\nSoal 4")
print(reverseStr("Salatiga"))


# =====================Soal 5=====================

def palindrome(x) :
    reverse = reverseStr(x)
    if x == reverse :
        return True
    else :
        return False

print("\nSoal 5")
print(palindrome("kasur ini rusak"))
print(palindrome("yahaha"))


# =====================Soal 6=====================


def selisih(x) :
    selisihNum = max(x) - min(x)
    return selisihNum

listNum = [77,44,90,45,30]
print("\nSoal 6")
print(selisih(listNum))


# =====================Soal 7=====================


def alphabet(x) :
    vokal = []
    kons = []
    for i in x :
        if i.isalpha() :
            if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                vokal.append(i)
            else:
                kons.append(i)

    huruf = (vokal, kons)
    return huruf


print("\nSoal 7")
print(alphabet("indonesia"))


# =====================Soal 8=====================


def search(x, y) :
    sch = {}
    for i in x :
        if i == y :
            sch["status"] = True
            sch["index"] = x.index(i)
            break
        else:
            sch["status"] = False
    return sch

print("\nSoal 8")
print(search(listNum, 45))


# =====================Soal 9=====================



def aritmatika(opr, x = 1, y =1) :
    hasil = 0
    try :
        if opr == '+' :
            hasil = x + y
            return hasil
        elif opr == '-' :
            hasil = x - y
            return hasil
        elif opr == '*' :
            hasil = x * y
            return hasil
        elif opr == '/' :
            if y == 0 :
                raise ZeroDivisionError("Tidak bisa dibagi dengan angka 0!")
            else:
                hasil = x / y
                return hasil
        else :
            raise ValueError("Operator tidak dikenali, gunakan '+', '-', '*', '+'")
    except ZeroDivisionError as error :
        print(error)
    except ValueError as error :
        print(error)


print("\nSoal 9")
print(aritmatika('/', 7, 6))



# =====================Soal 10=====================



print("\nSoal 10")
import volume



print("- Kubus : ", volume.kubus(5))

print("\n- Balok : ", volume.balok(3, 5, 7))

print("\n- Limas Segi-4 : ", volume.limas4(11, 13, 19))

print("\n- Prisma Segi-3 : ", volume.prisma3(2, 4, 6))