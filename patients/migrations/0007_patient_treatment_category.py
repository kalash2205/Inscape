# Generated by Django 3.2.9 on 2021-11-29 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20211129_1837'),
        ('patients', '0006_auto_20211129_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='treatment_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.specialities'),
        ),
    ]