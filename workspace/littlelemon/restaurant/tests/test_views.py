# test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient  # Import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(Title='Menu 1', Price=9.99, Inventory=100)
        Menu.objects.create(Title='Menu 2', Price=12.50, Inventory=75)
        Menu.objects.create(Title='Menu 3', Price=8.75, Inventory=50)

    def test_getall(self):
        # Create a user and a token
        user = User.objects.create_user(username='atestuser', password='atestpassword')
        token = Token.objects.create(user=user)
        
        # Create an instance of the APIClient
        client = APIClient()
        # Use reverse with the full URL path, including the app name
        url = reverse('menu-list-create')
        
        # Add the token to the request headers using force_authenticate
        client.force_authenticate(user=user, token=token)
        response = client.get(url)

        # Check if the request is successful (HTTP 200 status code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the test instances of the Menu model
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)