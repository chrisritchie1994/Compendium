# Generated by Django 2.1.3 on 2018-11-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compendium_app', '0006_auto_20181125_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='data_type',
            field=models.CharField(choices=[('Real', 'Real'), ('Test', 'Test')], default='Real', max_length=4),
        ),
    ]
