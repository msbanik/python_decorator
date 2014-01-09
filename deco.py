def outer(fun):
	def inner(*args, **kwargs):
		fun(*args, **kwargs)
	return inner
