#!/bin/bash
cd /home/programfid/app/
if [ ! -d "archive" ]; then
  mkdir -pv archive
fi
pfile=$(find . -daystart -mtime +1 -name "*.csv" | sed 's|^./||')
mv $pfile /archive 
cd /home/programfid/app/archive
gzip *.csv