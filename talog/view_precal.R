foo=read.csv('to_precal.csv')
minutes=1:96*15
x11()
plot(minutes, foo$Measured)
lines(minutes, foo$Modelled)
locator(1)