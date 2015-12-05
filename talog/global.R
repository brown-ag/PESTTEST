library(cmaes)
foo = function(x) {
	return(1/x)
}
cma_es(10, foo)

