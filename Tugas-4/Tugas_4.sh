#!/bin/bash
echo -e "\n "
echo -e "\033[1;36m Pencetak perulangan bilangan ganjil\033[0m\n"
echo "Batas harus bilangan ganjil"
echo -n "Masukkan batas : "
read batas
echo -e "\n"
mod=$(($batas % 2))

if [ $mod == 0 ]
then 
	echo -e "\033[1;31m $batas bukan bilangan ganjil\033[0m\n"
	echo -n "Masukkan batas lagi : "
	read batas
	echo -e "\n"
fi
echo "Output : $batas"
a=0
until [ ! $batas -gt $a ]
do
  echo $batas
  batas=$((batas-2))
done

