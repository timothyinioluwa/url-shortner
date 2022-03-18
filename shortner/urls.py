from django.urls import path
from .views import HomeView,create_link,go_to_page

app_name = 'shortner'

urlpatterns = [
   
    path('',HomeView.as_view(),name='home'),
    path('create/',create_link,name='shorten_link'),
    path('<str:pk>',go_to_page,name='shorten_link'),
]
