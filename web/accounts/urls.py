from . import views
from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import SignUpView , TalkCreateView


urlpatterns = [    
    path('unsecure', views.unsecure, name='unsecure'),
    path('secure/', views.secure, name='secure'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logged_out'),
    path("", views.index,name='home'),
    path('signup/',SignUpView.as_view(), name="signup"),
    path('404/',views.error ,name='404'),
    path('board/', views.board,name='board'),
    path('main/', views.main, name='main'),
    path('hello/',views.hello,name='hello'),
    path('talks/', views.talks,name='all_talks'),
    path('talks/talk/<int:id>',views.talk),
    ##path('talks/create', views.talk_create, name='talk_create'),
    path('talks/create', TalkCreateView.as_view(),name='talk_create'),
    path('photo/', views.photo, name='photo')
]
