# Generated by Django 2.2.2 on 2020-01-02 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='college',
            old_name='Name',
            new_name='name',
        ),
    ]
