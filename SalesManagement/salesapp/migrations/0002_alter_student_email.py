# Generated by Django 4.2.16 on 2024-11-28 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
