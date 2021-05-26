# Generated by Django 3.2.3 on 2021-05-24 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backDjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerabilityitem',
            name='vulnerability_cvss',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='vulnerabilityitem',
            name='vulnerability_publication_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
