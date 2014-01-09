__author__ = 'msbanik'
# Thread implementation with decorator
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
	print 'Sum of {0} and {1} is: {2} \n'.format(x, y, x + y)

# running each sum operation on different thread
sum(2, 3)	
sum(4, 5)	
