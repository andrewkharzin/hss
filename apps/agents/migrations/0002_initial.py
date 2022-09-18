# Generated by Django 4.1.1 on 2022-09-18 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("agents", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="agent",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user_agent",
            ),
        ),
    ]
