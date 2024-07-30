from django.shortcuts import render
import random
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Admin,Driver
import json
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from .utils import send_driver_email
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import  BadHeaderError
from smtplib import SMTPException

@csrf_exempt
def admin_signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone_num = data.get('phone_num')
            password = data.get('password')
            address = data.get('address')

            if not (name and email and phone_num and password and address):
                return JsonResponse({'error': 'All fields are required'}, status=400)

            hashed_password = make_password(password)

            admin = Admin.objects.create(
                name=name,
                email=email,
                phone_num=phone_num,
                password=hashed_password,
                address=address
            )

            return JsonResponse({'message': 'Admin created successfully'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if not (email and password):
                return JsonResponse({'error': 'Email and password are required'}, status=400)

            try:
                admin = Admin.objects.get(email=email)
                if check_password(password, admin.password):
                    refresh = RefreshToken.for_user(admin)
                    return JsonResponse({
                        'message': 'Login successful',
                        'access': str(refresh.access_token),
                        'refresh': str(refresh)
                    }, status=200)
                else:
                    return JsonResponse({'error': 'Invalid credentials'}, status=401)
            except Admin.DoesNotExist:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
# def generate_otp():
#     return random.randint(100000, 999999)





@csrf_exempt
def add_driver(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            driver = Driver.objects.create(
                name=data['name'],
                email=data['email'],
                phone_num=data['phone_num'],
                password=data['password'],  # Ensure this is securely hashed
                address=data['address'],
                driving_license_number=data['driving_license_number']
            )
            try:
                send_driver_email(driver)
            except BadHeaderError:
                return JsonResponse({'error': 'Invalid header found.'}, status=400)
            except SMTPException as e:
                return JsonResponse({'error': f'SMTP error occurred: {str(e)}'}, status=500)
            except Exception as e:
                return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

            return JsonResponse({'message': 'Driver added and email sent successfully.'}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Missing fields'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

            


@csrf_exempt
def driver_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if not (email and password):
                return JsonResponse({'error': 'Email and password are required'}, status=400)

            try:
                driver = Driver.objects.get(email=email)
                if check_password(password, driver.password):
                    refresh = RefreshToken.for_user(driver)
                    return JsonResponse({
                        'message': 'Login successful',
                        'access': str(refresh.access_token),
                        'refresh': str(refresh)
                    }, status=200)
                else:
                    return JsonResponse({'error': 'Invalid credentials'}, status=401)
            except Admin.DoesNotExist:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

