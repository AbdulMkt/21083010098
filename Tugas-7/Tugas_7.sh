#!/bin/bash
# Mendeklarasikan fungsi

Luaspersegi() {
 panjang
 printf "\n"
 lebar
 printf "\n"
 echo "Luas Persegi :"
 let luas=$panjang*$lebar
 echo "$luas"
}

panjang() {
 echo "Masukkan Panjang :"
 read panjang
}

lebar() {
 echo "Masukkan Lebar :"
 read lebar
}

# Memanggil fungsi
Luaspersegi
