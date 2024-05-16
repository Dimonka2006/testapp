#!/bin/bash
set -e
echo "Hello, $USER!"
echo "Today is $(date)"
echo "begin starting babah system"

#to create backup directory

if [ ! -d "backup" ]; then
  mkdir -pv backup
echo "create backup directory"
fi

#let's create a backup copy

source_dir="/home/programfid/app/"
backup_dir="/home/programfid/app/backup/"
timestamp=$(date +"%Y-%m-%d-%h-%m-%s")
dfile=$(find . -maxdepth 1 -type f -name "*.sh" -o -name "*.py" | sed 's|^./||')
# | sed 's/ /\t/g' {} | cut -f 2
#find . -name "*.sh" -o -name "*.py" -exec ls -f '{}' \+
backup_file="$timestamp_$dfile.tar.gz"
echo $dfile
tar -czvf "$backup_dir/$backup_file" "$dfile"
#find $backup_dir -name "*.tar.gz" -mtime +10 -exec rm {} \;
