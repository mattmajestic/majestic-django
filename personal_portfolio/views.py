from django.shortcuts import render

def soccer_api(request):
    return render(request, 'soccer.html', {})