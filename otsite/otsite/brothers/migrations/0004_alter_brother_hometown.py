# Generated by Django 4.0.4 on 2022-06-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brothers', '0003_remove_brother_name_brother_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='hometown',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
