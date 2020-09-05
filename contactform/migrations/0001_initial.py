# Generated by Django 2.2.2 on 2020-01-02 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Address', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'College',
                'verbose_name_plural': 'Colleges',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Full Name', max_length=50)),
                ('email', models.EmailField(help_text='Email Address', max_length=254, unique=True)),
                ('message', models.TextField(max_length=1000)),
                ('college', models.ForeignKey(help_text='College', on_delete=django.db.models.deletion.CASCADE, to='contactform.College')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Student',
            },
        ),
    ]