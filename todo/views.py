# myapp/views.py
from django.http import HttpResponse

def listen_view(request):
    print("Request received!")
    file_path = '/home/pomolist/file.txt'

    with open(file_path, 'w') as file:
        file.write("Requecest received")

    return HttpResponse("Request received successfully.")
