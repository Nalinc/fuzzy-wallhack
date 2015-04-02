from invenio.search_engine import perform_request_search
from invenio.search_engine_utils import get_fieldvalues

isbns = [] # List of ISBNs as strings
links = [] # List of TOC links as strings

print len(isbns)
print len(links)

ls_len = range(len(isbns))
ls = []

for i in ls_len:
    ls.append((isbns[i], links[i]))
ls = list(set(ls))

isbns = [x[0] for x in ls]
links = [x[1] for x in ls]

rep_isbns = set([x for x in isbns if isbns.count(x) > 1]) #Repeated isbns with a different link.
#rep_alt_isbns = [] #Repeated isbn(alternate, found in CDS) with a different link.
alt_isbns = [] #Not repeated, however alternate isbns of the same book with different links.
not_found = [] # ISBNs not found.
dupl_isbns = []

i = 0
while 1:
    if i >= len(isbns): break
    recids = perform_request_search(p='020__a:'+str(isbns[i]), of="id")
    if not recids:
        not_found.append(isbns[i])
        del links[i]
        del isbns[i]
        #if i != 0: i -= 1
        continue
    elif len(recids) > 1: dupl_isbns.append((recids, isbns[i]))
    else:
        isbs = get_fieldvalues(recids[0], '020__a')
        isbn = isbns[i]
        if isbn in isbs: isbs.remove(isbn)
        for isb in isbs:
            if isb in isbns:
                if isb in rep_isbns: isbns[i] = isb
                else:
                    if links[i] == links[isbns.index(isb)]:
                        del links[i]
                        del isbns[i]
                        i -= 1
                        break
                    else:
                        alt_isbns.append((recids[0], isbn, isb))
    i += 1


ls_len = range(len(isbns))
ls = []

for i in ls_len:
    ls.append((isbns[i], links[i]))
ls = list(set(ls))

isbns = [x[0] for x in ls]
links = [x[1] for x in ls]

ls_len = range(len(isbns))
for i in ls_len:
    print str(isbns[i]) + '    ' + str(links[i])

rep_isbns = set([x for x in isbns if isbns.count(x) > 1])
print rep_isbns

rep_links =  list(set([x for x in links if links.count(x) > 1]))
ls_len = range(len(rep_links))
for i in ls_len:
    print rep_links[i]


alt_isbns = list(set(alt_isbns))

for (x,y,z) in alt_isbns:
    if (x,z,y) in alt_isbns: alt_isbns.remove((x,y,z))


print len(isbns)
print len(links)

print len(not_found)
print len(rep_isbns)
print len(rep_links)
print len(alt_isbns)
print len(dupl_isbns)

print not_found
print alt_isbns
print dupl_isbns