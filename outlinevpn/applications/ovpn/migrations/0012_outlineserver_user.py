# Generated by Django 4.1 on 2022-08-15 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ovpn', '0011_alter_outlinekey_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlineserver',
            name='user',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='user_server', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
