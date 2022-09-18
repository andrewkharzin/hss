# Generated by Django 4.1.1 on 2022-09-18 11:50

import apps.orders.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("agents", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "order_number",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "order_createAt",
                    apps.orders.models.CustomDateTimeField(auto_now=True),
                ),
                (
                    "order_updateAt",
                    apps.orders.models.CustomDateTimeField(auto_now_add=True),
                ),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("ACP", "Order accepted"),
                            ("CNF", "Order confirmed"),
                            ("CPD", "Order completed"),
                            ("RJD", "Order rejected"),
                        ],
                        default="ACP",
                        max_length=50,
                    ),
                ),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agent_orders",
                        to="agents.agent",
                    ),
                ),
            ],
        ),
    ]
