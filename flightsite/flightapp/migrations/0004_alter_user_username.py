# Generated by Django 4.1.7 on 2023-03-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
