#!/bin/bash
set -e

touch logins_{date +%Y%m%d}

pfile=$(find . -maxdepth 1 -name "message*" -printf " %f\n ")

search_str=$(cat $pfile | grep 'SUCCESS LOGIN')

time_log=$($search_str | cut -d " " -f7)
date_log=$($search_str | cut -d " " -f8)
user_log=$($search_str | cut -d " " -f14)

echo "$time_log $date_log $user_log" >> logins_{date +%Y%m%d}

done

