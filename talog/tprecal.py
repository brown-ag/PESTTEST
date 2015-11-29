import sys
######
# FUNCTION DEFINITIONS
######

#Reads residual file (.res) output from PEST run and converts to Comma-separated Value (.csv)
def makeCSVfromRES(fprefix):
	lines = readFile(fprefix+'.res')

	colnames=['Name','Group','Measured','Modelled','Res','Wt','WtMeas','WtMod','WtRes','SD','NatWt']

	buf=[]
	flee=""
	for c in colnames:
		flee=flee+c+","
	flee=flee+"\n"
	buf.append(flee)
	for l in lines[1:len(lines)]:
		foob=l.split()
		flee=""
		for oob in foob:
			flee=flee+oob+","
		buf.append(flee+"\n")
	return(writeFile(buf, fprefix+".csv"))

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def readFile(filename):
	lines=None
	try:
		with open(filename) as f:
			lines = f.readlines()
		f.close()
		return(lines)
	except:
		e=sys.exec_info()[0]
		print("Error: "+e)
		return(0)

def writeFile(what, filename):
	flag=1
	try:
		with open(filename,"w") as f:
			for w in what:
				f.write(w)
			f.close()
	except:
		raise
		flag=0
	return(flag)

######
# Main
######
case=sys.argv[1]
mode=sys.argv[2]
print(sys.argv[0]+" for case: "+case+" in mode:"+mode)

if mode == "help" or mode == "h" or mode == "-h":
	print("This is helpful?")
elif mode == "in":
	# Prepare raw data for PEST input
	lines = readFile('../tensio_data/tensio_4_5_14.csv')
	n=0
	ctrl_obs=[]
	ins_obs=[]
	timestamp=[]
	minutes=[]
	matric=[]
	#irrig=[]
	for l in lines:
		if n != 0:
			ff=l.split(",")
			ctrl_obs.append("[ten"+str(n)+"] "+str(float(ff[3])/-100)+" 1 soil")
				#for printing obs for control file
			ins_obs.append("l1 w w w !ten"+str(n)+"!") 
				# for reading fitted values in instruction file
			timestamp.append(str(ff[1]))
			minutes.append(int(ff[2]))
			matric.append(float(ff[3]))
			#irrig.append(ff[4])
		n+=1
		

elif mode == "pest": 
	#executes after instantiating pest but before running the TO model
	irrig=[]
	lines1 = readFile('../tensio_data/tensio_4_5_14.csv')
	for l in lines1[1:len(lines1)]:
		irrig.append(l.split(",")[4])
	lines=readFile("pre_TO.IN")
	startmin=int(float(lines[0].strip()))
	intenslen=int(float(lines[1].strip()))
	duratmin=int(float(lines[2].strip()))
	pulselm=int(float(lines[3].strip()))
	fstart=-1
	start=-1
	end=-1
	duration=0.0
	flag=-1
	n=0
	for i in irrig:
		ii=int(i.strip())
		if ii == 1 and flag==-1:
			flag=1
			start=n
		if ii == 0 and flag==1:
			flag=0
			end=n
		duration=duration+float(ii)
		n+=1
	if flag != 0 or start == -1 or end == -1:
		print("Error integrating irrigation event")
	start=startmin/15
	duration=duratmin/15
	end=start+duration
	#depthinc=float(intenslen)
	depthinc=float(pulselm/duration)
	surfbc=[]
	surfbc.append("Minutes\tP\tE\n")
	for j in range(0,96):
		add=0.0
		if((j-start)>=0 and (j)<end):
			add=depthinc
		take=0 #Zero evapotranspiration
		surfbc.append(str((j)*15)+"\t"+str(add)+"\t"+str(take)+"\n")
	print(surfbc)
	writeFile(surfbc,"SURFACE_BC.IN")
				  
	print("SURFACE B.C. [start: "+str(start*15)+ "min; end: "+str(end*15)+"min; duration: "+str(duration*15)+"min]\n")
	print("Water per timestep: "+str(depthinc)+"mm")
elif mode == "out":
	# Prepare PEST output for viewing
	makeCSVfromRES(case)
else:
	print("This is helpful?")
	
