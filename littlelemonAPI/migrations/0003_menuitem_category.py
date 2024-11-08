# Generated by Django 5.1.2 on 2024-11-07 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemonAPI', '0002_category_alter_menuitem_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='littlelemonAPI.category'),
        ),
    ]