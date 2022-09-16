#!bin/bash
echo -n "masukkan nama anda : "
read nama
clear
echo -e "Hallo $nama\nselamat dataang di operasi matematika sederhana\n"
echo "Keterangan operator berupa simbol sesuai yang tertera dibawah ini"
echo "Penjumlahan (+)"
echo "Pengurangan (-)"
echo "Perkalian (x)"
echo -e "Pembagian (\)\n"

echo "Masukkan operator angka yang ingin anda operasikan : "
echo -n "masukkan operator: "
read c

if [ $c = + ]
then
echo -e "\nAnda Memasuki Operator Penjumlahan"
echo -n "masukkan angka ke-1: "
read a
echo -n "masukkan angka ke-2: "
read b
echo "$a $c $b = `expr $a + $b`"
echo -e "\nJadi hasil dari $a $c $b adalah `expr $a + $b`"

elif [ $c = - ]
then
echo -e "\nAnda Memasuki Operator Pengurangan"
echo -n "masukkan angka ke-1: "
read a
echo -n "masukkan angka ke-2: "
read b
echo "$a $c $b = `expr $a - $b`"
echo -e "\nJadi hasil dari $a $c $b adalah `expr $a - $b`"

elif [ $c = / ]
then
echo -e "\nAnda Memasuki Operator Pembagian"
echo -n "masukkan angka ke-1: "
read a
echo -n "masukkan angka ke-2: "
read b
echo "$a $c $b = `expr $a / $b`"
echo -e "\nJadi hasil dari $a $c $b adalah `expr $a / $b`"

elif [ $c = x ]
then
echo -e "\nAnda Memasuki Operator Perkalian"
echo -n "masukkan angka ke-1: "
read a
echo -n "masukkan angka ke-2: "
read b
echo "$a $c $b = `expr $a \* $b`"
echo -e "\nJadi hasil dari $a $c $b adalah `expr $a \* $b`"
fi

