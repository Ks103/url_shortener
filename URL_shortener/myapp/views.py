
from ast import Pass
from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LongToShort
# Create your views here.


def hello_world(request):
    return HttpResponse("Hello world")


def home_page(request):
    context = {
        "submitted": False,
        "error": False
    }
    if request.method == 'POST':

        data = request.POST
        long_url = data['longurl']
        custom_name = data['custom_name']

        try:
            obj = LongToShort(long_url=long_url, short_url=custom_name)
            obj.save()

            data = obj.data
            clicks = obj.clicks

            context["long_url"] = long_url
            context["short_url"] = request.build_absolute_uri() + custom_name
            context["data"] = data
            context["clicks"] = clicks
            context["submitted"] = True
        except:
            context["error"] = True

    else:
        print("User not sending")

    return render(request, "index.html", context)


def redirect_url(request, short_url):
    row = LongToShort.objects.filter(short_url=short_url)
    if len(row) == 0:
        return HttpResponse("no such short url exist")
    obj = row[0]
    long_url = obj.long_url

    return redirect(long_url)


def task(request):
    context = {
        "my_name": "john",
        "x": 15
    }
    return render(request, "test.html", context)


def all_analytics(request):
    rows = LongToShort.objects.all()
    context = {
        "rows": rows
    }
    return render(request, "all-analytics.html", context)
