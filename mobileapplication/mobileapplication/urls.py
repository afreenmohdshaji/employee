"""
URL configuration for mobileapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mobile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobile/all',views.MobileListView.as_view(),name="mobile-all"),
    path('mobile/<int:pk>',views.MobileDetailView.as_view(),name="mobile-detail"),
    path('mobile/<int:pk>/remove',views.MobileDeleteView.as_view(),name="mobile-delete"),
    path('add/',views.MobileCreateView.as_view(),name="mobile-add")

]
