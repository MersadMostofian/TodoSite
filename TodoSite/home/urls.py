from django.urls import path
from . import views

urlpatterns = [
    path('',views.root,name='root'),
    path('home/',views.home,name='homePage'),
    path('detile/<int:todo_id>',views.detile,name='detiles'),
    path('delete/<int:todo_id>',views.delete,name='delete'),
    path('create/',views.create,name='create'),
    path('update/<int:todo_id>',views.update,name='update'),
]