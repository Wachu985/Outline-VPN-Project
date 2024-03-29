# Generated by Django 4.1 on 2022-08-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovpn', '0006_alter_outlinekey_limit_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlinekey',
            name='access_url',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Acceso Url'),
        ),
        migrations.AlterField(
            model_name='outlinekey',
            name='key_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Llave ID'),
        ),
        migrations.AlterField(
            model_name='outlinekey',
            name='limit_data',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Limite'),
        ),
        migrations.AlterField(
            model_name='outlinekey',
            name='method',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Metodo'),
        ),
        migrations.AlterField(
            model_name='outlinekey',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='outlinekey',
            name='password',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='outlinekey',
            name='port',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='outlinekey',
            name='used_bytes',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
