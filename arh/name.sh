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