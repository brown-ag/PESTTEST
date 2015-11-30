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

lines=readFile("svd_record.rec")

i=1
foo=[]
flag=False
done=False
for l in range(0,len(lines)):
	if (l % 3) ==0:
		foo.append(str(i)+";"+lines[l+1]+";"+lines[l+2]+";")
		i+=1

maxdecrease=0
whichmaxdecrease=-1
minphi=100
whichminphi=-1
for f in foo:
	parts=f.split(";")
	runid=parts[0].strip()
	startphi=float(parts[1].split("\n")[0].strip().split("=")[1].strip())
	endphi=float(parts[2].split("\n")[0].strip().split("=")[1].strip())
	deltaphi=startphi-endphi
	if deltaphi > maxdecrease:
		maxdecrease=deltaphi
		whichmaxdecrease=runid
	if endphi < minphi:
		minphi=endphi
		whichminphi=runid
		#print(minphi)
	#print(runid+":"+str(startphi)+":"+str(endphi)+":"+str(deltaphi))
	
print("Run with greatest decrease in objective function is ID#"+str(whichmaxdecrease)+" with a decrease of "+str(maxdecrease))
print("Run with lowest objective function is ID#"+str(whichminphi)+" with a PHI="+str(minphi))