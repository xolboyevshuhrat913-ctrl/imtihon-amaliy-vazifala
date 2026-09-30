
matn = input("Sonlarni probel bilan ajratib kiriting: ")

try:
    sonlar = [float(x) for x in matn.split()]
except ValueError:
    print("Xato: faqat sonlarni kiriting!")
    raise SystemExit(1)

if not sonlar:
    print("Xato: hech qanday son kiritilmadi!")
    raise SystemExit(1)

eng_katta = max(sonlar)

eng_kichik = min(sonlar)

yigindi = sum(sonlar)

ortacha = yigindi / len(sonlar)


juft = 0
toq = 0
for son in sonlar:
    if son == int(son):
        if int(son) % 2 == 0:
            juft += 1
        else:
            toq += 1


print("\n" + "=" * 35)
print("        NATIJALAR")
print("=" * 35)
print(f"Sonlar ro'yxati   : {sonlar}")
print(f"Eng katta son     : {eng_katta}")
print(f"Eng kichik son    : {eng_kichik}")
print(f"Yig'indi          : {yigindi}")
print(f"O'rtacha qiymat   : {ortacha:.2f}")
print(f"Juft sonlar soni  : {juft}")
print(f"Toq sonlar soni   : {toq}")
print("=" * 35)
