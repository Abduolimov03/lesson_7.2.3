from django.urls import path
from .views import air_list, air_detail, air_create, air_update, air_delete

urlpatterns = [
    path('', air_list, name='air_list'),
    path('detail/<int:pk>', air_detail, name='air_detail'),
    path('create', air_create, name='air_create'),
    path('update/<int:pk>', air_update, name='air_update'),
    path('delete/<int:pk>', air_delete, name='air_delete')
]