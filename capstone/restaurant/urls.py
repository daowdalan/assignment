from django.contrib import admin 
from django.urls import path, include
from . import views
from .views import *

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)


  
urlpatterns = [ 
    path('', views.index, name='index'), 
    path('api/restaurant/menus/', Menuview.as_view(), name='menus'),
    path('api/restaurant/bookings/', Bookingview.as_view(), name='bookings'),
    path('menu/', views.MenuItemView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-retrieve-update-delete'),
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]