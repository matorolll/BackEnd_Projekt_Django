# Generated by Django 4.2 on 2023-04-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auta_moc_auta_paliwo_auta_spalanie_auta_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='auta',
            name='model',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
