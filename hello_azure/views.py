from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from azure.monitor.opentelemetry import configure_azure_monitor
# configure_azure_monitor()

# from opentelemetry.sdk._logs.export import ConsoleLogExporter, BatchLogRecordProcessor
# from opentelemetry._logs import get_logger_provider
# log_exporter = ConsoleLogExporter()
# log_record_processor = BatchLogRecordProcessor(
#     log_exporter,
# )
# get_logger_provider().add_log_record_processor(log_record_processor)

# from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor
# from opentelemetry.trace import get_tracer_provider
# trace_exporter = ConsoleSpanExporter()
# trace_processor = BatchSpanProcessor(
#     trace_exporter,
# )
# get_tracer_provider().add_span_processor(trace_processor)

import logging

print("JEREVOSS: views.py")
from django.conf import settings
print("JEREVOSS: settings.DEBUG: %s" % settings.DEBUG)
print("JEREVOSS: settings.ALLOWED_HOSTS: %s" % settings.ALLOWED_HOSTS)
settings_middleware = getattr(settings, "MIDDLEWARE", [])
print("JEREVOSS: veiws settings.MIDDLEWARE: %s" % settings_middleware)


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