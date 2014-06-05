# 
#
#

import requests
from bs4 import BeautifulSoup
import re
import os

def save_file(URL,session=None,dir="",replace=False,max_size=None,altname=None,chunksize=2048):
	'''
	URL - > URL of the file to be downloaded
	session -> requests session if the file is only available in a session (typically login/auth/etc)
	dir -> directory of the saved file can be either reletive to the script or absoloute path. example: "archive/" saves files in a folder named archive
	replace -> if the file exists (True) replace it / (False) skip
	max_size -> max size of the file in Bytes , if the size exceeds this, download will be aborted
	altname -> name of the saved file ( if None: will attemp to retrive name from server, if fail: will attemp to pars the last part of URL into a file name , if fail: will name the file 'undefined' 
	chunksize -> size of each chunk for writing to disk (A.K.A buffer size)
	'''
	if(altname==None):
		if(session):
			dlh = session.head(URL)
		else:
			dlh= requests.head(URL)
		if (dlh.status_code != 200):
			raise Exception(dlh.status_code)
		try:
			fileheader=dlh.headers['Content-Disposition']
			mat=re.search('filename="(.*)"',fileheader)
			filename=mat.group(1)
		except:
			mat2=re.search("/([^/]+?)$",URL)
			if(mat2):
				filename=mat2.group(1)
			else:
				filename='undefined'
	else:
		filename=altname
		
	if (dir!="" and not os.path.exists(dir)):
		os.makedirs(dir)	
	path=dir+filename	
	if(replace==False and os.path.exists(path)) :
		return True
	else:
		if(session):
			dl = session.get(URL, stream=True)
		else:
			dl = requests.get(URL, stream=True)
		with open(path, 'wb') as f:
			for i,chunk in enumerate(dl.iter_content(chunksize)):
				f.write(chunk)
				if(max_size and f.tell()>max_size):
					dl.close()
					break;
			else:
					return f.tell()
	return False
		
