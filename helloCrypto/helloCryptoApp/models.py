from django.db import models

# Have a Currency model to store the different ticker symbols
class Currency(models.Model):
    class Meta:
        db_table = 'currency'

    ticker_symbol = models.CharField(max_length=5)

# Have a Value model to store the currency, date, and value
# I set the on_delete to PROTECT so you can't cascade delete info
class Value(models.Model):
    class Meta:
        db_table = 'value'
        
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    date = models.DateField()
    value = models.FloatField()