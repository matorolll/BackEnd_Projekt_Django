# Generated by Django 4.2 on 2023-04-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_auta_zdj_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auta',
            name='zdj_url',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
