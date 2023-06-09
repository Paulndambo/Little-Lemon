# define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='home'),
    path("menu/", views.MenuItemView.as_view()),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view()),
    path("booking", include(router.urls)),
]
