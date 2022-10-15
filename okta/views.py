from django.shortcuts import render

def okta(request):
    return render(request, 'okta.html', {})