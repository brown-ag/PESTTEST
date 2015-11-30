foo=read.csv('to_reg1.csv')
minutes=1:96*15
x11()
plot(minutes, foo$Measured[1:96])
lines(minutes, foo$Modelled[1:96])
locator(1)
