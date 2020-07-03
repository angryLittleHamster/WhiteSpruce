class TaxableItem():
    """Implementation of TaxableItem"""
    
    def __init__(self, value=None):
        self._cost = value
    
    @property
    def TaxableAmount(self):
        return self._cost
        