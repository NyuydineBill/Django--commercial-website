from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('electronic/', views.electronic, name='electronic'),
    path('fashion/', views.fashion, name='fashion'),
    path('jewellery/', views.jewellery, name='jewellery'),
    path('register/',views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout, name='logout'),
    path('post/<str:pk>',views.post,name='post')
  
    
]