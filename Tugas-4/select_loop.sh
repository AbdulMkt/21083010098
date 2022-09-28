#!/bin/bash

select minuman in teh kopi air jus susu semua gaada
do 
  case $minuman in 
    teh|kopi|air|semua)
     echo "maaf,  habis"
     ;;
    jus|susu)
      echo "tersedia"
    ;;
    gaada)
      break
    ;;
    *) echo "Tidak ada di daftar menu"
    ;;
  esac
done
