import os, sys

from invenio.invenio_connector import InvenioConnector
from time import sleep


isbn = []
recID = []
duplicateRecords = []

def main():

	# Open a file
	#path = "/home/nalinc/Project/Task1/Destination/TOC/.."
	path = "/home/nalinc/Project/Task1/Destination/BBM/Module_1/"
	server_url = "http://cds.cern.ch"

	try:
		server = InvenioConnector(server_url)
	except Exception, e:
		sys.stderr.write("Error: %s\n" % (str(e),))

	global isbn 
	isbn = os.listdir( path )
	# This would print all the files and directories

	for f in xrange(len(isbn)):
   		isbn[f] = isbn[f][:17].replace('-','').replace('_','')  #filter first 17 characters to get isbn & remove '-'

		try:
			rec = server.search(p="020__a:%s" % (isbn[f],), of="id")
			print("{0}\t\t{1}".format(isbn[f],rec))


		except Exception, e:
			sys.stderr.write("Error: %s\n" % (str(e),))
			count = 100
			recid = ""
		sleep(1)



   	func()



def func():
	print("\n{0} files processed".format(len(isbn)))



if __name__ == '__main__':
	main()

