# Generated by Django 4.2.13 on 2024-07-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
