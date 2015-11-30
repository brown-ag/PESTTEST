arggg=commandArgs(TRUE)[1];
arggg2=commandArgs(TRUE)[2];
print(arggg2);
foo=read.csv(paste(arggg,'.csv',sep=""));
minutes=1:96*15;x11();
plot(minutes, foo$Measured[1:96],ylim=c(-2,0));
lines(minutes, foo$Modelled[1:96]);
if(is.na(arggg2)) {
	locator(1)
} else {
	Sys.sleep(arggg2)
}