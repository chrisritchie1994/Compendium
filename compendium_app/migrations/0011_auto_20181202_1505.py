# Generated by Django 2.1.3 on 2018-12-02 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compendium_app', '0010_auto_20181202_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='journal_id',
            new_name='journal',
        ),
    ]
