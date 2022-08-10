from django.contrib import admin
from django.urls import path,include
from Home import views
admin.site.site_header = "Gjs Mayhem Admin"
admin.site.site_title = "Gjs Mayhem Admin Portal"
admin.site.index_title = "Welcome to Gjs Mayhem"
urlpatterns = [
    path('',views.index,name='Home'),
    path('about',views.about,name='Home'),
    path('services',views.services,name='Home'),
    path('Contacts',views.Contacts,name='Home')
]
