import os
dictionary={}

def create_MARC(recid, path):
  out = []
  out.append('\t<record>')
  out.append('\t\t<controlfield tag="001">' + str(recid) + '</controlfield>')
  out.append('\t\t<datafield tag="FFT" ind1=" " ind2=" ">\n' +
             '\t\t\t<subfield code="a">' + path + '</subfield>\n' +
             '\t\t\t<subfield code="d">' + "Table of contents" + '</subfield>\n' +
             '\t\t\t<subfield code="t">Additional</subfield>\n' +
             '\t\t</datafield>')
  out.append('\t</record>\n')
  return "\n".join(out)

def createFile(f,out):
  f.write(out)

def loadDictionary():
  global dictionary
  with open("../uSingleRecords.txt") as f:
    for line in f:
      (key, val) = line.split()
      dictionary[int(key)] = val

def main():
  loadDictionary()
  count=0

  f=open("file.xml","w")
  f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
  f.write("<collection>\n")
  pname="/home/nalinc/Desktop/Work/TOC/"
  fname=os.listdir(pname)
  
  for i in xrange(len(fname)):
    isbn = fname[i]
    isbn = fname[i][:17].replace('-','').replace('_','')  #filter first 17 characters to get isbn & remove '-'
    if int(isbn) in dictionary.keys():
      count+=1
      recid=dictionary[int(isbn)]
      path="/afs/cern.ch/user/n/nchhibbe/public/TOC/"+str(fname[i])
#      path="/home/nalinc/Desktop/Work/TestBBM/"+str(fname[i])
      out=create_MARC(recid,path)
      createFile(f,out)


  f.write("</collection>\n")
  f.close()
  print("Done! {0} files processed, {1} accepted".format(len(fname),count))




if __name__ == '__main__':
  main()