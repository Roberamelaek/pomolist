# myapp/views.py
from django.http import HttpResponse

def listen_view(request):
    print("Request received!")
    return HttpResponse("Request received successfully.")
