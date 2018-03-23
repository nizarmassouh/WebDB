import os,sys
import time
from itertools import izip
queries=open(sys.argv[1])
dirnames=open(sys.argv[2])

for line,dirs in izip(queries,dirnames):
    q=(line.rstrip()).split(',')
    for i,query in enumerate(q):
	dirs=dirs.rstrip()	
	query=query.lstrip(' ')
	print "Downloading "+ query + ":"
	os.system("python ./Download/googleget.py '%s' '%s' %s &" % (query ,dirs,str(i)))
	os.system("python ./Download/yahooget.py '%s' '%s' %s &" % (query ,dirs,str(i)))
	os.system("python ./Download/bingget.py '%s' '%s' %s " % (query ,dirs,str(i)))
	time.sleep(2)
