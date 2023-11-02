from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from azure.monitor.opentelemetry import configure_azure_monitor
configure_azure_monitor()

import logging

print("JEREVOSS: views.py")


# from opentelemetry.instrumentation.django import DjangoInstrumentor

# DjangoInstrumentor().instrument()

def index(request):
    print("index")
    logging.warning("index")
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    print("hello")
    logging.warning("hello")
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')