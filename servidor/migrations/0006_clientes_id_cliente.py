# Generated by Django 2.1.4 on 2019-02-28 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0005_sensores_sensor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='id_cliente',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]