__author__ = 'msbanik'

def sugar(func):
	def inner(*args, **kwargs):
		print 'Sugar added'
		func(*args, **kwargs)
	return inner

def milk(func):
	def inner(*args, **kwargs):
		print 'Milk added'
		func(*args, **kwargs)
	return inner

def condiments(func):
	def inner(*args, **kwargs):
		print 'Condiments added'
		func(*args, **kwargs)
	return inner

@milk
@sugar
def coffee_one(name):
	print 'I am: %s' % name	

@sugar
@condiments
def coffee_two(name):
	print 'I am: %s' % name	


coffee_one('Freshly brewed')
print
coffee_two('Vanila flavored')