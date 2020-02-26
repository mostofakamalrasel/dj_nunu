from django.shortcuts import render

def about_view(request):
    context = {
        'page_title': 'About Page'
    }
    return render(request, 'pages/about.html', context)