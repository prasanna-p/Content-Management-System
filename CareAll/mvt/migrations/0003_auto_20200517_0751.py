# Generated by Django 2.2.10 on 2020-05-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvt', '0002_auto_20200517_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careseeker',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caretaker',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]