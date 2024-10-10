from django.contrib import admin

# Register your models here.
from .models import Currency, Value

admin.site.register([Currency, Value])