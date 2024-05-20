##!/bin/bash
set -x
#выложить на сервер
scp -P 22 backup_deploy.sh dus@srv503956.hstgr.cloud:/home/programfid/app
ssh dus@srv503956.hstgr.cloud 'bash -s' < cd /home/programfid/app ./backup_deploy.sh


exit 0