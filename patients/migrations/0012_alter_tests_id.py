# Generated by Django 3.2.9 on 2021-11-30 01:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0011_alter_tests_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
