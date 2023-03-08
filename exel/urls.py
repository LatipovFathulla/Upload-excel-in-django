from django.contrib import admin
from django.urls import path

from api_exel.views import ProductList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', ProductList.as_view())
]
