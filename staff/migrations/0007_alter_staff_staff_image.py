# Generated by Django 3.2.9 on 2021-11-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_alter_staff_staff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_image',
            field=models.ImageField(blank=True, default='staffprofiles/user-default.png', null=True, upload_to='staffprofiles/'),
        ),
    ]