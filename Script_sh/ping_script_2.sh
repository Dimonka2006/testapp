#!/bin/bash

			        
host="$1"
timeout="$2"
ping -w "${timeout}" "${host}"

# ping -w 5 google.com

# ./ping_script_2.sh 5 example.com