from os import getpid
from time import time,sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
   if (i+1)%2==0:
      print(i+1, "genap  - ID Process", getpid())
   else:
     print(i+1, "ganjil - ID Process", getpid())
   sleep(1)

n=int(input("Masukkan Batasan :"))

print("\n")
#SEKUENSIAL
sekuensial_awal = time()
print("Sekuensial")
for i in range(n):
   cetak(i)
sekuensial_akhir=time()
print("\n")
#MULTIPROCESSING DENGAN KELAS PROCESS
process_awal=time()
print("Multiprocess.process")
for i in range(n):
    p=Process(target=cetak, args=(i, ))
    p.start() 
    p.join()
process_akhir=time()
print("\n")
#MULTIPROCESSING DENGAN KELAS POOL
pool_awal=time()
pool = Pool()
print("Multiprocess.pool")
pool.map(cetak,range(0,n))
pool.close()
pool_akhir=time()
print("\n")
#BANDINGKAN WAKTU EKSEKUSI
print("Perbandingan waktu")
print("Sekuensial:", sekuensial_akhir - sekuensial_awal, "detik")
print("Kelas Process:", process_akhir - process_awal, "detik")
print("Kelas Pool:", pool_akhir - pool_awal, "detik")
print("\n")
print("\n")
print("\n")
print("\n")
