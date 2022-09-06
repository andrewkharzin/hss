# Generated by Django 3.1.7 on 2022-09-06 04:37

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(blank=True, max_length=15, null=True)),
                ('agent_company', models.CharField(choices=[('NW_TECH', 'Nord Avia Technics'), ('AFL_TDO', 'Aeroflot Technics Directions'), ('SKY_TECH', 'Sky technik'), ('UNSiGN', 'UNSIGN')], default='UNSiGN', max_length=50, null=True, verbose_name='Agent company')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('phone_number_mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]
