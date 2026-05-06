import socket
import time

baslangic = time.time()

hedef = socket.gethostbyname(input("Hedef (IP veya site): "))

for port in range(1, 1025):
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    sonuc = soket.connect_ex((hedef, port))

    if sonuc == 0:
        print(f"Port {port} AÇIK")

    soket.close()

bitis = time.time()
print("Tarama süresi:", bitis - baslangic)
