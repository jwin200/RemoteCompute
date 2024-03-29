# Generated by Django 3.2 on 2021-05-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutableModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=120)),
                ('file', models.FileField(default=None, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('file_type', models.CharField(choices=[('PY', '.py'), ('JV', '.java'), ('C++', '.cpp')], default=None, max_length=120)),
                ('user', models.CharField(default=None, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='FileTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=120, null=True)),
                ('file', models.FileField(default=None, null=True, upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]
