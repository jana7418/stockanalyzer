# Generated by Django 3.0.7 on 2020-06-14 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200614_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='index',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Index'),
            preserve_default=False,
        ),
    ]