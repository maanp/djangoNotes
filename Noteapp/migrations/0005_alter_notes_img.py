# Generated by Django 3.2.6 on 2022-01-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noteapp', '0004_alter_notes_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='img',
            field=models.ImageField(default=None, upload_to='static1/img'),
        ),
    ]
