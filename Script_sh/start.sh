#!/usr/bin/bash

log=log-$(date +"%Y-%m-%d")
#cd /home/programfid/app; nohup ./run.sh >> ./logs/$log &2>1 &
cd /home/programfid/app && source ./venv/bin/activate && flask run
start.sh (END)