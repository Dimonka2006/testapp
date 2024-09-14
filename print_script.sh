#!/bin/bash
# подсчитываю кол-во входных переменных
# если не равно 2 пишет ошибку и закрывает программу
if [[ $# != 2 ]] ; then
    echo "Usage: $0 --host HOSTNAME --timeout SECONDS" >&2
    exit 1
fi

if [[ "$1" == "--host" && "$3" == "--timeout" ]] ; then
    shift
    shift
    # shift убирает первый и второй аргументы из списка 
   
    host="$1"
    timeout="$1"
else
    echo "Неверный формат параметров." >&2
    exit 1
fi

ping -c 4 -w "${timeout}" "${host}"

#./ping_script.sh --host HOSTNAME --timeout SECONDS
# HOSTNAME – это имя хоста, а SECONDS – количество секунд.