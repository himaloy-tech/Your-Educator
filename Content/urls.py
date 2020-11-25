from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home' ),
    path('about', views.about, name='about' ),
    path('course', views.courses, name='course' ),
    path('contact', views.contact, name='contact' ),
    path('search', views.search, name='search'),
    path('teacher', views.teacher, name='teacher'),
    path('blog', views.blog, name='blog'),
    path('subscription', views.subscription , name='subscription'),
    path('signup', views.signup , name='signup'),
    path('login', views.login , name='login'),
    path('logout', views.logout , name='logout'),
]