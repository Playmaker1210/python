nap = int(input("0 és 6 kozott"))
eltelt_napok = int(input("Eltelt napok szama"))

napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

def milyen_nap(nap, eltelt_napok):
    print(napok[nap])
    nap += eltelt_napok
    nap %= 7
    return napok[nap]

print(milyen_nap(nap, eltelt_napok))