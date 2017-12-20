from django.shortcuts import get_object_or_404, redirect, render
from cocukcacim.apps.page.models import Page


def index(request):
    return render(request, 'page.index.html')


def page(request, page_id=None, **kwargs):
    current_page = get_object_or_404(Page, id=page_id)

    if not current_page.get_context():
        return redirect(current_page.sub_pages.first())

    return render(request, 'page.index.html', {
        'page': current_page
    })
