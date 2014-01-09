# function decorator
def outer(fun):
	def inner(*args, **kwargs):
		print 'logger'
		fun(*args, **kwargs)
	return inner

def prod(x, y):
	return x * y

prod = outer(prod)
print prod(2, 3)
