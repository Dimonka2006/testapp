#!/bin/bash
if [ ! -d "archive" ]; then
  mkdir -pv archive
fi
pfile=$(find . -daystart -mtime +1 -name "*.csv" | sed 's|^./||')
mv $pfile archive 
cd archive
gzip *.csv