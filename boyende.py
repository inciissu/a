boy  = float(input('Lütfen boyunuzu "metre" cinsinden giriniz...'))
kilo = float(input('Lütfen kilonuzu "kilogram" cinsinden giriniz...'))
vki = round (kilo / boy ** 2)
if vki < 18.5:
  print(f"Vücut kitle indeksiniz: {vki}, zayıfsınız")
elif vki < 25:
  print(f"Vücut kitle indeksiniz: {vki}, kilonuz normal")
elif vki < 30:
  print(f"Vücut kitle indeksiniz: {vki}, kilonuz biraz fazla")
elif vki < 35:
  print(f"Vücut kitle indeksiniz: {vki}, 1. derece obezsiniz")
elif vki < 40:
  print(f"Vücut kitle indeksiniz: {vki}, 2. derece obezsiniz")
else:
  print(f"Vücut kitle indeksiniz: {vki}, 3. derece obezsiniz.")