# Generated by Django 3.2.9 on 2021-11-30 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0012_alter_tests_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bills',
            old_name='date',
            new_name='bdate',
        ),
        migrations.RenameField(
            model_name='bills',
            old_name='mcost',
            new_name='bmcost',
        ),
        migrations.RenameField(
            model_name='bills',
            old_name='owner',
            new_name='bowner',
        ),
        migrations.RenameField(
            model_name='bills',
            old_name='tcost',
            new_name='btcost',
        ),
        migrations.RemoveField(
            model_name='bills',
            name='rcost',
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
    ]
