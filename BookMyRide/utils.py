# utils.py

from django.core.mail import send_mail

def send_driver_email(driver):
    subject = 'Driver Details'
    message = (
        f'Driver ID: {driver.driver_id}\n'
        f'Name: {driver.name}\n'
        f'Phone Number: {driver.phone_num}\n'
        f'Email: {driver.email}\n'
        f'Password:{driver.password}\n'
        f'Address: {driver.address}\n'
        f'Driving License Number: {driver.driving_license_number}'
    )
    email_from = 'shalinijoshi226@gmail.com'
    recipient_list = [driver.email]

    send_mail(subject, message, email_from, recipient_list)
