from django.shortcuts import render

def index(request):
    return render(request, 'tools/index.html', context={'title': 'Tools'})

def prepare_excel(request):
    return render(request, 'tools/prepare_excel.html', context={'title': 'Excel preparation'})
