from os import path
from django.shortcuts import render
from assistant.models import UserFile
from assistant.models import user_directory_path
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'tools/index.html', context={'title': 'Tools'})

def prepare_excel_index(request):
    return render(request, 'tools/prepare_excel.html', context={'title': 'Excel preparation'})

def prepare_db_excel(request):
    if request.method == 'POST':
        file_owner = User.objects.get(id=2)
        uploaded_user_file = request.FILES['document']
        original_filename = uploaded_user_file.name
        new_user_file = UserFile(user_id=file_owner, original_name=original_filename)
        file_storage_path = user_directory_path(new_user_file, original_filename)
        new_user_file.path = file_storage_path
        new_user_file.save()
        file_system_storage = FileSystemStorage()
        file_system_storage.save(file_storage_path, uploaded_user_file)
        return JsonResponse({
            'status': '200_OK'
        })
