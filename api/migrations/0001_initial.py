# Generated by Django 4.2.5 on 2023-09-19 14:53

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('matieres_principales', django_mysql.models.ListCharField(models.CharField(max_length=32), max_length=132, size=4)),
                ('image', models.ImageField(upload_to='domaines')),
            ],
        ),
        migrations.CreateModel(
            name='Ecole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('note', models.FloatField()),
                ('contact', models.CharField(max_length=16)),
                ('image', models.ImageField(upload_to='ecoles')),
            ],
        ),
        migrations.CreateModel(
            name='Metier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('salaire', models.IntegerField()),
                ('description', models.TextField()),
                ('qualite', django_mysql.models.ListCharField(models.CharField(max_length=32), max_length=132, size=4)),
                ('image', models.ImageField(upload_to='metiers')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Enseigne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(max_length=15)),
                ('prix', models.IntegerField()),
                ('domaine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.domaine')),
                ('ecole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ecole')),
            ],
        ),
    ]
