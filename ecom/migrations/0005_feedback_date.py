# Generated by Django 3.0.5 on 2024-03-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
