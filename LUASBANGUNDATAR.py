def Luas_persegi(sisi):
  return sisi ** 2

def Luas_Persegi_Panjang(panjang, lebar):
  return panjang * lebar

def Luas_Segitiga(alas, tinggi):
  return 0.5 * alas * tinggi

def Luas_Lingkaran(jari_jari):
  import math
  return math.pi * jari_jari ** 2
  

def main():
  print("Sebelum itu kita kenalan dulu yuk, tulis dulu nama kamu dibawah ini yaa")
  orang = input("Tulis nama kamu: ")

  print()

  print(f"Allo {orang} saya Ekoo ")
  print("Saya suka main EFEF, oshi saya charlotte😁")

  print()

  print(f"Yaudah deh kalo gitu  {orang}")
  print("Aku bisa bantu kamu menghitung luas bangun datar lohh")

  print()

  print("Daftar luas bangun yang saya bisa bantu hitung :v")
  print("ketikan mau nomor berapa yaa")
  print("misal 1/2/3/4")
  print("1) Luas lingkaran")
  print("2) Luas segitiga")
  print("3) Luas persegi panjang")
  print("4) Luas persegi")
  
print()

  pilih = int(input("Mau ngitung luas apa nih kira-kira🤔: "))
  print(f"Allo {orang} ini aku kasih contoh angka yang dimasukan yaaa:")
  print("Contoh : 12 ")
  print

  if pilih == 4:
    sisi = int(input("Masukkan sisinya: "))
    print(f"Luas persegi = {Luas_persegi(sisi)}")
    print(f"Kapan-kapan lagi {orang}:v")

  elif pilih == 3:
    panjang = int(input("Masukkan Panjangnya: "))
    lebar = int(input("Masukkan Lebarnya: "))
    print(f"Luas Persegi Panjangnya = {Luas_Persegi_Panjang(panjang, lebar)}")
    print(f"Kapan-kapan lagi {orang}:v")

  elif pilih == 2:
    alas = int(input("Berapa nih Alasnya? : "))
    tinggi = int(input("Kalo Tingginya? : "))
    print(f"Nih kukasih tau Luas Segitiganya= {Luas_Segitiga(alas, tinggi)}")
    print(f"Kapan-kapan lagi {orang}:v")

  elif pilih == 1:
    jari_jari = int(input(" Berapa nih Jari-Jarinya? : "))
    print(f"Nih kukasih tau Luas Lingkarannya = {Luas_Lingkaran(jari_jari):.2f}")
    print(f"kapan-kapan lagi {orang}:v")

if __name__ == "__main__":
  main()