# Generated by Django 4.1 on 2022-08-14 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ovpn', '0009_alter_outlinekey_limit_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlinekey',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ovpn.outlineserver', verbose_name='server_fora'),
        ),
    ]
