#!/bin/bash

python tprecal.py "$1" "in" "$2"
pest $1.pst
python tprecal.py "$1" "out" "$2"
Rscript viewcsv.R $1 3 

echo $1
echo $2 
