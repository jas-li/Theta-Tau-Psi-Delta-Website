# Generated by Django 4.0.4 on 2022-05-28 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brothers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brother',
            old_name='class_year',
            new_name='graduation_year',
        ),
    ]
