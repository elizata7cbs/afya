# Generated by Django 5.0.6 on 2024-06-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('otp', models.TextField()),
                ('expirydate', models.TextField()),
            ],
            options={
                'db_table': 'otps',
            },
        ),
    ]
