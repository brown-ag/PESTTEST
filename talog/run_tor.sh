#!/bin/bash

python tprecal.py "$1" "in" 
pest $1.pst
python tprecal.py "$1" "out"
Rscript viewcsv.R $1 3 

echo $1
echo $2 
