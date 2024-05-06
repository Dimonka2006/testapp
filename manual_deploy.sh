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
timestamp =$(date +%Y% m%d%H%M%S)
backup_file="backup_$timestamp.tar.gz"
tar -czvf"$backup_dir/$backup_file""$source_dir"
