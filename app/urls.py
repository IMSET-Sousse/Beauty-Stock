from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('product/', include('product.urls')),
    path('', views.home, name='home'),
    path('dashboard/', include('dashboard.urls')),
=======
    path('stock/', include('stock.urls')),
    path('', RedirectView.as_view(url='/stock/home/')),  
>>>>>>> a79e0c3354aaa37c9598c1f698af23f4c998c8eb
]
