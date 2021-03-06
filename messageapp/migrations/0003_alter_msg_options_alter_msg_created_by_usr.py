# Generated by Django 4.0.4 on 2022-05-20 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messageapp', '0002_rename_created_by_msg_created_by_usr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msg',
            options={'ordering': ['created_at'], 'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterField(
            model_name='msg',
            name='created_by_usr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
