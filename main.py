SM = [[4, 252], [8, 248], [16, 240], [32, 224], [64, 192], [128, 128]]
MASK = "255.255.255."

# bekérjük az alhálózatokat

alhalozat_hossza = []
MAX_HALOZAT_HOSSZ = 256
MAX_ALHALOZAT_SZAMA = 64

alhalozatok_szama = int(input("Hány alhálózatod lesz? "))
while not (alhalozatok_szama <= MAX_ALHALOZAT_SZAMA):
    alhalozatok_szama = int(input("Hiba! Hány alhálózatod lesz (MAX: 64)? "))

for i in range(alhalozatok_szama):
    jelenlegi_nagysag = int(input(f"{i+1}. Alhálózat nagysága: "))
    while not (jelenlegi_nagysag >= 2):
        jelenlegi_nagysag = int(input(f"Hiba! {i+1}. Alhálózat nagysága (nagyobb, mint 1): "))

    alhalozat_hossza.append(jelenlegi_nagysag)

# sorba rendezzük

alhalozat_hossza.sort()
alhalozat_hossza.reverse()


# hálózat cím (és a 0 levétele a végéről)

halozat_pont0 = input("Hálózat címe: ")
halozat = ""
for i in range(len(halozat_pont0) - 1):
    halozat += halozat_pont0[i]


# számítás

nw = []
m = []
h1 = []
hn = []
bc = []

for i in range(len(alhalozat_hossza)):
    for j in range(len(SM)):
        if alhalozat_hossza[i] + 2 <= SM[j][0]:
            if i == 0:
                nw.append(0)
                m.append(SM[j][1])
                h1.append(1)
                hn.append(nw[i] + SM[j][0] - 2)
                bc.append(nw[i] + SM[j][0] - 1)
                break
            else:
                nw.append(bc[i - 1] + 1)
                m.append(SM[j][1])
                h1.append(nw[i] + 1)
                hn.append(nw[i] + SM[j][0] - 2)
                bc.append(nw[i] + SM[j][0] - 1)
                break

    print(f"{alhalozat_hossza[i]} - alhálózat:\n"
          f"\tN: {halozat}{nw[i]}\n"
          f"\tM: {MASK}{m[i]}\n"
          f"\tH1: {halozat}{h1[i]}\n"
          f"\tHn: {halozat}{hn[i]}\n"
          f"\tBc: {halozat}{bc[i]}")
