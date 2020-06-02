# Generated by Django 2.2.10 on 2020-05-29 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvt', '0009_auto_20200527_0609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundtransferrecord',
            name='payer',
        ),
        migrations.AddField(
            model_name='fundtransferrecord',
            name='payer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_history', to='mvt.CareSeeker'),
        ),
        migrations.RemoveField(
            model_name='fundtransferrecord',
            name='reciver',
        ),
        migrations.AddField(
            model_name='fundtransferrecord',
            name='reciver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_history', to='mvt.CareTaker'),
        ),
    ]
