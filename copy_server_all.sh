##!/bin/bash
set -e
echo "Hi, what's your name?"
read NAME
echo "my name is $NAME"
#выложить на сервер backup скрипт
scp -P 22 backup_deploy.sh $NAME@srv503956.hstgr.cloud:/home/programfid/app
#добавление прав на исполнение и запуск выложеного скрипта на сервере

ssh $NAME@srv503956.hstgr.cloud 'cd /home/programfid/app && sudo chmod 774 backup_deploy.sh && sudo chmod +x backup_deploy.sh && ./backup_deploy.sh'

#запуск выложеного скрипта на сервере 
#ssh $NAME@srv503956.hstgr.cloud 'cd /home/programfid/app && ./backup_deploy.sh'
#выложить программы и базы на сервер 
#scp -r directory NAME@remote_host[:dest_dir] если копировать директорию
# rsync -nva dir NAME@host:dest_dir или через службу rsunc для передачи всей иерархии каталогов, 
# включая символические ссылки, права доступа, режимы и устройства, используйте параметр -a

scp -P 22 test_prog.sh $NAME@srv503956.hstgr.cloud:/home/programfid/app
#переименование всех файлов на programfid

ssh $NAME@srv503956.hstgr.cloud 'cd /home/programfid/app && sudo chown -R programfid:programfid ./'
#Остановка сервиса
#sudo systemctl stop app.service
#Обновить конфигурацию systemd:
#sudo systemctl daemon-reload
#Добавить сервис в автозагрузку и запустить его:
#sudo systemctl enable app.service
#sudo systemctl start app.service
#Проверьте что сервис запущен:
#sudo systemctl status app.service
ssh $NAME@srv503956.hstgr.cloud 'sudo systemctl stop app.service && sudo systemctl daemon-reload'
ssh $NAME@srv503956.hstgr.cloud 'sudo systemctl enable app.service && sudo systemctl start app.service'
exit 0