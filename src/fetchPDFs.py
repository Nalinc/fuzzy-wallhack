import urllib2



for line in open("op"):
    columns = line.split("    ")
    if len(columns) >= 2:
#        print(columns[1].rsplit('/',1)[1].replace('-',''))
         try:
     		 f=urllib2.urlopen(columns[1])
	    	 output = open(str(columns[1].rsplit('/',1)[1].replace('-','')),'w')
	    	 output.write(f.read())
	    	 output.close()
         except Exception, e:
         	 print(str(e)+"\n"+str(columns[1]))
         

#f = urllib2.urlopen(columns[1])
#output = open(columns[1],'wb')
#output.write(f.read())
#output.close()