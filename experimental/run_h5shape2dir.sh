#!/bin/zsh

#echo $1

for filename in $1/*.h5; do
    #echo $filename
    python3 h5shape.py -i $filename
done
