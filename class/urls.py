from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('insert/', views.insert, name='insert'),
    path('insert_data/', views.insert_data, name='insert_data'),
    path('view_data/', views.view_data, name='view'),
    path('update/<id>/', views.update, name='update'),
    path('delete_data/<id>/', views.delete_dt, name='delete_data'),
]