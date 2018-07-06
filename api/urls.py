from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='validate'),
    path('read/',views.read,name='read'),
    path('update/<str:user_username>/',views.update,name='update'),
    path('delete/<str:user_username>/',views.delete,name='delete')
]