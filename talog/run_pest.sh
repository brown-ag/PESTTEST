#!/bin/bash
python tprecal.py to_precal in
pest to_precal.pst
python tprecal.py to_precal out
R --no-save < view_precal.R
pause
