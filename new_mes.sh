#!/bin/bash
set -e

pfile=$(find -name "messages * " -type f)

search_str=$(cat $pfile | grep 'SUCCESS LOGIN')

$search_str | cut -d " " -f7 && echo " " && 
$search_str | cut -d " " -f8 && echo " " && 
$search_str | cut -d " " -f11 > logins_date