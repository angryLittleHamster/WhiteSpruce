import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'Model/Patterns/Strategy/RetailTaxStrategies')


from TaxableItem import TaxableItem
from HarmonizedRetailSalesTaxStrategy import HarmonizedRetailSalesTaxStrategy


print ("some Strategies work and some don't")

item = TaxableItem(value=2.00)
print("Item Cost:")
print(item.TaxableAmount)

taxStrategy = HarmonizedRetailSalesTaxStrategy(0.15)
taxes = taxStrategy.CalculateRetailSalesTaxFor(item)

print("Taxes Total: ")
print(taxes)

print("Total: ")
print(item.TaxableAmount + taxes)


