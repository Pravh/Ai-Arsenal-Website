from django.urls import path,include

from .views import DashboardListView,register,index

urlpatterns = [
    path('dashboard/',DashboardListView.as_view(),name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',register,name='register'),
    path('oauth/',include('social_django.urls')),
    path('',index,name='index'),
]