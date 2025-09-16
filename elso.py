import random

szamok = []
#100 elemu lista feltoltese 1-99 kozotti veletlenszamokkal
#..... szam generalas
for i in range(100):
    rszam = random.randint(1,100)
#szam elhelyezese a listaban
    szamok.append(rszam)

print(szamok)
# egyszamjatek
jatek_szam = 0
nem_talaltDB = 0

#kitalanando szam
kitalalando_szam = random.randint(1,100)