from django.shortcuts import render

def management_view(request):
    return render(request, 'manage.index.html', {})

