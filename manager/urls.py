from django.urls import path

from manager.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home_page')
]