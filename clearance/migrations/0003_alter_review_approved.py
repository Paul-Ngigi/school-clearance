# Generated by Django 4.2.6 on 2023-12-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clearance', '0002_alter_review_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='approved',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
    ]