#!/bin/bash

msg="Quick meaningless update"
if [ -z "$1" ]; then
    msg=$1
fi
echo -e "\e[35m\tAdding\e[0m"
git add .
echo -e "\e[35m\tStatus:\e[0m"
git status
echo -e "\e[35m\tCommiting:\e[0m"
git commit -m "msg"
echo -e "\e[35m\tPushing:\e[0m"
git push origin main
echo -e "\e[34m\tDone\e[0m"