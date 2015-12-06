#!/bin/bash
python tprecal.py $1 in
cmaes_p $1.pst
python tprecal.py $1 out
echo $1
Rscript viewcsv.R $1
