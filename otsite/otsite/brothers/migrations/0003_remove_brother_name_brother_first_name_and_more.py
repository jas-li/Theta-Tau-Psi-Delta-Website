# Generated by Django 4.0.4 on 2022-05-31 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brothers', '0002_rename_class_year_brother_graduation_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brother',
            name='name',
        ),
        migrations.AddField(
            model_name='brother',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='brother',
            name='hometown',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='brother',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='brother',
            name='graduation_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='brother',
            name='major',
            field=models.CharField(default='', max_length=120),
        ),
    ]