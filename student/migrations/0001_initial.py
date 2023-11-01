# Generated by Django 4.2.6 on 2023-10-28 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('school', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('program', models.CharField(max_length=30)),
                ('academic_year', models.CharField(choices=[('FIRST', 'first'), ('SECOND', 'second'), ('THIRD', 'third'), ('FOURTH', 'fourth')], max_length=15)),
                ('year', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
