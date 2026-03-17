from django.shortcuts import render

def customPageNotFound(request, exception):
    return render(request, '404.html', status=404)