# Generated by Django 3.2.3 on 2021-05-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backDjango', '0003_alter_vulnerabilityitem_asset_hostname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vulnerabilityitem',
            options={'verbose_name': 'vulnerability_item', 'verbose_name_plural': 'vulnerability_itens'},
        ),
        migrations.AlterField(
            model_name='vulnerabilityitem',
            name='asset_hostname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterModelTable(
            name='vulnerabilityitem',
            table='vulnerability_item',
        ),
    ]
