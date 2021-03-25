#!/bin/bash
msg="Quick meaningless update"
if [ -z "$1" ]; then
    msg=$1
fi
git add .
git status
git commit -m "$1"
git push origin main