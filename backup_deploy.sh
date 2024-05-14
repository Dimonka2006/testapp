#!/bin/bash
set -e
echo "Hello, $USER!"
echo "Today is $(date)"
echo "begin starting babah system"

#to create backup directory

if [ ! -d "backup" ]; then
  mkdir -pv backup
fi

#let's create a backup copy

source_dir="/home/programfid/app/"
backup_dir="/home/programfid/app/backup/"
fdate=$(date +"%Y-%m-%d-%h-%m")
dfile=$(find . -maxdepth 1 -type f -name "*.sh" -o -name "*.py")
bfile="$fdate_$dfile.tar.gz"
echo $dfile
#tar -czvf "$backup_dir/$bfile" "$dfile"
#find $backup_dir -name "*.tar.gz" -mtime +10 -exec rm {} \;
tar -czvf "/home/programfid/app/backup/"/"date +"%Y-%m-%d-%h-%m"_find -type f -name "*.sh" -o -name "*.py".tar.gz" "find -type f -name "*.sh" -o -name "*.py"

backup_deploy.sh (END)

