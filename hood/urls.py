from django.urls import path 
from . import views

urlpatterns=[
   path('',views.home, name='home'),
   path('logout/', views.logoutUser, name='logout'),
   path('profile/',views.profile,name = 'profile'),
   path('comment/<int:id>/',views.comment,name='comment'),
   path('newpost/',views.new_post,name='newpost'),
   path('post/<int:id>/',views.post,name='post'),
]