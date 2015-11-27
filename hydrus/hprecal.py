with open('./tensio_data/tensio_4_5_14.csv') as f:
    lines = f.readlines()
f.close()
n=0
for l in lines:
	if n != 0:
		ff=l.split(",")
		#print "[ten"+str(n)+"] "+ff[3]+" 1 soil" #for printing obs for control file
		#print "l1 [ten"+str(n)+"]31:44" # for reading fitted values in instruction file
		#print "           "+ff[2]+"         -"+ff[3]+"     1     1        1 "
	n+=1
	
##This part creates PROFILE.DAT given the IC of the observed data
def frange(x, y, jump):
  while x < y:
    yield x
    x += jump
	
def makeICvector(val,depth,maxdepth,disc):
	foob=frange(val-depth,val+(maxdepth-depth),0.5)
	toob=[]
	for i in foob:
		toob.append("{:.6e}".format(i))
	return toob
	
def makeICprofile(val, depth, maxdepth, disc):
	profile_dat=[]
	head=[]
	tail=[]
	head.append("Pcp_File_Version=3")
	head.append("    2")
	head.append("    1  0.000000e+000  1.000000e+000  1.000000e+000")
	head.append("    2 -1.000000e+002  1.000000e+000  1.000000e+000")
	head.append("  "+str(disc*maxdepth)+"    0    0    1 x         h      Mat  Lay      Beta           Axz            Bxz            Dxz          Temp          Conc ")

	tail.append("    1")
	tail.append("   61")
	tail.append('\0')

	for h in head:
		profile_dat.append(h) 

	kekeke=makeICvector(val, depth, maxdepth, disc)
	
	x=0
	for k in kekeke:
		profile_dat.append("   "+str(x+1)+" -"+str("{:.6e}".format((float(x)/disc))) + " " + k + "    1    1  0.000000e+000  1.000000e+000  1.000000e+000  1.000000e+000")
		x+=1
		
	for t in tail:
		profile_dat.append(t)
		
	return profile_dat


prof=makeICprofile(-145, 60, 101, 2)

with open("PROFILE.DAT","w") as out:
	eee=0
	for p in prof:
		if eee!=0:
			out.write("\n")
		out.write(p)
		eee+=1
out.close()