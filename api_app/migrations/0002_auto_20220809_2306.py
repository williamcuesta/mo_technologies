# Generated by Django 2.0.9 on 2022-08-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criature',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='criature',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='criature',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
