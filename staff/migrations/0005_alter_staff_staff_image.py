# Generated by Django 3.2.9 on 2021-11-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20211129_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_image',
            field=models.ImageField(blank=True, default='staffprofiles/doctordefault.png', null=True, upload_to='staffprofiles/'),
        ),
    ]
