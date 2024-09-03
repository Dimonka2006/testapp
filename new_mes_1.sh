#!/bin/bash
set -e
cd /home/dus

cat messages | grep 'SUCCESS LOGIN' |cut -d " " -f7 && 
cat messages | grep 'SUCCESS LOGIN' |cut -d " " -f8 
cat messages | grep 'SUCCESS LOGIN' | cut -d " " -f11 > logins_date