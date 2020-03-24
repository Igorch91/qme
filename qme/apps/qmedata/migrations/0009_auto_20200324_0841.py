# Generated by Django 3.0.3 on 2020-03-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qmedata', '0008_deviations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deviations',
            options={'verbose_name': 'Отклонение', 'verbose_name_plural': 'Отклонения'},
        ),
        migrations.AddField(
            model_name='deviations',
            name='dev_fil_pd',
            field=models.FloatField(default=8),
        ),
        migrations.AddField(
            model_name='deviations',
            name='dev_one_size',
            field=models.FloatField(default=0.04),
        ),
        migrations.AddField(
            model_name='deviations',
            name='dev_sdl_size',
            field=models.FloatField(default=0.004),
        ),
        migrations.AddField(
            model_name='deviations',
            name='dev_sig_pd',
            field=models.FloatField(default=4),
        ),
        migrations.AddField(
            model_name='deviations',
            name='dev_two_size',
            field=models.FloatField(default=0.04),
        ),
        migrations.AddField(
            model_name='deviations',
            name='dev_vent',
            field=models.FloatField(default=1),
        ),
    ]