#!/bin/bash

python tprecal.py "$1" "in" "$2" 1
pest $1.pst
python tprecal.py "$1" "out" "$2" 1
Rscript viewcsv.R $1 0 

#echo $1
#echo $2 
