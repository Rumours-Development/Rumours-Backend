from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend_service import views

router = routers.DefaultRouter()
router.register(r'home', views.HomeView, 'backend_service')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include(router.urls))
]