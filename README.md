# fuzzy-wallhack
Archived scripts used to enrich metadata on CDS during CERN Summer Program 2014

## RepoDetails

* **doc/** : `Report_Nalinc.pdf` -  my student report for CERN Summer Student Program 2014
* **src/** : `fetchPDFs.py` - Fetch PDF's and name them with corresponding ISBN(removing special characters) 
* **src/** : `FetchRecordIDs.py` - Fetch record ID's of books from CDS corresponding to ISBN
* **src/** : `sanitize.py`[optional] - Sanitize the records covering following cases
  * Repeated ISBN with same link
  * Repeated ISBN with a different link.
  * Alternate ISBN(found in CDS) with a different link. 
  * Not repeated, however alternate ISBN of the same record with different links.
  * ISBN not found on cds
* **src/** : `createMarcXML.py` - Script to create MarcXML
* **doc/** : `tox.xml` -  Sample marcXML generated for TOC
* **doc/** : `multipleVolumeTOC.xml` -  Sample marcXML generated for TOC with multiple volumes

  




  
