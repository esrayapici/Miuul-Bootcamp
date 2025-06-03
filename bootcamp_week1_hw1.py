text = "The goal is to turn data into information, and information into insight."
buyukharftext = text.upper()
print(buyukharftext)

lst = ["D","A","T","A","S","C","I","E","N","C","E"]
print(lst)
print(len(lst))
print(lst[0],lst[10])
print(lst[0:4])
print(lst.pop(8))
print(lst)
print(lst.append(4))
print(lst)
print(lst.insert(8,'N'))
print(lst)

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}
dict.keys()
print(dict.keys())
dict.values()
print(dict.values())
dict['Daisy']= ["England",13]
dict.values()
print(dict.values())
dict.update({'Ahmet':["Turkey",24]})
dict.values()
print(dict.values())
del dict['Antonio']
print(dict)

l = [2,13,18,93,22]


def ayir_tek_cift(liste):
        teksayilar = []
        ciftsayilar = []
        for sayi in liste:
                if (sayi % 2 ==0):
                        ciftsayilar.append(sayi)
                else:
                        teksayilar.append(sayi)
        return(teksayilar,ciftsayilar)
print(ayir_tek_cift(l))

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

print("Mühendislik Fakültesi Başarı Sıralaması:")
for i, ogr in enumerate(ogrenciler[:3], 1):
    print(f"{i}. {ogr}")

print("\nTıp Fakültesi Başarı Sıralaması:")
for i, ogr in enumerate(ogrenciler[-3:], 1):
    print(f"{i}. {ogr}")

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

print("Ders Bilgileri:")
for kod, kr, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Ders Kodu: {kod} | Kredi: {kr} | Kontenjan: {kont}")

def kume_karsilastir(kume1, kume2):
    if kume1.issuperset(kume2):  # kume1, kume2'yi kapsıyor mu?
        ortak = kume1.intersection(kume2)
        print("1. küme 2. kümeyi kapsıyor. Ortak elemanlar:", ortak)
    else:
        fark = kume2.difference(kume1)
        print("1. küme 2. kümeyi kapsamıyor. 2. kümenin 1. kümeden farkı:", fark)

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

kume_karsilastir(kume1, kume2)


