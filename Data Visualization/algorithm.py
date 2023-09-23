values = [1, 3, 5, 2, 2]
toplam = 0


def ilerisiniDonder(index):
    deger = 0
    for number in range(index, len(values)):
        deger += values[number]
    return deger


def gerisiniDonder(index):
    deger = 0
    for number in range(0, index):
        deger += values[number]
    return deger


for number in range(0, len(values)):
    toplam += values[number]
for number in range(1, len(values)):
    deger = toplam
    deger -= values[number]
    deger = deger / 2
    if deger == gerisiniDonder(number):
        if deger == ilerisiniDonder(number + 1):
            print(f"Orta nokta {number} ve deger {int(deger)}")
            break
