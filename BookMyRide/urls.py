from django.urls import path
from . import views

urlpatterns = [
    path('admin-signup/', views.admin_signup, name='admin_signup'),
        path('admin-login/', views.admin_login, name='admin_login'),
   
    path('add-driver/', views.add_driver, name='add_driver'),
        path('driver-login/', views.driver_login, name='driver_login'),

]
