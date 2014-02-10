from django.shortcuts import render


def work_page(request):
    print request
    return render(request, 'work.html')
