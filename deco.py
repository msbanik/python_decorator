def outer(fun):
	def inner(*args, **kwargs):
		print 'logger'
		fun(*args, **kwargs)
	return inner
