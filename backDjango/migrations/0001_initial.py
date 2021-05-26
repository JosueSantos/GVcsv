# Generated by Django 3.2.3 on 2021-05-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VulnerabilityItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_hostmane', models.CharField(max_length=200)),
                ('asset_ip_address', models.CharField(max_length=200)),
                ('vulnerability_title', models.CharField(max_length=300)),
                ('vulnerability_severity', models.CharField(max_length=50)),
                ('vulnerability_cvss', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vulnerability_publication_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
