import abc
#Example of an abstract base class
class MyAbstractBaseClass(metaclass=abc.ABCMeta):
    """Abstract Base Class Definition""" 
    
    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    @abc.abstractproperty
    def some_property(self):
        """Required property"""


class MyChildClass(MyAbstractBaseClass):
    """Implementation of MyAbstractBaseClass"""
    
    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        """Implementation of abstract method"""
        self._myprop *= 2 + value
    
    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._myprop

# Bad Class with result in 
# TypeError: Can't instantiate abstract class BadClass with abstract methods do_something, some_property
# class BadClass(MyAbstractBaseClass):
#     pass

#code to run
#badClass = BadClass()
a = MyChildClass(value=42)
print (a.some_property)
a.do_something(value=41)
print (a.some_property)
    
