from curses.ascii import HT
from urllib.parse import _NetlocResultMixinStr
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.views.generic import TemplateView

from .models import Currency, Value
import csv
import pandas as pd
import io

def index(request):
    template = loader.get_template('helloCryptoApp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['input-file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Please choose a csv file")
        else:
            data_file = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_file)

            # a dictionary to store row_ind:currency_id
            ticker_ids = {}
            for index, row in enumerate(csv.reader(io_string, delimiter=',')):
                # first line is a header line with the ticker symbols and "date"
                # so use this line to create the objects in the Currency table
                if index == 0:
                    for row_ind, symbol in enumerate(row):
                        # skip the first value because that's just "date"
                        if row_ind != 0:
                            c = Currency(ticker_symbol=symbol)
                            c.save()
                            ticker_ids[row_ind] = c.id
                else:
                    # We will only get the date once at the beginning of the loop,
                    # so save it outside of the loop
                    date_value = None
                    for row_ind, input_value in enumerate(row):
                        if row_ind == 0:
                            date_value = pd.to_datetime(input_value, format='%m/%d/%Y')
                        else:
                            curr_id = ticker_ids[row_ind]
                            c = Currency.objects.get(pk=curr_id)
                            curr_value = float(input_value)
                            v = Value(currency=c, date=date_value, value=curr_value)
                            v.save()
        return redirect('line_chart')
    else:
        template = loader.get_template('helloCryptoApp/index.html')
        context = {}
        return HttpResponse(template.render(context, request))

def line_chart(request):

    # dates will be the x axis
    dates = []
    for value in Value.objects.all():
        if value.date not in dates:
            dates.append(value.date)
    currencies = Currency.objects.all()
    # names will be the labels for the different sets of data
    names = [currency.ticker_symbol for currency in currencies]
    # store the values from the db per currency
    # like this [[values1], [values2], ...]
    value_data_per_currency = []
    for currency in currencies:
        value_objs = Value.objects.filter(currency=currency)
        values = [value_obj.value for value_obj in value_objs]
        value_data_per_currency.append(values)

    data = {
        'dates': dates,
        'label': names,
        'data': value_data_per_currency
    }

    template = loader.get_template('helloCryptoApp/line_chart.html')
    return HttpResponse(template.render(data, request))

