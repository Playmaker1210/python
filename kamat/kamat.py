betet = 10000
kamatlab = 0.08
kamatozasok = 12
t = input()

szamolas = betet * (1 + kamatlab / kamatozasok) ** (kamatozasok * t)
print(szamolas)
