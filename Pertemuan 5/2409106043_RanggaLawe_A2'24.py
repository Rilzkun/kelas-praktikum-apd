# nama= ["cello", "shandy", "farel", "ghazali", "vito","yuyun", "adri", "rizal","ifnu"]
# matkul= ["apd", "apl", "basdat","strukdat", "web","jarkom"]
# print(type,[nama])
# print(nama[2:5])

# data= nama+matkul

# print("sebelum")
# print(nama)
# print("")
# print("sesudah")
# print(data)
# print(data*3)
# nama.append("rizal")
# nama.insert(2, "riya")
# print(nama)
# nama[4]= "fufufafa"
# del nama[2]
# hapus = nama.pop(2)
# print(nama)
# print(hapus)

# print(nama[0:2])
# print(nama[2:4])
# print(nama[1:9])
# print(nama[1:9:2])

# data= ["farel", "celio",[1,2,["halo",23,2,3,True]]]
# print(data[2][2][0])

# print(data[-1])

# matkul= [1,2,3,4,[5,6,7]]
# print(matkul[4])
# print(matkul[4][3])

# matkul= [1,2,3,4]

# for i in matkul:
#     # print(i)
#     print(i, end="-")

# matkul= [[1,2,3],[4,5,6],[7,8,9]]

# for i in matkul:
    # print(i)
    # for j in i:
    #     print(j)

# nama= ("cello", "shandy", "farel", "ghazali", "vito","yuyun")
# print(nama:1 )

# mahasiswa=(69, "informatika", "2309106043", "aldy")
# absen,prodi,nim=mahasiswa
# print(nim)

# print(
# """
# ==================
# data mahasiswa
# ==================

# 1. tambah data
# 2. tampilkan data
# 3. ubah data
# 4. hapus data
# 5. keluar

# ==================
# """)
# data_mahasiswa=[]
# while true:
#     pilih= int(input("pilih: "))
#     if pilih == 1:
#         nama= input(nama: )
#         nim=input(nim: )
#         kelas=input(kelas: )
#         data_mahasiswa.append([nama,nim,kelas])
#     elif pilih == 2:
#         for data in data_mahasiswa:
#             for i in range(len(data)):
#                 print(f"\n data mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i]}\nNIM : ")
     
#     elif pilih == 3:

#     elif pilih == 4:
#     elif pilih == 5:

print( 
"""
===========================
|   DATA MAHASISWA A24    |
===========================
|    1. TAMBAH DATA       |           
|    2. TAMPILKAN DATA    |          
|    3. UBAH DATA         |     
|    4. HAPUS DATA        |      
|    5. KELUAR            |  
===========================
"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")




