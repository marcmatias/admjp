from django.urls import path
from . import views

app_name = 'sistema'

urlpatterns = [
    path('', views.IndexListView.as_view(), name="home"),
]
