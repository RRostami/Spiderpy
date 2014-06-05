import core
from pydoc import help

def test_save_file():
	print(core.save_file("http://uva.onlinejudge.org/images/banners/cp3_small.png"))
	print(core.save_file("http://uva.onlinejudge.org/images/banners/cp3_small.png",altname="tester.png"))
def test_all_links():
        
	for link in core.all_links("http://www.farsnews.com/NewsV.php?tal=1&i=1"):
		print(link)
help(core.all_links)
