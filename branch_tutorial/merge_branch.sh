#!/bin/bash
cd ../
git add .
#git commit -m "commit changes to branch"
git commit -m "commit changes to branch"
git branch -a
git checkout master
git merge demo
git push
