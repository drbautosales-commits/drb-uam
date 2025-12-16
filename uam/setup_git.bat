@echo off
chcp 65001
git init
git remote add origin https://github.com/drbautosales-commits/drb-uam.git
git add .
git commit -m "Initial commit: UAM project files"
git branch -M main
git push -u origin main
pause

