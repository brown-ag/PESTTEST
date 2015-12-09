#!/bin/bash
python tprecal.py $1 in $2
cmaes_p $1.pst
python tprecal.py $1 out $2
echo $1
Rscript viewcsv.R $1
