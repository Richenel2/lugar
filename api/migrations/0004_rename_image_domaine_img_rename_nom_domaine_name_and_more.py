# Generated by Django 4.2.5 on 2023-09-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_ecole_email_ecole_link_alter_domaine_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domaine',
            old_name='image',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='domaine',
            old_name='nom',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ecole',
            old_name='description',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='ecole',
            old_name='nom',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ecole',
            old_name='note',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='enseigne',
            old_name='duration',
            new_name='fee',
        ),
        migrations.RenameField(
            model_name='enseigne',
            old_name='domaine',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='enseigne',
            old_name='prix',
            new_name='year',
        ),
        migrations.RenameField(
            model_name='metier',
            old_name='image',
            new_name='img',
        ),
        migrations.RemoveField(
            model_name='ecole',
            name='image',
        ),
        migrations.AddField(
            model_name='ecole',
            name='fee',
            field=models.IntegerField(default=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ecole',
            name='img',
            field=models.URLField(default='a'),
            preserve_default=False,
        ),
    ]
