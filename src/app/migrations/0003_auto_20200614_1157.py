# Generated by Django 3.0.7 on 2020-06-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200612_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Exchange',
            field=models.CharField(choices=[('NSE', 'NSE'), ('BSE', 'BSE')], default='NSE', max_length=3),
        ),
        migrations.AddConstraint(
            model_name='stock',
            constraint=models.UniqueConstraint(fields=('Symbol', 'Exchange'), name='Unique Stock'),
        ),
    ]