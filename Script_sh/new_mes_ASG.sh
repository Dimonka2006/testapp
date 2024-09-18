#!/bin/bash
set -e

grep "SUCCESS LOGIN" messages* | awk -F ' ' '{new_line=$6 FS "_" FS $3 FS $14 FS $15; print new_line}' | while read line; do
    IFS='_' read -ra ARR <<< "$line"
    echo "${ARR[1]}" | tr -d '' >> $(echo "logins_${ARR[0]}" | tr -d '')
done