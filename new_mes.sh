#!/bin/bash
set -e

touch logins_{date +%Y%m%d}

pfile=$(find . -maxdepth 1 -name "message*" -printf " %f\n ")

search_str=$(cat $pfile | grep 'SUCCESS LOGIN')

time_log=$($search_str | cut -d " " -f7)
date_log=$($search_str | cut -d " " -f8)
user_log=$($search_str | cut -d " " -f15)

# time_log=$(cat messages | grep 'SUCCESS LOGIN' | cut -d " " -f7)
# date_log=$(cat messages | grep 'SUCCESS LOGIN' | cut -d " " -f8)
# user_log=$(cat messages | grep 'SUCCESS LOGIN' | cut -d " " -f15)

echo "$time_log $date_log $user_log" >> logins_{date +%Y%m%d}


