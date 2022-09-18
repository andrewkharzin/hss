# Generated by Django 4.1.1 on 2022-09-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("stuffs", "0001_initial"),
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="aogservice",
            name="aog_item",
            field=models.ManyToManyField(to="stuffs.aog"),
        ),
        migrations.AddField(
            model_name="aogservice",
            name="responsibles_persons",
            field=models.ManyToManyField(to="services.dutyperson"),
        ),
    ]
