# Generated by Django 5.1.6 on 2025-04-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lep', '0002_wiresinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiresinfo',
            name='mod_elast_mat',
            field=models.IntegerField(verbose_name='Модуль упругости материала'),
        ),
    ]
