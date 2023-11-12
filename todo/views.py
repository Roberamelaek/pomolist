# todo/views.py
from django.http import HttpResponse, JsonResponse
import subprocess
import os
from django.views import View

from django.conf import settings

import markdown2  # Use markdown2 instead of markdown

class TodoListView(View):
    def get(self, request, *args, **kwargs):
        todo_files_directory = getattr(settings, 'TODO_FILES_DIRECTORY', '.')
        todo_files = [os.path.join(todo_files_directory, f) for f in os.listdir(todo_files_directory) if f.endswith('.md')]

        todos_data = []
        for todo_file in todo_files:
            with open(todo_file, 'r') as file:
                content = file.read()
                title, description = self.extract_title_and_description(content)

                todos_data.append({
                    'title': title,
                    'description': description,
                })

        return JsonResponse({'todos': todos_data})

    def extract_title_and_description(self, content):
        lines = content.split('\n')
        if lines:
            title_line = lines[0].strip('#').strip()
            title = title_line  # Removed markdown conversion
            description = '\n'.join(lines[1:]).strip()
            return title, description
        return '', ''


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

