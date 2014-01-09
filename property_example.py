# property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

# fget is a function to be used for getting an attribute value, and likewise
# fset is a function for setting, and fdel a function for del'ing, an
# attribute.  Typical use is to define a managed attribute x:
class Book(object):
    def getname(self): 
        return self._name
    def setname(self, name): 
        self._name = name
    def delname(self): 
        del self._name
    name = property(getname, setname, delname, "I'm the 'name' property.")

book = Book()
book.name = 'Dive Into Python'

# Decorators make defining new properties or modifying existing ones easy:
class C(object):
    @property
    def x(self): return self._x
    @x.setter
    def x(self, value): self._x = value
    @x.deleter
    def x(self): del self._x
