from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.index, name='index'),
    path('post/<str:slug>', views.detail, name='detail'),
    path('new-url', views.newUrlView, name='newUrl'),
    path('old-url', views.oldUrlRedirect, name='oldUrl'),
    path('contact', views.contactView, name='contact'),
    path('about', views.aboutView, name='about')
]
