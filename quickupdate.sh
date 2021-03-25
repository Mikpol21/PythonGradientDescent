#!/bin/bash
msg="Quick meaningless update"
git add .
git status
git commit -m "$1"
git push origin main