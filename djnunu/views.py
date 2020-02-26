from django.shortcuts import render

def home_view(request):
    context = {
        'page_title': 'Home Page'
    }
    return render(request, 'home.html', context)