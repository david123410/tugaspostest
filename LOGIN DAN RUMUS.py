import math
def biodata():
    Nama_user = input("Masukkan nama user")
    NIM = input ("Masukkan NIM Mahasiswa (10 digit)")
    Password = input ("Masukkan password")
    Nama_user1 = ("david sebastian sutandy")
    Password1 = ("davidkeren")
    NIM_D = ("2309116041")
    if NIM == NIM_D and Nama_user == Nama_user1 and Password == Password1  :
        print ("Login berhasil")
        sisi()
    else :
        print ("NIM salah,silahkan login ulang")
        biodata()
def sisi():
        print ("Masukkan sisi yang tidak diketahui (alas,tinggi,miring)")
        print ("ketik alas untuk mencari alas segitiga:")
        print ("ketik tinggi untuk mencari tinggi segitiga:")
        print ("ketik miring untuk mencari sisi miring segitiga:")
        sisis = input()
        if sisis == "alas":
            tinggi1= float(input("masukkan tinggi segitiga:"))
            miring1= float(input("masukkan sisi miring segitiga:"))
            print ("Panjang alas segitiga adalah" , math.sqrt(miring1 ** 2 - tinggi1**2))
        elif sisis == "tinggi":
            alas2 = float (input("masukkan alas segitiga:"))
            miring2 = float (input("masukkan sisi miring segitiga:")) 
            print ("Tinggi segitiga ini adalah" , math.sqrt(miring2**2 - alas2**2))
        elif sisis == "miring":
            alas3 = float(input("masukkan alas segitiga"))
            tinggi3 = float (input("masukkan tinggi segitiga"))
            print ("Panjang sisi miring segitiga ini adalah " , math.sqrt (alas3**2 + tinggi3**2))
        else:
            print ("Input salah silahkan masukkan sisi yang ingin dicari")
            sisi()
biodata()