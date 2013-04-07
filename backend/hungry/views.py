from django.shortcuts import render_to_response
from django.http import HttpResponse
import helpers.yelpbusiness as yb
import models
import json

def home(request):
    return HttpResponse('hello world')

def response_xdomain_access(data):
    response = HttpResponse(data)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def business_all(request):
    b_all = models.Business.objects.all()
    return_json = {}
    l = []
    for b in b_all:
        d = {}
        d['yelp_id'] = b.yelp_id.encode('utf-8')
        d['json_data'] = b.json_data.encode('utf-8')
        l.append(d)
    return_json['businesses'] = l
    return response_xdomain_access(str(return_json))

def business_single(request, business):
    businesses = models.Business.objects.all()
    return HttpResponse(str(businesses))
