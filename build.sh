#!/bin/bash

jb build --all . &
git add . &
git commit -m $1 &
git push &
ghp-import -n -p -f _build/html