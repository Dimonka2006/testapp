#!/bin/bash 
set -e 
pfile=$(find . -maxdepth 1 -name "message*" -printf "%f\n") 
for name in $pfile
do
	while IFS= read stroka
	#search_str=$(cat $name | grep 'SERVER: INFO - SUCCESS LOGIN by ')
	#for stroka in $search_str
	do
		if echo "$stroka" | grep 'SERVER: INFO - SUCCESS LOGIN by '; then
			#echo "$stroka" 
			pole2=$(echo "$stroka" | cut -d " " -f2)
			#echo "$pole2"
			if ($pole2 -eq ""); then
				date_log=$(echo "$stroka" | cut -d " " -f6)
				echo "$stroka" | cut -d " " -f3,14,15 > logins_$data_log
			else
				date_log=$(echo "$stroka" | cut -d " " -f5)
				echo "$stroka" | cut -d " " -f2,13,14 > logins_$data_log
			fi
		fi
	done < "$name"
done