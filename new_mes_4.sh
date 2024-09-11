#!/bin/bash
set -e
if [ ! -f "temp" ]; then
  rm -f temp
fi
pfile=$(find . -maxdepth 1 -name "message*" -printf "%f\n")
for name in $pfile
do

cat $name | grep 'SERVER: INFO - SUCCESS LOGIN by ' >> temp
done

search_str=$(cat temp)

for i in $search_str


do
echo $i

    date_log=$(echo '$i' | cut -d " " -f6)
    echo $data_log
    #echo $i | cut -d " " -f3,14,15 > logins_$file_data
    #touch logins_$date_log

done

fi