# classmethod example
class Book:
	def len_d(self, x):
		return len(x)

	def __init__(self, name, tame):
		self.name = name
		self.lenf = self.len_d

	def __init__(self, name):
		self.name = name
		self.lenf = self.len_d

	def getlen(self, x):
		return self.lenf(x)

	def __call__(*args, **kwargs):
		print args, kwargs

	def printname(self, ):
		print self.name

	@classmethod	
	def whyiamhere(cls, x):
		print dir(cls)
		print "class method: " + str(x)

	@staticmethod	
	def count(x):
		print __doc__
		print type(__doc__)
		print 'static method: ' + str(x)


# book = Book('Algo')		
# book.printname()
def len_t(s):
	return len(s)

def len_t_2(s):
	return len(s) + 2

book = Book('Algo', '')
setattr(book, 'lenf', len_t)
l = book.getlen('afasdasdf')
print l

book1 = Book('Algo')
# setattr(book1, 'lenf', len_t_2)
l = book1.getlen('afasdasdf')
print l

# book(1, 2, a=1, b=2)
# Book.whyiamhere(10)
# Book.count(10)
# book.__doc__()