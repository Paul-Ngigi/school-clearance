# Generated by Django 4.2.6 on 2023-12-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_year',
            field=models.CharField(choices=[('FIRST', 'first'), ('SECOND', 'second'), ('THIRD', 'third'), ('FOURTH', 'fourth'), ('FIFTH', 'fifth'), ('SIXTH', 'sixth')], max_length=15),
        ),
    ]
