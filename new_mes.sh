#!/bin/bash

touch logins_$(date +%Y%m%d)

pfile=$(find . -maxdepth 1 -name "message*" -printf "%f\n")

search_str=$(cat $pfile | grep 'SERVER: INFO - SUCCESS LOGIN by ')

if [[ -n $search_str ]]; then
    time_log=$(echo "$search_str" | cut -d " " -f7)
    date_log=$(echo "$search_str" | cut -d " " -f8)
    user_name_log=$(echo "$search_str" | cut -d " " -f14)
    user_famil_log=$(echo "$search_str" | cut -d " " -f15)
    echo -e "$time_log $date_log $user_log $user_famil_log" >> logins_$(date +%Y%m%d)
fi
