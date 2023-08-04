from django.urls import path
from .views import MenuItemView, SingleMenuItemView

urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-item-detail'),
]
