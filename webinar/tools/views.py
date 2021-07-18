from django.shortcuts import render
from assistant.models import UserFile

def index(request):
    return render(request, 'tools/index.html', context={'title': 'Tools'})

def prepare_excel(request):
    userfile = UserFile.objects.first()
    return render(request, 'tools/prepare_excel.html', context={
        'title': 'Excel preparation',
        'filepath': userfile.path
        })
