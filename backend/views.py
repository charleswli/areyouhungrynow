from django.shortcuts import render_to_response
from django.http import HttpResponse
import helpers.yelpbusiness as yb
import json

def home(request):
    return HttpResponse('hello world')

def demo_search(request):
    return HttpResponse('search')

def demo_sushi(request, sushi):
    return HttpResponse(sushi)

def demo_business(request, business=''):
    business_json = yb.request(business)
    response = HttpResponse(json.dumps(business_json))
    response["Access-Control-Allow-Origin"] = "*"  
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"  
    response["Access-Control-Max-Age"] = "1000"  
    response["Access-Control-Allow-Headers"] = "*"  
    return response

def demo_yelp(request):
    business_json = yb.request('yelp-san-francisco')
    return HttpResponse(json.dumps(business_json))
