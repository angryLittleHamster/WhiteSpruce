import abc
from typing import TypeVar, Generic

T = TypeVar('T')

class RetailSalesTaxStrategyBaseClass(metaclass=abc.ABCMeta):
    """Abstract Base Class Definition""" 
    
    @abc.abstractmethod
    def CalculateRetailSalesTaxFor(self, item: T):
        """Required method"""

    @abc.abstractproperty
    def RetailSalesTax(self, value=None):
        """Required property"""