#!/bin/bash
set -e
echo "Hi, what's your name?"
read NAME

if NAME=""

[ -n $NAME ]; then

    echo "$USER is empty"
else
    echo "$NAME is not empty"
fi

#выложить на сервер backup скрипт
scp -P 22 backup_deploy.sh $NAME@srv503956.hstgr.cloud:/home/programfid/app

#добавление прав на исполнение и запуск выложеного скрипта на сервере
ssh $NAME@srv503956.hstgr.cloud 'cd /home/programfid/app && sudo chmod 774 backup_deploy.sh && sudo chmod +x backup_deploy.sh && ./backup_deploy.sh'

# перенос всех библиотек
dfile=$(find . -maxdepth 1 -name "*.sh" -printf " %f " -o -name "*.py" -printf " %f ")
scp -P 22 $dfile $NAME@srv503956.hstgr.cloud:/home/programfid/app

#переименование всех файлов на programfid и добавление полномочий
ssh $NAME@srv503956.hstgr.cloud 'cd /home/programfid/app && sudo chown -R programfid:programfid ./'
d_sh=$(find . -maxdepth 1 -name "*.sh" -printf " %f ")
ssh $NAME@srv503956.hstgr.cloud 'cd /home/programfid/app && sudo chmod 774 $d_sh && sudo chmod +x $d_sh'

#Остановка сервиса
#Обновить конфигурацию systemd:
#Добавить сервис в автозагрузку и запустить его:

ssh $NAME@srv503956.hstgr.cloud 'sudo systemctl stop app.service && sudo systemctl daemon-reload'
ssh $NAME@srv503956.hstgr.cloud 'sudo systemctl enable app.service && sudo systemctl start app.service'
#sudo systemctl status app.service

exit 0