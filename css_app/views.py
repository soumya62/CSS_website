from django.shortcuts import render
def index(request):
    return render(request, 'css_app/home.html', {})
