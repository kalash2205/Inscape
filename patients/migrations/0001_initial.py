# Generated by Django 3.2.9 on 2021-11-27 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meds',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('mname', models.CharField(max_length=200)),
                ('mcost', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(choices=[('p', 'primary'), ('m', 'moderate'), ('a', 'advanced')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('contact', models.IntegerField(blank=True, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('age', models.IntegerField(null=True)),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], max_length=200, null=True)),
                ('arrival', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('IPD', 'In patient'), ('OPD', 'Out patient')], max_length=200, null=True)),
                ('treatment_category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='staff.specialities')),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('tname', models.CharField(choices=[('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', '')], max_length=200)),
                ('tcost', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('rno', models.IntegerField(blank=True, null=True)),
                ('rcost', models.IntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mcost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.meds')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
                ('rcost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.rooms')),
                ('tcost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.tests')),
            ],
        ),
    ]
