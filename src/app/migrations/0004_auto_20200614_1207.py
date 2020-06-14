# Generated by Django 3.0.7 on 2020-06-14 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200614_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='index',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Index'),
        ),
    ]
