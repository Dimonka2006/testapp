#!/bin/bash
# подсчитываю кол-во входных переменных
# если не равно 2 пишет ошибку и закрывает программу
if [[ $# != 2 ]] ; then
    echo "Usage: $0 --host HOSTNAME --timeout SECONDS" >&2
    exit 1
fi

if [[ "$1" == "--host" && "$2" == "--timeout" ]] ; then
   
    host="$1"
    timeout="$2"
else
    echo "Введен неверный формат параметров." >&2
    exit 1
fi

ping -c 4 -w "${timeout}" "${host}"

# ./ping_script_1.sh 5 example.com 

# HOSTNAME – это имя хоста, а SECONDS – количество секунд.