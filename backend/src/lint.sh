#!/bin/zsh 
# This script is used to lint the codebase

for files in 'backtester' 'aoStrategy' 'bdays' 'helpers' 'main' 'stock' 'smaStrategy' 'tests' 'defines'
do 
	autopep8 --in-place --aggressive --aggressive $files.py
done 

echo "Linting complete"
