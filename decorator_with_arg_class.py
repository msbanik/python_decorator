class logger:
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
	def __call__(self, func):
		print self.args, self.kwargs
		def outer(*args, **kwargs):
			func(*args, **kwargs)
		return outer

@logger('DEBUG')
def sum(x, y):
	print 'Sum of {0} and {1} is: {2}'.format(x, y, x + y)

sum(2, 3)	