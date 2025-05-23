# Generated by Django 5.1.6 on 2025-04-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WiresInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wire', models.CharField(max_length=15, verbose_name='Марка провода')),
                ('gen_cross_sec', models.FloatField(verbose_name='Общее сечение')),
                ('diametr', models.FloatField(verbose_name='Диаметр')),
                ('weight', models.FloatField(verbose_name='Вес')),
                ('coef_lin_exp', models.FloatField(verbose_name='Коэффициент линейного расширения')),
                ('mod_elast_mat', models.FloatField(verbose_name='Модуль упругости материала')),
                ('max_vol', models.FloatField(verbose_name='Допускаемое напряжение (наибольшие нагрузки)')),
                ('avg_vol', models.FloatField(verbose_name='Допускаемое напряжение (среднегодовая температура)')),
            ],
        ),
    ]
