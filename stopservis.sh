#!/bin/bash
set -e
stopscript=$(ps aux | grep "flask run" | grep -v grep | cut -d " " -f7)
echo $stopscript
for i in $stopscript;do
echo $i
kill -9 $i
echo "Stopping proces"
done