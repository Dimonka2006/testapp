#!/bin/bash
set -e
echo "Hello, $USER!"
echo "Today is $(date)"
echo "begin starting babah system"

#to create backup directory
cd /home/programfid/app/
if [ ! -d "backup" ]; then
mkdir -pv backup
echo "create backup directory"
fi

#let's create a backup copy
source_dir="/home/programfid/app"
backup_dir="/home/programfid/app/backup"
timestamp=$(date +"%Y-%m-%d-%H-%M")
dfile=$(find . -maxdepth 1 -name "*.sh" -printf " %f " -o -name "*.py" -printf " %f ")
#| sed 's|^./||') 
# 2 way
backup_file="$timestamp.tar.gz"
echo $dfile
echo $backup_dir
echo $backup_dir/$backup_file
tar -czvf $backup_dir/$backup_file $dfile
#find $backup_dir -name "*.tar.gz" -mtime +10 -exec rm {} \;
