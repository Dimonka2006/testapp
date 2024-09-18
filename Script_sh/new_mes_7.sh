#!/bin/bash
set -e
pfile=$(find . -maxdepth 1 -name "message*" -printf "%f\n")
for name in $pfile
do
        while IFS= read stroka
        do
                if [[ $stroka == *"SERVER: INFO - SUCCESS LOGIN by"* ]]; then
                        pole2=$(echo "$stroka" | cut -d " " -f2)
                        if [[ $pole2 = "" ]]; then
                                date_log=$(echo "$stroka" | cut -d " " -f7)
                                #echo "$date_log"
                                echo "$stroka" | cut -d " " -f4,15,16 >> logins_$date_log
                        else
                                date_log=$(echo "$stroka" | cut -d " " -f6)
                                #echo "$date_log"
                                echo "$stroka" | cut -d " " -f3,14,15 >> logins_$date_log
                        fi
                fi
        done < "$name"
done