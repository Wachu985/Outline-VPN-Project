# Generated by Django 4.1 on 2022-09-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovpn', '0012_outlineserver_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlinekey',
            name='size',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
    ]
