# Generated by Django 3.1.2 on 2021-06-29 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Depertment',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='depertment',
            new_name='department',
        ),
    ]
