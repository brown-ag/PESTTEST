for /L %%i in (1,1,100) do (
del temp.pst
del temp.res
parrep random%%i.par precal.pst temp.pst
pest temp
copy temp.res temp.res.%%i)