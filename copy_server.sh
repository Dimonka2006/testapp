#!/bin/bash
set -e
#выложить на сервер backup скрипт
scp -P 22 backup_deploy.sh dus@srv503956.hstgr.cloud:/home/programfid/app
#запуск выложеного скрипта на сервере 
ssh dus@srv503956.hstgr.cloud 'bash -s' < "cd /home/programfid/app && ./backup_deploy.sh"
#выложить программы и базы на сервер 
#scp -r directory user@remote_host[:dest_dir] если копировать директорию
# rsync -nva dir user@host:dest_dir или через службу rsunc для передачи всей иерархии каталогов, 
# включая символические ссылки, права доступа, режимы и устройства, используйте параметр -a
scp -P 22 test_prog.sh dus@srv503956.hstgr.cloud:/home/programfid/app
#переименование всех файлов на programfid
ssh dus@srv503956.hstgr.cloud 'bash -s' < "cd /home/programfid/app && sudo chown -R programfid:programfid ./"
#Остановка сервиса
sudo systemctl stop app.service
#Обновить конфигурацию systemd:
sudo systemctl daemon-reload
#Добавить сервис в автозагрузку и запустить его:
sudo systemctl enable app.service
sudo systemctl start app.service
#Проверьте что сервис запущен:
sudo systemctl status app.service

exit 0