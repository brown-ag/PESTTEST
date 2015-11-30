# This part of script file added by SVDAPREP
#
# Delete model input files.
/bin/rm TO.IN
/bin/rm pre_TO.IN
#
# Run PARCALC to compute base parameters from super parameters.
parcalc
#
# The following is copied directly from file ./run_model.sh
#
python tprecal.py tocals pest
./test_alf
#Rscript viewcsv.R tocals 2
