from django.urls import path
from .views import MenuItemView, SingleMenuItemView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-item-detail'),
    # path('message/',views.msg, name='message'),
    path('token-auth/', obtain_auth_token, name='token-auth'),
]
