from django.urls import path

from . import views

urlpatterns = [
    path('index/upload_csv/line_chart', views.line_chart, name='line_chart'),
    path('index/upload_csv/', views.upload_csv, name='upload_csv'),
    path('index/', views.index, name='index'),
]