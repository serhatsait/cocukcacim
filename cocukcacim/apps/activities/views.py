from django.shortcuts import render
from django.utils import timezone
from .models import Activity



def activity_view(request):
    posts = Activity.objects.filter(created_at__lte=timezone.now())
    return render(request, 'activity.index.html', {'posts': posts})

<<<<<<< HEAD
=======

def index(request):
    pass


def event(request):
    pass
>>>>>>> 4ec23b58334a5dc91a5a4e046eb635b7409f529f
