# project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('', RedirectView.as_view(url='/inventory/')),  
    path('accounts/', include('accounts.urls'))
]