#!/bin/bash
echo "Hello, $USER!"
echo "Today is $(date)"
echo "begin starting babah system"

#let's create a backup copy
source_dir="/etc/systemd/system/"
backup_dir="/home/programfid/app/archive"
timestamp =$(date +%Y% m%d%H%M%S)
backup_file="backup_$timestamp.tar.gz"
tar -czvf"$backup_dir/$backup_file""$source_dir"
