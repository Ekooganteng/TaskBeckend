def tambah(x, y):
  return x + y

def kurang(x, y):
  return x - y

def kali(x, y):
  return x * y

def bagi(x, y):
  if y == 0:
    print("Gada jawabannya bang😠😠")
  else:
    return x / y

print("Allo kamu🤗 ")
print("Sebelum ke halaman berikutnya kenalan dulu ya abangku🔥🔥🔥")
Abangku = (input("Tulis nama abangku🔥🔥: "))

print()

print(f"allo {Abangku} saya Ekoo😁")
print("Saya suka main EFEF,oshi saya charlotte😱😱")

print ()

print("Pilih salah satu aja yaa🥰: ")
print("1. boleh pertambahan")
print("2. boleh pengurangan")
print("3. boleh perkalian")
print("4. boleh pembagian")
opsi = (input("terserah dah mau yang mana aja boleh🤨 (1/2/3/4): "))

print()

bilangan1= float(input("Berapa nih bilangan pertamanya: "))
bilangan2 = float(input("Berapa nih bilangan keduanya: "))

print()

if opsi == '1':
  print(f"Hasil Perjumlahan Dari {bilangan1} + {bilangan2} = ", tambah(bilangan1, bilangan2), "😁") 

elif opsi == '2':
  print(f"Hasil Pengurangan Dari {bilangan1} - {bilangan2} = ", kurang(bilangan1, bilangan2), "😁")

elif opsi == '3':
  print(f"Hasil Perkalian Dari {bilangan1} × {bilangan2} = ", kali(bilangan1, bilangan2), "😁")

elif opsi == '4':
  print(f"Hasil Pembagian Dari {bilangan1} / {bilangan2} = ", bagi(bilangan1, bilangan2), "😁")

else:
  print(f"Onde Mande,{Abangku}")
  print("Pilih yang bener dong 😡😡 (1/2/3/4) ")