# Generated by Django 5.0.6 on 2024-10-15 11:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.blogcategory'),
            preserve_default=False,
        ),
    ]
