from django.shortcuts import render
from work.models import Post


def work_page(request):
    print request
    return render(request, 'work.html', {
        'posts': Post.objects.all().order_by('date_created')})
