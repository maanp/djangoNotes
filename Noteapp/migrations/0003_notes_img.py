# Generated by Django 3.2.6 on 2022-01-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noteapp', '0002_remove_notes_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='img',
            field=models.ImageField(default=None, upload_to=None),
        ),
    ]
