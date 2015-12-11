arggg=commandArgs(TRUE)[1];
arggg2=commandArgs(TRUE)[2];
print(arggg2);
foo=read.csv(paste(arggg,'.csv',sep=""));
#impu=read.csv("")
minutes=1:96*15;
meas=foo$Measured[1:96]
modu=foo$Modelled[1:96]

flk=paste(sqrt(mean((meas-modu)^2)),"\n")
write(flk,file="foob.out")
print(paste("RMSE: ",sqrt(mean((meas-modu)^2))))

if(arggg2 != -1) {
	x11();
	plot(minutes, meas,ylim=c(-2,0));
	lines(minutes, modu);

	m_meas=max(meas)
	m_modu=max(modu)
	t_meas=minutes[which(meas==m_meas)][1]
	t_modu=minutes[which(modu==m_modu)][1]
	print("Peak time information")
	print(paste("Measured max:",m_meas,"@",t_meas,"minutes"))
	print(paste("Modelled max:",m_modu,"@",t_modu,"minutes"))
	print(paste("Delta max (meas-mod):",m_meas-m_modu))
	print(paste("Delta time (meas-mod):",t_meas-t_modu))

	dmeas=diff(meas)
	dmodu=diff(modu)
	dm_meas=max(dmeas)
	dm_modu=max(dmodu)
	dt_meas=minutes[which(dmeas==dm_meas)]
	dt_modu=minutes[which(dmodu==dm_modu)][1]
	print(paste("dMeasured max:",dm_meas,"@",dt_meas,"minutes"))
	print(paste("dModelled max:",dm_modu,"@",dt_modu,"minutes"))
	print(paste("Delta max (dmeas-dmod):",dm_meas-dm_modu))
	print(paste("Delta time (dmeas-dmod):",dt_meas-dt_modu))



	if(arggg2 == 0) {
		locator(1)
	} else {
		Sys.sleep(arggg2)
	}
}
