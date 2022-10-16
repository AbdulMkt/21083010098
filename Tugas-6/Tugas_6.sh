#!/bin/bash
echo -e "\n"
echo -e "\033[1;36m IPK MAHASISWA\033[0m\n"
echo -n "Masukkan Banyak Semester yang telah diikuti : "
read r

declare -a IPSMahasiswa

i=0
let p=$r-1

while [ $i -le $p ];
do
  let t=$i+1
  printf "Masukkan IP Semester %.1i : " $t;
  read ip;
  IPSMahasiswa[$i]=$ip;
  let jumlah=jumlah+$ip;
  let i=$i+1;
done

let IPK=$jumlah/$r
echo "nilai per semester" ${IPSMahasiswa[@]}
echo "Nilai IPS:" $jumlah "/" $r
echo "Nilai IPK:" $IPK
