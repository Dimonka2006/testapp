#!/bin/bash
set -e

pfile=$(find . -maxdepth 1 -name "message*" -printf "%f\n")
for name in $pfile; do
    search_str=$(cat "$name" | grep 'SERVER: INFO - SUCCESS LOGIN by ')
    for stroka in $search_str; do
        pole2=$(echo "$stroka" | cut -d " " -f2)
        if [[ "$pole2" == "" ]]; then
            date_log=$(echo "$stroka" | cut -d " " -f6)
            echo "$stroka" | cut -d " " -f3,14,15 > logins_"$date_log".log
        else
            date_log=$(echo "$stroka" | cut -d " " -f5)
            echo "$stroka" | cut -d " " -f2,13,14 > logins_"$date_log".log
        fi
    done
done

