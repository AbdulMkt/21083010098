import os
import time
import random

print("+=======================================================+")
print("|   SELAMAT DATANG DI GAME TEBAK ANGKA DAN HANGMAN      |")
print("+=======================================================+")
nama = input("Silahkan Masukkan nama anda :") # pemain diminta memasukkan nama

def main(): # main sebagai pengatur alur pembukaan permainnan
    os.system('clear') # menghapus output sebelumnya 
    print("+=======================================================+")
    print("|   SELAMAT DATANG DI GAME TEBAK ANGKA DAN HANGMAN      |")
    print("+=======================================================+")
    print("                   HALLO", nama.upper(),"                 ") #memanggil variabel nama dan di buat kapital(upper)
    print("+=======================================================+")
    print("|                    MENU UTAMA                         |")# memilih game
    print("+=======================================================+")
    print("| 1. TEBAK ANGKA                                        |")
    print("| 2. HANGMAN                                            |")
    print("| 3. Exit Program                                       |")
    print("+=======================================================+")
    pil=int(input("Masukkan pilihan menu [1-3] : "))
    if pil==1: # jika memasukkan pilihan 1 akan masuk ke game tebak_anngka
        os.system("clear")
        tebak_angka(nama)
    elif pil==2: # jika memasukkan pilihan 2 akan masuk ke game HANGMAN 
        os.system("clear")
        hangman()
    elif pil==3: # jika memasukkan pilihan 3 akan mengakhiri game 
        os.system('clear')
        print('[SAMPAI JUMPA]')
        time.sleep(1.5)
        os.system('clear')
        exit()
    else: # jika memasukkan pilihan selain pilihan 1,2 dan 3 akan terjadi error dan proses main akan diulang kembali
        os.system('clear')
        print('[Pilihan tidak valid]')
        time.sleep(1.5)
        os.system('clear')
        main()

def main_menu(): # main menu digunakan untuk memberi pilihan untuk main kembali atau mau keluar
    ulang = input('\n                Main Lagi ??(Y/T)\n').upper()
    if ulang == "Y": # jika "Y" maka proses akan kembali ke main()
        main() 
    elif ulang== "T":  # jika "T" maka akan mengakhiri game dan keluar
        os.system('clear')
        print('[SAMPAI JUMPA]')
        time.sleep(1.5)
        os.system('clear')
        exit()
    else: # jika memasukkan pilihan selain pilihan "Y" dan "T"akan terjadi error dan proses main_nenu akan diulang kembali
        os.system('clear')
        print('[Pilihan tidak valid]')
        time.sleep(1.5)
        os.system('clear')
        main()

def tebak_angka(nama):
    while(True): # perulangan untuk memperoses game tebak angka
        os.system('clear')
        print("+=========================================================+")
        print("                    HALLO", nama.upper(),"                 ")
        print("+=========================================================+")
        print("+=========================================================+")
        print("|           SELAMAT DATANG DI GAME TEBAK ANGKA            |")
        print("+=========================================================+")
        print("|Petunjuk! :                                              |")
        print("|1.Angka yang diberikan adalah tanggal hari libur nasional|")
        print("|  tahun 2022,Angka tersebut akan dirandom                |")
        print("|2.Anda diminta untuk menebak angkan tersebut             |")
        print("|3.Percobaan yang diberikan sebanyak 5 kali               |")
        print("+=========================================================+")
        jawab = input('\n                   MULAI (Y/T)\n').upper() # disini di beri pilihan Y/T
        if jawab == "Y": # jika Y akan mulai memasuki game
            os.system("clear")
            print("+=======================================================+")
            print("|                     TEBAK ANGKA                       |")
            print("+=======================================================+")
            print("\nContoh angka: 1,15,27,31")
            
            tgl = [1,28,3,15,29,2,4,5,6,16,26,10,30,17,8,25]
            random_angka = random.choice(tgl) # merandom tgl yang selanjutnya tgl yang terpilih akan ditebak
            
            batas_percobaan = 5 # batas percobaan yang diberikan
            
            for percobaan in range(batas_percobaan): # akan dilakukan perulangan sebanyak batas_percobaan 
                try: 
                    jawaban = int(input(f'\n[Percobaan ke-{percobaan + 1}] Masukkan angka: ')) # disuruh memasukkan jawaban dan setiap jawaban akan +1 percobaan
                    if jawaban == random_angka: # jika tebakan benar makan akan mencetak seperti outpu dibawah ini
                        print("+=======================================================+")
                        print("|           *       *       *  *  * *    *              |")
                        print("|            *     * *     *   *  *  *   *              |")
                        print("|             *   *   *   *    *  *   *  *              |")
                        print("|              * *     * *     *  *    * *              |")
                        print("|               *       *      *  *     **              |")
                        print("+=======================================================+")
                        print('               Selamat, tebakanmu benar!')
                        print("+=======================================================+")
                        main_menu() # jika sudah selesai game akan di kembalikan ke main_menu
                    elif jawaban < random_angka: # jika tebakan lebih kecil dari angka yang diberikan maka akan mencetak output seperti dibawahh ini
                        print("Angka yang anda masukkan terlalu kecil")
                        
                    elif jawaban > random_angka : # jika tebakan lebih besar dari angka yang diberikan maka akan mencetak output seperti dibawahh ini
                        print("Angka yang anda masukkan terlalu besar")
                except ValueError: # error handling jika input type int bukan int
                    print("Mohon masukkan angka :)")
                    continue # melanjutkan game
                   

            else: # jika percobaan sudah habis akan mencetak output seperti dibawah ini
                print("+=======================================================+")
                print("|        * * * * * * * *  * * * * * * *  * * * *        |")
                print("|        *       *     *  *     *     *  *              |")
                print("|        * * * * * * * *  *     *     *  * * * *        |")
                print("|        *     * *     *  *     *     *  *              |")
                print("|        * * * * *     *  *     *     *  * * * *        |")
                print("|         * * * *  *       *  * * * *  * * * *          |")
                print("|         *     *  *       *  *        *     *          |")
                print("|         *     *   *     *   * * * *  * * * *          |")
                print("|         *     *    *   *    *        * *              |")
                print("|         * * * *      *      * * * *  *    *           |")
                print("+=======================================================+")
                print("|         Kesempatan yang diberikan telah habis         |")
                print("          Jawaban yang benar adalah tanggal", random_angka)
                print("+=======================================================+")
                main_menu() # jika sudah selesai game akan di kembalikan ke main_menu
        

        elif jawab == "T": # jika T maka kembali ke main menu
            main_menu() 

        else: # jika jawabnnya selain Y/T maka akan terjadi eror
            os.system('clear')
            print('[Pilihan tidak valid]')
            time.sleep(1.5)
            os.system('clear')
            continue # digunakan untuk melanjutkan perulangan game tebak angka
    
        break # berhenti
        
