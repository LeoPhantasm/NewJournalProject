from django.urls import path
from .views import Index, Home, SignUpView, Dashboard, EditItem, DeleteItem
import NewSystem
from django.contrib.auth import views as auth_views
urlpatterns=[
        path('', Index.as_view(), name='index'),
        path('dashboard/', Dashboard.as_view(), name='dashboard'),
        path('signup/', SignUpView.as_view(), name='signup'),
        path('login/', auth_views.LoginView.as_view(template_name='NewSystem/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='NewSystem/logout.html'), name='logout'),
        path('edit-item/<int:pk>', EditItem.as_view(), name='edit-item'),
        path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
        path('home/', Home.as_view(), name='home'),
    ]
