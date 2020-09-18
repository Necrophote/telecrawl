import os
import time, threading

def foo():
	os.system("start crawl.bat")
	print(time.ctime())
	threading.Timer(10, foo).start()

foo()