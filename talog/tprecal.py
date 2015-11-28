with open('../tensio_data/tensio_4_5_14.csv') as f:
    lines = f.readlines()
f.close()
n=0
for l in lines:
	if n != 0:
		ff=l.split(",")
		#print "[ten"+str(n)+"] "+str(float(ff[3])/-100)+" 1 soil" #for printing obs for control file
		#print "l1 w w w !ten"+str(n)+"!" # for reading fitted values in instruction file
		#print "           "+ff[2]+"         -"+ff[3]+"     1     1        1 "
	n+=1
	
with open('to_precal.res') as f:
	lines = f.readlines()
f.close()
colnames=['Name','Group','Measured','Modelled','Res','Wt','WtMeas','WtMod','WtRes','SD','NatWt']

with open('to_precal.csv','w') as f:
	for c in colnames:
		f.write(c)
		f.write(",")
	f.write("\n")

	for l in lines[1:len(lines)]:
		foob=l.split()
		for oob in foob:
			f.write(oob)
			f.write(",")
		f.write("\n")
	f.close()

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump
