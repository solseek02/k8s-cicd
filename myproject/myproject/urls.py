from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_view, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('chat/', views.chat_view, name='chat'),
    path('chat_api', views.chat_api, name='chat_api'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),
]

