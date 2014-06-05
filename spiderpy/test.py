import core


def test_save_file():
	print(core.save_file("http://uva.onlinejudge.org/images/banners/cp3_small.png"))
	print(core.save_file("http://uva.onlinejudge.org/images/banners/cp3_small.png",altname="tester.png"))
test_save_file()