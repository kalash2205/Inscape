# Generated by Django 3.2.9 on 2021-11-29 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_patient_treatment_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meds',
            name='category',
        ),
    ]
