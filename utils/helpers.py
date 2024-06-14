import os
import random
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail
from .models import OTP
from afya_clinic.settings import BASE_DIR

def otp(self, name, otp, email):
    # verification_link = f"https://3c97-2c0f-fe38-2102-f942-62c5-78b8-6e43-79e6.ngrok-free.app/spinner/account
    # /verify/{email}"
    try:
        email_content = f"""
        <html>
            <head>
                <style>
                    font-size: 12px;
                </style>
            </head>
            <body>
                <p>Hello {name},</p>
                <p style="font-size: 20px, color: black;">Use: <span class="otp" >{otp}</span></p>
                <p>If you did not request this, please ignore. Do not share OTP with anyone.</p>
            </body>
        </html>
        """
        sent = send_mail(
            'Verification OTP',
            '',
            'no-reply@gmail.com',
            [email],
            fail_silently=False,
            html_message=email_content,
        )
        return sent

    except Exception as e:
        # response.setMessage(f"Error sending email: {str(e)}")
        sent = 0
        print(f"Error sending email: {str(e)}")
    return sent


def generateotp(self):
    characters = "0123456789"
    otp = ''.join(random.choice(characters) for _ in range(6))
    return otp


def saveotp(self, otp, email):
    expiry_time = timezone.now() + timedelta(minutes=5)
    otpData = OTP(
        otp=otp,
        email=email,
        expirydate=expiry_time
    )
    otpData.save()
    return None


def send_generated_password(self, name, username, password, email):
    try:
        email_content = f"""
        <html>
            <head>
                <style>
                    font-size: 12px;
                </style>
            </head>
            <body>
                <p>Hello {name},</p>
                <p>Welcome to Alfatah ClinicCare! We're excited to have you join our healthcare community as we embark on this journey together..</p>
                <p>Congratulations! Your account setup is complete and ready to go!</p>
                <p>Here are your login credentials. Please make note of them for future access..</p>

                <p>Your username: {username}</p>
                <p>Your new password: {password}</p>

            </body>
        </html>
        """
        sent = send_mail(
            'Your New Account Credentials',
            '',
            'no-reply@gmail.com',
            [email],
            fail_silently=False,
            html_message=email_content,
        )
        return sent

    except Exception as e:
        sent = 0
        print(f"Error sending email: {str(e)}")
    return sent


def log(self, request):
    current_date = datetime.now().strftime('%Y.%m.%d')
    log_file_name = f"{current_date}-request.log"
    log_dir = os.path.join(BASE_DIR, 'utils/logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file_path = os.path.join(log_dir, log_file_name)
    log_string = f"[{datetime.now().strftime('%Y.%m.%d %I.%M.%S %p')}] => method: {request.method} uri: {request.path} queryString: {request.GET.urlencode()} protocol: {request.scheme} remoteAddr: {request.META.get('REMOTE_ADDR')} remotePort: {request.META.get('REMOTE_PORT')} userAgent: {request.META.get('HTTP_USER_AGENT')}"
    if os.path.exists(log_file_path):
        mode = 'a'
    else:
        mode = 'w'
    with open(log_file_path, mode) as log_file:
        log_file.write(log_string + '\n')