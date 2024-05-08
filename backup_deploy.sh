#!/bin/bash
echo "Hello, $USER!"
echo "Today is $(date)"
echo "begin starting babah system"

#to create backup directory
cd /home/programfid/app/
if [ ! -d "backup" ]; then
  mkdir -pv backup
fi

#let's create a backup copy
source_dir="/home/programfid/app/"
backup_dir="/home/programfid/app/backup/"
timestamp=$(date +%Y% m%d%H%M%S)
file=$(find . -maxdepth 1 -type f -name "*.sh" -o -name "*.py")
backup_file="$timestamp_backup_$file.tar.gz"
tar -czvf"$backup_dir/$backup_file""$source_dir"

backup_deploy.sh (END)

