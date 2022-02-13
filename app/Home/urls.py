from os import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import blog.views

urlpatterns = [
    path('', blog.views.homePage, name="homePage"),
    path("admin/", admin.site.urls),
    path("<int:pk>/productInfo/", blog.views.productInfo),
    path("<int:pk>/cart/", blog.views.cart)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