def hangman():
    while(True):
        os.system('clear')
        print("+=========================================================+")
        print("                    HALLO", nama.upper(),"                 ")
        print("+=========================================================+")
        print("+=========================================================+")
        print("|             SELAMAT DATANG DI GAME HANGMAN              |")
        print("+=========================================================+")
        print("|Petunjuk! :                                              |")
        print("|1.Kata yang ditebak merupakan nama bulan  dalam kalender |")
        print("|2.nama bulan tersebut akan dirandom                      |")
        print("|2.Anda diminta untuk menebak nama bulan tersebut dengan  |")
        print("| menebah setiap hurufnya satu-persatu                    |")
        print("|3.Percobaan yang diberikan sebanyak 5 kali               |")
        print("+=========================================================+")
        jawab = input('\n                   MULAI (Y/T)\n').upper()
            
        if jawab == "Y":
            os.system("clear")
            print("+=======================================================+")
            print("|                        HANGMAN                        |")
            print("+=======================================================+")
            global count
            time.sleep(1) # menjeda proses selama 1 detik
            print ("Mulai Game......")
            time.sleep(0.5)# menjeda proses selama 1 detik
            # word ini berisi nama bulan yang dirandom yang selanjutnya akan terpilih salah satu buat di tebak 
            word = random.choice(["januari","februari","maret","april","mei","juni","juli","agustus","september","oktober","november","desember"])
            # membuat variabel guesses yang berisi nilai kosong
            guesses = '' # variabel kosong untuk menyimpan setiap karakter tebakan
            count= 0
            kesempatan = 5 # jumlah kesempatan menebak yang diberikan
            while kesempatan > 0: # mengecek setiap kesempatan
                failed = 0 # kesempatan dimuali dari 0     
                for char in word:  # untuk karakter yang terdapat di word
                    if char in guesses: # mengecek jika karakter ada di guesss
                        print (char,end=""), # maka akan mencetak karakter 
                    else: # jika karakter tidak ada di dalam guess
                        print ("_",end=""),   # maka akan tetap mencetak "_" tanpa mencetak karakter
                        failed += 1    # dan tingkat kegagalan ditambah satu
                        
                if failed == 0:    # jika kegagalan =0 makan akan mencetak 
                    print("\n+=======================================================+")
                    print("|           *       *       *  *  * *    *              |")
                    print("|            *     * *     *   *  *  *   *              |")
                    print("|             *   *   *   *    *  *   *  *              |")
                    print("|              * *     * *     *  *    * *              |")
                    print("|               *       *      *  *     **              |")
                    print("+=======================================================+")
                    print('               Selamat, tebakanmu benar!')
                    print("+=======================================================+")
                    main_menu() # jika sesesai akan di bawa kembali ke main_menu
                    break
                print
                guess = input("Masukkan karakter yang menurut anda sesuai :".lower())
               #alur game tebakan
                guesses += guess                    
                if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
                    print("Karakter yang anda masukkan tidak falid, silahka masukkan lagi..!\n")
                    continue
                
                if guess not in word: # jika tebakan karakter tidak sesuai yang ada di guesses maka
                    count += 1 # count akan bertambah satu sampai count = kesempatan 
                    if count == 1: # jika count =1 maka akan mencetak seperti dibawah ini dan setiap kesempatan akan dikurangi count
                        time.sleep(1)
                        print("\n")
                        print("+=======================================================+")
                        print("|        * * * * * * * *  * * * * * * *  * * * *        |")
                        print("+=======================================================+")
                        print("\n")
                        print("Tebakan salah. " + str(kesempatan - count) + "nyawa tersisa\n")

                    elif count == 2:# jika count = 2 maka akan mencetak seperti dibawah ini dan setiap kesempatan akan dikurangi count
                        time.sleep(1)
                        print("\n")
                        print("+=======================================================+")
                        print("|        * * * * * * * *  * * * * * * *  * * * *        |")
                        print("|        *       *     *  *     *     *  *              |")
                        print("|        * * * * * * * *  *     *     *  * * * *        |")
                        print("|        *     * *     *  *     *     *  *              |")
                        print("+=======================================================+")
                        print("\n")
                        print("Tebakan salah. " + str(kesempatan - count) + "nyawa tersisa\n")

                    elif count == 3: # jika count = 3 maka akan mencetak seperti dibawah ini dan setiap kesempatan akan dikurangi count
                        time.sleep(1)
                        print("\n")
                        print("+=======================================================+")
                        print("|        * * * * * * * *  * * * * * * *  * * * *        |")
                        print("|        *       *     *  *     *     *  *              |")
                        print("|        * * * * * * * *  *     *     *  * * * *        |")
                        print("|        *     * *     *  *     *     *  *              |")
                        print("|        * * * * *     *  *     *     *  * * * *        |")
                        print("|         * * * *  *       *  * * * *  * * * *          |")
                        print("+=======================================================+")
                        print("\n")
                        print("Tebakan salah. " + str(kesempatan - count) + "nyawa tersisa\n")

                    elif count == 4: # jika count = 4 maka akan mencetak seperti dibawah ini dan setiap kesempatan akan dikurangi count
                        time.sleep(1)
                        print("\n")
                        print("+=======================================================+")
                        print("|        * * * * * * * *  * * * * * * *  * * * *        |")
                        print("|        *       *     *  *     *     *  *              |")
                        print("|        * * * * * * * *  *     *     *  * * * *        |")
                        print("|        *     * *     *  *     *     *  *              |")
                        print("|        * * * * *     *  *     *     *  * * * *        |")
                        print("|         * * * *  *       *  * * * *  * * * *          |")
                        print("|         *     *  *       *  *        *     *          |")
                        print("|         *     *   *     *   * * * *  * * * *          |")
                        print("|         *     *    *   *    *        * *              |")
                        print("+=======================================================+")
                        print("\n\n")
                        print("Tebakan salah. " + str(kesempatan - count) + "nyawa tersisa\n")

                    elif count == 5: # jika count = 5 maka akan mencetak seperti dibawah ini dan setiap kesempatan akan dikurangi count
                        time.sleep(1)
                        print("\n")
                        print("+=======================================================+")
                        print("|        * * * * * * * *  * * * * * * *  * * * *        |")
                        print("|        *       *     *  *     *     *  *              |")
                        print("|        * * * * * * * *  *     *     *  * * * *        |")
                        print("|        *     * *     *  *     *     *  *              |")
                        print("|        * * * * *     *  *     *     *  * * * *        |")
                        print("|         * * * *  *       *  * * * *  * * * *          |")
                        print("|         *     *  *       *  *        *     *          |")
                        print("|         *     *   *     *   * * * *  * * * *          |")
                        print("|         *     *    *   *    *        * *              |")
                        print("|         * * * *      *      * * * *  *    *           |")
                        print("+=======================================================+")
                        print("|         Kesempatan yang diberikan telah habis         |")
                        print("          Jawaban yang benar adalah ", word)
                        print("+=======================================================+")
                        main_menu() # jika sesesai akan di bawa kembali ke main_menu
                
        elif jawab == "T": # jika "T" maka akan kembali ke main_menu
            main_menu() 

        else: # jika memasukkan pilihan selain pilihan "Y" dan "T"akan terjadi error dan proses akan diulang kembali
            os.system('clear')
            print('[Pilihan tidak valid]')
            time.sleep(1.5)
            os.system('clear')
            continue
        break
    
    
    

main() # memanggil main untuk memulai proses 






