from django.urls import path

from pages.views import about_view

app_name = 'pages'

urlpatterns = [
    path('', about_view, name='about')
]
