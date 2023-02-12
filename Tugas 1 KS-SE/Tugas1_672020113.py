priceTuple = (10000, 13000, 8000, 9000, 16000)
fruitTuple = ('mangga', 'apel', 'jeruk', 'semangka', 'anggur')

#Soal 1

i = 0
fruitDict = {}

for p in priceTuple :
    fruitDict[fruitTuple[i]] = priceTuple[i]
    i+=1

print("Soal 1 :")
print(fruitDict)

# ================================================
print("\n\n")
# ================================================

#Soal 2

totPrice = sum(fruitDict.values())
avePrice = totPrice / len(fruitDict.values())

print("Soal 2 :")
print(avePrice)

# ================================================
print("\n\n")
# ================================================



test_list = [4, 1, {'tiga': 3, 'tujuh': 7}, (9, 8, [2, 5]), 6]

#Soal 3

ls = []

for t in test_list :
    if isinstance(t, int) :
       ls.append(t)
    elif isinstance(t, dict) :
        x = list(t.values())
        for j in x :
            ls.append(j)
    elif isinstance(t, tuple) :
        for i in t :
            if isinstance(i, int) :
                ls.append(i)
            elif isinstance(i, list) :
                for j in i :
                    ls.append(j)

ls.sort()
# print(ls)
stringLs = ' '.join(str(i) for i in ls)

print("Soal 3 :")
print(type(stringLs))
print(stringLs)

# ================================================
print("\n\n")
# ================================================

#Soal 4

iLs = stringLs.split(' ')
intLs = []

for i in iLs :
    intLs.append(int(i))

print("Soal 4:")
print(intLs)

sumIntLs = sum(intLs)
print("Total : ")
print(sumIntLs)

# ================================================
print("\n\n")
# ================================================


str1 = "teknik informatika fakultas teknologi informasi universitas kristen satya wacana"
str2 = "sedang belajar bahasa pemrograman"
tupleMahasiswa = ('DEVA', 'IVAN')
dictKelas = {'IF001': 'Kapita Selekta', 'IF002': 'Matematika Diskrit', 'IF003': 'Pemrograman Web'}
listPython = ['p', 'y', 't', 'h', 'o', 'n']

#Soal 5
print("Soal 5:")


p1 = "Hari ini " + tupleMahasiswa[0].title() + " tidak mengikuti mata kuliah " + dictKelas['IF003']
print(p1)

idk = list(dictKelas)
p2 = dictKelas[idk[1]] + " " + idk[1] + " adalah salah satu mata kuliah di progdi " + str1[0:18].title() + str1[47:80].title()
print(p2)

python = ""
for i in listPython :
    python += i
p3 = tupleMahasiswa[1].title() + str2[6:33] + " " + python.title() + " di mata kuliah " + dictKelas['IF001']
print(p3)

# ================================================
print("\n\n")
# ================================================

listHari = ['Senin', 'Rabu', 'Jumat', 'Sabtu']
#Soal 6
print("Soal 6:")

listHari.insert(1, 'Selasa')
listHari.insert(3, 'Kamis')
listHari.insert(6, 'Minggu')

print(listHari)

# ================================================
print("\n\n")
# ================================================

#Soal 7
print("Soal 7:")

listHari.pop(5)
listHari.pop(5)

lh = tuple(listHari)

print(lh)



