#!/bin/bash
set -e


pfile=$(find . -maxdepth 1 -name "message*" -printf "%f\n")

search_str=$(cat $pfile | grep 'SERVER: INFO - SUCCESS LOGIN by ')

if [[ -n $search_str ]]; then
    date_log=$(echo "$search_str" | cut -d " " -f7)
    touch logins_$date_log
    echo "$search_str" | cut -d " " -f3,14,15 >> logins_$date_log
fi