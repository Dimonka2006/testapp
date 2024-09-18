#!/bin/bash
set -e

if [ ! -f "temp" ]; then
rm -f temp
fi

pfile=$(find . -maxdepth 1 -name "message*" -printf "%f\n")
cat $pfile | grep 'SERVER: INFO - SUCCESS LOGIN by ' >> temp

while IFS= read stroka

do
pole2=$(echo "$stroka" | cut -d " " -f2)

if [[ $pole2 = "" ]]; then
date_log=$(echo "$stroka" | cut -d " " -f7)
echo "$stroka" | cut -d " " -f4,15,16 >> logins_$date_log

else
date_log=$(echo "$stroka" | cut -d " " -f6)
echo "$stroka" | cut -d " " -f3,14,15 >> logins_$date_log

fi
done < "temp"

rm -f temp