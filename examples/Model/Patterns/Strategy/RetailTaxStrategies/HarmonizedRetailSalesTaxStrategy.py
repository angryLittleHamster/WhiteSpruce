from TaxableItem import TaxableItem
from RetailSalesTaxStrategy import RetailSalesTaxStrategyBaseClass
from typing import TypeVar, Generic

T = TypeVar('TaxableItem')

class HarmonizedRetailSalesTaxStrategy(RetailSalesTaxStrategyBaseClass):
    """Implementation of RetailSalesTaxStrategy"""
    
    def __init__(self, value=None):
        self._retailSalesTax = value

    def CalculateRetailSalesTaxFor(self, item: T):
        """Implementation of abstract method"""
        if item.TaxableAmount < 0.00:
            #throw new RetailTaxCalculatorException($"Invalid Taxable Amount: {item.TaxableAmount:C} for {nameof(RetailSalesTax)}: {RetailSalesTax}");
            print("Exception for calc taxes")
            return -1.0
        elif item.TaxableAmount == 0.00:
            return 0.00
        else:
            return self._retailSalesTax * item.TaxableAmount
    
    @property
    def RetailSalesTax(self):
        """Implementation of abstract property"""
        return self._retailSalesTax