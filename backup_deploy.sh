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
timestamp=$(date +"%Y-%m-%d-%h-%m-%s")
dfile=$(find . -maxdepth 1 -type f -name "*.sh" -o -name "*.py")
backup_file="$timestamp_$dfile.tar.gz"
echo $dfile
tar -czvf "$backup_dir/$backup_file $dfile"
#find $backup_dir"*.tar.gz" -mtime +10 -exec rm {} \;

backup_deploy.sh (END)

