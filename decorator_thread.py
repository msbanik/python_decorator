import threading

class thread:
	def __init__(self, f):
		self.f = f
	def __call__(self, *args, **kwargs):
		t = threading.Thread(target=self.f, args=args)
		t.setDaemon(True)
		t.start()


@thread
def sum(x, y):
	print threading.currentThread().getName()
	print x + y


sum(2, 3)	
