# Generated by Django 3.0.5 on 2020-04-09 19:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Date_de_naissance', models.DateField(blank=True)),
                ('num_tel', models.CharField(blank=True, max_length=8, unique=True)),
                ('Disponibilite', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('Nb_années_expérience', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('cv', models.FileField(upload_to='')),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
