# Generated by Django 5.0.2 on 2024-03-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0007_alter_sa_serial_numbers_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sa_serial_numbers',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
