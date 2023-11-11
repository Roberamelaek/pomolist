# myapp/views.py
from django.http import HttpResponse
import subprocess
import os


def listen_view(request):
    repo_path = '/home/pomolist/file.txt'

    os.chdir(repo_path)

    try:
        subprocess(['git','pull'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        response_message = "Git pull successful."
    except subprocess.CalledProcessError as e:
        response_message = f"Error during git pull: {e.stderr.decode('utf-8')}"

    return HttpResponse(response_message)