import json
from django.http import JsonResponse
import os
from django.conf import settings

def getLineChartData(request):
    return getChartData('line-chart-data.json')

def getBarChartData(request):
    return getChartData('bar-chart-data.json')

def getPieChartData(request):
    return getChartData('pie-chart-data.json')

def getCandlestickData(request):
    return getChartData('candlestick-data.json')

def getChartData(fileName):
    data = None
    with open(os.path.join(settings.BASE_DIR, 'static/data/' + fileName)) as file:
        data = json.load(file)
    return JsonResponse(data)