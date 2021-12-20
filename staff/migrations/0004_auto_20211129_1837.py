# Generated by Django 3.2.9 on 2021-11-29 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20211129_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='speciality',
        ),
        migrations.AddField(
            model_name='specialities',
            name='sowner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff'),
        ),
    ]
