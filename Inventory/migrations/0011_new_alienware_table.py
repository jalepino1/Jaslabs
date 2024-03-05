# Generated by Django 5.0.2 on 2024-03-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0010_alienware_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_alienware_table',
            fields=[
                ('serial_number', models.CharField(max_length=100)),
                ('last_checked', models.CharField(max_length=100)),
                ('sa_serial_number', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'new_alienware_table',
                'managed': False,
            },
        ),
    ]
