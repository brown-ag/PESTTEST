rm svd_record.rec
for a in {1..100}
do
	rm tocal.bpa
	rm tocal.res
	rm rocals.rec
	#parrep random$a.par tocal.pst temp.pst
	parrep pnul$a.par tocal.pst.bak tocal.pst
	#./run_pest.sh temp
	#pest temp
	pest tocals

	echo "$a" >> svd_record.rec
	grep -F "Sum of squared weighted" tocals.rec >> svd_record.rec
	
	cp tocal.bpa ./svd/tocal.bpa.$a
	cp tocal.res ./svd/tocal.res.$a
	cp tocal.rec ./svd/tocal.rec.$a
	cp tocals.rec ./svd/tocals.rec.$a
done
