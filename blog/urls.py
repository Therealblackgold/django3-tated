
from django.urls import path
from . import views

#we have to specify blog app incase we have mor than one app.
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    #we can also replace int with a string.
    path('<int:blog_id>/', views.detail, name='detail'),
]
