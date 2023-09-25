# tugaspostest
#Tugas postest david sebastian sutandy
import math
#saya menggunakan import math agar bisa melakukan operasi seperti sqrt untuk rumus pythagoras
def biodata():
#function biodata ini saya buat agar ketika kita salah input saya bisa memanggil function biodata ini dan bisa mengisi ulang datanya
    Nama_user = input("Masukkan nama user")
    NIM = input ("Masukkan NIM Mahasiswa (10 digit)")
    Password = input ("Masukkan password")
    #ini input biasa untuk memasukkan nama nim dan password
    Nama_user1 = ("david sebastian sutandy")
    Password1 = ("davidkeren")
    NIM_D = ("2309116041")
    #ini data yang harus diisi jika data yang diisi berbeda dengan ini, maka tidak bisa login
    if NIM == NIM_D and Nama_user == Nama_user1 and Password == Password1  :
        print ("Login berhasil")
        sisi()
        #ini kalau nim nama dan password benar maka login akan berhasil dan lanjut ke function buat hitungannya
    else :
        print ("NIM salah,silahkan login ulang")
        biodata()
        #jika input salah maka akan kembali ke input awal
def sisi():
#ini function buat hitungan, kalau kita input selain alas,tinggi,atau miring maka akan kembali ke sini
        print ("Masukkan sisi yang tidak diketahui (alas,tinggi,miring)")
        print ("ketik alas untuk mencari alas segitiga:")
        print ("ketik tinggi untuk mencari tinggi segitiga:")
        print ("ketik miring untuk mencari sisi miring segitiga:")
        #ini untuk bertanya pada user sisi apa yang ingin dicari
        sisis = input()
        #ini buat input 
        if sisis == "alas":
            tinggi1= float(input("masukkan tinggi segitiga:"))
            miring1= float(input("masukkan sisi miring segitiga:"))
            print ("Panjang alas segitiga adalah" , math.sqrt(miring1 ** 2 - tinggi1**2))
            # jika user memasukkan alas, maka operasi ini akan dijalankan dan saya menggunakan float agar user bisa memasukkan angka desimal dan ini juga kenapa saya menggunakan import math di awal, jika tidak import math dulu saya ga bisa menggunakan sqrt
        elif sisis == "tinggi":
            alas2 = float (input("masukkan alas segitiga:"))
            miring2 = float (input("masukkan sisi miring segitiga:")) 
            print ("Tinggi segitiga ini adalah" , math.sqrt(miring2**2 - alas2**2))
            #sama seperti  sebelumnya, tapi ini buat hitung tinggi jadi rumusnya ada yang beda
        elif sisis == "miring":
            alas3 = float(input("masukkan alas segitiga"))
            tinggi3 = float (input("masukkan tinggi segitiga"))
            print ("Panjang sisi miring segitiga ini adalah " , math.sqrt (alas3**2 + tinggi3**2))
            #sama juga kaya yang tadi tapi ini buat hitung sisi miring
        else:
            print ("Input salah silahkan masukkan sisi yang ingin dicari")
            sisi()
            #jika input user bukan alas,tinggi,atau miring maka ini akan memanggil function sisi untuk input ulang sisi yang ingin dicari
biodata()

#ini foto output untuk mencari alas
![image_2023-09-25_212921596](https://github.com/david123410/tugaspostest/assets/144750420/2126c72e-4352-4367-9462-88efce10e6f2)
#ini foto hasil output untuk mencari tinggi
![image_2023-09-25_213139357](https://github.com/david123410/tugaspostest/assets/144750420/543bd201-db40-4fab-8876-96327f1febb7)
#ini foto hasil output untuk mencari sisi miring 
![image_2023-09-25_213354188](https://github.com/david123410/tugaspostest/assets/144750420/cbc76786-171c-45a6-bf9a-c7e633ce843c)
#dari ketiga foto ini saya sudah ada tes dan rumusnya berhasil
#ini adalah outputnya kalau kita salah memasukkan data,disini saya tes kalau salah memasukkan nama,nim,dan password hasilnya login gagal dan kembali ke input nama user lagi
![image_2023-09-25_213558321](https://github.com/david123410/tugaspostest/assets/144750420/59da3ea8-808c-401d-8449-780a428bc525)
#dan ini adalah ketika kita menginput selain alas,tinggi atau miring, dia akan kembali ke function sisi dan kita disuruh input ulang
![image_2023-09-25_213845579](https://github.com/david123410/tugaspostest/assets/144750420/474454e0-84d6-4cce-a9ae-df45f5b2132f)

#ini foto flowchart yang saya buat
![Untitled Diagram drawio](https://github.com/david123410/tugaspostest/assets/144750420/b8842077-69ff-4f2f-bc9d-bc4dae1af0a3)

#Sekian dari saya, terima kasih 
