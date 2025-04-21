from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('products/', include('products.urls')),
    path('', RedirectView.as_view(url='/stock/home/')),  
    path('dashboard/', include('dashboard.urls')),
=======
    path('stock/', include('stock.urls')),
    path('', RedirectView.as_view(url='/stock/home/')),  
>>>>>>> 6ab0928b7f4c57d4d5e67f014c789c8a61a4c1e9
]
