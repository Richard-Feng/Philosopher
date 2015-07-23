"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginTest(TestCase):
	"""docstring for LoginTest"""
	def setUp(self):
		user = User.objects.create(username = "donald")
		user.set_password("123456")
		user.save()
	def test_login_fail_with_wrong_password(self):
		response = self.client.post('/accounts/login/', {"username": "donald", "password": "000000" })
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "username and password didn't match")
	def test_login_fail_with_wrong_username(self):
		response = self.client.post('/accounts/login/', {"username": "test", "password": "123456"})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "username and password didn't match")
	def  test_login_success(self):
		response = self.client.post('/accounts/login/', {"username": "donald", "password": "123456" })
		self.assertEqual(response.status_code, 302)
		
class SignUpTest(TestCase):
	"""docstring for SignUpTest"""
	def setUp(self):
		user = User.objects.create(username = "donald")
		user.set_password("123456")
		user.save()
	def test_sign_up_with_exist(self):
		userinfo = {
			"user-username": "donald",
			"user-email": "123456@123.com",
			"user-password1": "123456",
			"user-password2": "123456",
			"userprofile-role": "s",
			"userprofile-gender": "f",
			"userprofile-schoolID": "1234",
			"userprofile-phone": "123456789",
		}
		response = self.client.post('/philosopher/accounts/signup/', userinfo)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "A user with that username already exists.")	
	def test_sign_up_with_wrong_email(self):
		userinfo = {
			"user-username": "test",
			"user-email": "wrongemail",
			"user-password1": "123456",
			"user-password2": "123456",
			"userprofile-role": "s",
			"userprofile-gender": "f",
			"userprofile-schoolID": "1234",
			"userprofile-phone": "123456789",
		}
		response = self.client.post('/philosopher/accounts/signup/', userinfo)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Enter a valid e-mail address.")	

	def test_sign_up_with_different_password(self):
		userinfo = {
			"user-username": "test",
			"user-email": "123456@123.com",
			"user-password1": "123456",
			"user-password2": "000000",
			"userprofile-role": "s",
			"userprofile-gender": "f",
			"userprofile-schoolID": "1234",
			"userprofile-phone": "123456789",
		}
		response = self.client.post('/philosopher/accounts/signup/', userinfo)		
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "The two password fields didn&#39;t match.")	
	
	def test_sign_up_successfully(self):
		userinfo = {
			"user-username": "test",
			"user-email": "123456@123.com",
			"user-password1": "123456",
			"user-password2": "123456",		
			"userprofile-role": "s",
			"userprofile-gender": "f",
			"userprofile-schoolID": "1234",
			"userprofile-phone": "123456789",
		}
		response = self.client.post('/philosopher/accounts/signup/', userinfo)
		self.assertEqual(response.status_code, 302)

	