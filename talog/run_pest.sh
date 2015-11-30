#!/bin/bash
python tprecal.py $1 in
pest $1.pst
python tprecal.py $1 out
echo $1
Rscript viewcsv.R $1
