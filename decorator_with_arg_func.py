__author__ = 'msbanik'
# decorator logger with arguments

def logger(level):
	def outer(func):
		def inner(*args, **kwargs):
			print '\nEntering Func'
			if level == 'DEBUG':
				print '\t Func args: ', args, kwargs
			func(*args, **kwargs)
			print 'Exiting Func'
		return inner
	return outer


@logger('DEBUG')
def sum(x, y):
	print 'Sum of {0} and {1} is: {2}'.format(x, y, x + y)

sum(2, 3)	

@logger('INFO')
def prod(x, y):
	print 'Prod of {0} and {1} is: {2}'.format(x, y, x * y)

prod(2, 3)	
