# Generated by Django 3.2.9 on 2021-11-27 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dname', models.CharField(max_length=200)),
                ('dno', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dhead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialities',
            fields=[
                ('sname', models.CharField(max_length=200)),
                ('sno', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.IntegerField(unique=True)),
                ('address', models.CharField(max_length=500)),
                ('staff_image', models.ImageField(blank=True, default='staffprofiles/user-default.png', null=True, upload_to='staffprofiles/')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]