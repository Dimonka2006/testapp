##!/bin/bash
set -e
#выложить на сервер backup скрипт
scp -P 22 backup_deploy.sh dus@srv503956.hstgr.cloud:/home/programfid/app
#запуск выложеного скрипта на сервере 
ssh dus@srv503956.hstgr.cloud 'bash -s' < cd /home/programfid/app ./backup_deploy.sh
#выложить программы и базы на сервер 
scp -P 22 test_prog.sh dus@srv503956.hstgr.cloud:/home/programfid/app
#поиск и переименование всех файлов dus на programfid
ssh dus@srv503956.hstgr.cloud 'bash -s' < find ./home/programfid/app -user dus | chown programfid {}

#Обновить конфигурацию systemd:
sudo systemctl daemon-reload
#Добавить сервис в автозагрузку и запустить его:
sudo systemctl enable app.service
sudo systemctl start app.service
#Проверьте что сервис запущен:
sudo systemctl status app.service

exit 0