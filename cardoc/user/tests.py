import json
import unittest

from user.models import *

from django.test import TestCase, Client


class SignUpTest(TestCase):
    def test_sign_up_success(self):
        client = Client()
        user = {
            "email" : "wecode3@naver.com",
            "password" : "123qwe!@",
            "name" : "위코더3"
        }
        response = client.post("/user", json.dumps(user), content_type="application/json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), 
        {
            "id": 1,
            "email": "wecode3@naver.com",
            "password": "pbkdf2_sha256$260000$vYgG3wtQpkqLMZDYu7pIrk$dzcG0pT2i49jRCYPsYh1yZxZpF+oR6HLNsL8e4wGoEo=",
            "name": "위코더3"
        })

    def test_sign_up_password_short_fail(self):
        client = Client()
        user = {
            "email" : "wecode3@naver.com",
            "password" : "123qwe!",
            "name" : "위코더3"
        }
        response = client.post("/user", json.dumps(user), content_type="application/json")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), ["incorrect validation"])
    
    def test_sign_up_key_error(self):
        client = Client()
        user = {
            "email" : "wecode3@naver.com",
            "passwords" : "123qwe!@",
            "name" : "위코더3"
        }
        response = client.post("/user", json.dumps(user), content_type="application/json")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'password': ['This field is required.']})
