#!/bin/bash

usage() {
    echo "Usage: $0 --host HOSTNAME --timeout SECONDS" >&2
    exit 1
}

check_parameters() {
    if [[ $# != 2 ]] || ! [[ "$1" == "--host" ]] || ! [[ "$2" == "--timeout" ]]; 
    then
        usage
    fi
}

main() {
    check_parameters "$@"
    
    host="$1"
    timeout="$2"
    
    ping -c 4 -w "${timeout}" "${host}"
}

main "$@"


# HOSTNAME – это имя хоста, а SECONDS – количество секунд.