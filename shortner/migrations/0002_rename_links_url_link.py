# Generated by Django 3.2.5 on 2021-09-15 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='links',
            new_name='link',
        ),
    ]
