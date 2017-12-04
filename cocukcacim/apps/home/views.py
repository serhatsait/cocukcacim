from django.shortcuts import render
from cocukcacim.apps.block.models import Block


def yasir(request):
    blocks = Block.objects.all()

    return render(request, 'index.home.html', {'blocks': blocks})
