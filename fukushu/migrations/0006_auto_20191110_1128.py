# Generated by Django 2.1.7 on 2019-11-10 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fukushu', '0005_auto_20191110_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='totomodel',
            old_name='probrem1',
            new_name='problem1',
        ),
        migrations.RenameField(
            model_name='totomodel',
            old_name='probrem2',
            new_name='problem2',
        ),
    ]
