# Generated by Django 3.0.5 on 2020-04-09 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='cv',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
