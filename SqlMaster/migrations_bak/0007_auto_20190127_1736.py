# Generated by Django 2.1.5 on 2019-01-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SqlMaster', '0006_auto_20190127_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='protocol',
            field=models.CharField(default='CoAP', max_length=4, verbose_name='接入协议'),
        ),
    ]