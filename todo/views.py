# todo/views.py
from django.http import HttpResponse
import subprocess
import os

def listen_view(request):
    repo_path = '/home/pomolist/Flexo'  # Specify the correct path to your Git repository

    try:
        # Change to the repository directory
        os.chdir(repo_path)
        
        # Run the 'git pull' command
        subprocess.run(['git', 'pull'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        response_message = "Git pull successful."
    except subprocess.CalledProcessError as e:
        response_message = f"Error during git pull: {e.stderr.decode('utf-8')}"
    except Exception as ex:
        response_message = f"Unexpected error: {str(ex)}"
    
    return HttpResponse(response_message)
