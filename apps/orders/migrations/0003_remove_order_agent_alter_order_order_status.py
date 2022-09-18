# Generated by Django 4.1.1 on 2022-09-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="agent",
        ),
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("ACCEPTED", "Order accepted"),
                    ("CONFIRMED", "Order confirmed"),
                    ("COMPLETED", "Order completed"),
                    ("REJECTED", "Order rejected"),
                ],
                default="ACCEPTED",
                max_length=50,
            ),
        ),
    ]
