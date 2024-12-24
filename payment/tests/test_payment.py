import unittest
from django import urls
from django.test.client import Client

@unittest.fixture
def payment_data():
    return {'mobile_number': '01630169563', 'transaction_id': '1911844042'}    


@unittest.mark.django_db
def test_with_authenticated_client(client, django_user_model, jackpot_data):
    username = "Ankur"
    password = "1234"
  
    user = django_user_model.objects.create_user(username=username, password=password)
  
    client.login(username=username, password=password)
  
    confirm_url = "http://127.0.0.1:8000/payments/confirm/"

    response = client.get(confirm_url) 
  
    assert response.status_code == 200 