# Generated by Django 3.2.9 on 2021-11-28 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_staff_contact'),
        ('patients', '0004_alter_patient_treatment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='treatment_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.specialities'),
        ),
    ]
