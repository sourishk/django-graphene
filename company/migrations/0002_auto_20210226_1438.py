# Generated by Django 3.1.7 on 2021-02-26 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Company',
        ),
    ]