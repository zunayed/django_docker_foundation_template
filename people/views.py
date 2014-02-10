from django.shortcuts import render
from models import People


def people_page(request):
    return render(request, 'people.html', {
        'people': People.objects.all().order_by('title')})
