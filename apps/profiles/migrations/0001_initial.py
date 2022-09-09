# Generated by Django 3.1.7 on 2022-09-09 10:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone number')),
                ('phone_number_mobile', models.CharField(blank=True, max_length=12, null=True, verbose_name='Mobile number')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Company Email')),
                ('position', models.CharField(default='', max_length=75, verbose_name='Position')),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='uploads/users/profiles/%Y/%m/%d/', verbose_name='User Image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
