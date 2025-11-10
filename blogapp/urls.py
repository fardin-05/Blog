from django.urls import path
from blogapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('new/',views.create_post, name='create_post'),
    path('<int:pk>/edit/',views.edit_post, name='edit_post'),
    path('<int:pk>/delete/',views.delete_post, name='delete_post'),
    path('search/', views.search_posts, name='search_posts'),
]
