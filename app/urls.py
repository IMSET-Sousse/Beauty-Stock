from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('', views.home, name='home'),
    path('dashboard/', include('dashboard.urls')),
]
