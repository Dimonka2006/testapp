#!/bin/bash
set -e


pfile=$(find . -maxdepth 1 -name "message*" -printf "%f\n")
for name in $pfile
do

search_str=$(cat $name | grep 'SERVER: INFO - SUCCESS LOGIN by ')

if [[ -n $search_str ]]; then


for i in $search_str


do
echo $i

    date_log=$(echo '$i' | cut -d " " -f6)
    echo $data_log
    #echo $i | cut -d " " -f3,14,15 > logins_$file_data
    #touch logins_$date_log

    done

fi
done